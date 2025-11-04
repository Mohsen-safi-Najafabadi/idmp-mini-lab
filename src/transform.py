
from pathlib import Path
import pandas as pd
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, SKOS, XSD, DCTERMS

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"

EX = Namespace("https://example.org/idmp/")
RMS = Namespace("https://spor.ema.europa.eu/rms/")  # demo namespace base for RMS concept IRIs
SCHEMA = Namespace("https://schema.org/")

def uri(ns, local):
    return URIRef(ns + local)

def load_csv(name):
    return pd.read_csv(DATA / name)

def add_routes(g, df):
    for _, row in df.iterrows():
        rid = str(row["identifier"])
        r = uri(EX, f"route/{rid}")
        g.add((r, RDF.type, EX.RouteOfAdministration))
        g.add((r, SKOS.prefLabel, Literal(row["term_name"])))
        g.add((r, EX.status, Literal(row["status"])))
        if pd.notna(row["source_id"]):
            g.add((r, EX.sourceId, Literal(str(row["source_id"]))))
        # Link to an RMS-like IRI pattern (demo)
        g.add((r, SKOS.exactMatch, uri(RMS, f"term/{rid}")))

def add_substances(g, df):
    for _, row in df.iterrows():
        sid = row["substance_id"]
        s = uri(EX, f"substance/{sid}")
        g.add((s, RDF.type, EX.Substance))
        g.add((s, SKOS.prefLabel, Literal(row["preferred_term"])))
        if pd.notna(row.get("inn")):
            g.add((s, EX.inn, Literal(row["inn"])))
        if pd.notna(row.get("cas")):
            g.add((s, EX.cas, Literal(row["cas"])))
        if pd.notna(row.get("synonyms")):
            for alt in [a.strip() for a in str(row["synonyms"]).split(";")]:
                if alt:
                    g.add((s, SKOS.altLabel, Literal(alt)))

def add_orgs(g, df):
    for _, row in df.iterrows():
        oid = row["org_id"]
        o = uri(EX, f"org/{oid}")
        g.add((o, RDF.type, EX.Organization))
        g.add((o, SKOS.prefLabel, Literal(row["org_name"])))
        for col, pred in [("org_type", EX.organizationType), ("country", EX.country), ("lei", EX.lei)]:
            if pd.notna(row.get(col)):
                g.add((o, pred, Literal(row[col])))

def add_products(g, df_products, df_routes, df_substances, df_orgs):
    routes = {str(r["identifier"]): r for _, r in df_routes.iterrows()}
    subs = {r["substance_id"]: r for _, r in df_substances.iterrows()}
    orgs = {r["org_id"]: r for _, r in df_orgs.iterrows()}

    for _, row in df_products.iterrows():
        pid = row["product_id"]
        p = uri(EX, f"product/{pid}")
        g.add((p, RDF.type, EX.MedicinalProduct))
        g.add((p, SKOS.prefLabel, Literal(row["product_name"])))
        # route link (to our local route resource)
        route_code = str(row["route_code"])
        g.add((p, EX.hasRoute, uri(EX, f"route/{route_code}")))
        # substance link
        g.add((p, EX.hasSubstance, uri(EX, f"substance/{row['substance_id']}")))
        # org link
        g.add((p, EX.hasOrganization, uri(EX, f"org/{row['org_id']}")))
        # authorization date
        g.add((p, DCTERMS.issued, Literal(row["authorization_date"], datatype=XSD.date)))

def build_graph():
    g = Graph()
    g.bind("ex", EX)
    g.bind("skos", SKOS)
    g.bind("dct", DCTERMS)

    df_routes = load_csv("routes_of_administration.csv")
    df_substances = load_csv("substances.csv")
    df_orgs = load_csv("organizations.csv")
    df_products = load_csv("products.csv")

    add_routes(g, df_routes)
    add_substances(g, df_substances)
    add_orgs(g, df_orgs)
    add_products(g, df_products, df_routes, df_substances, df_orgs)

    OUT.mkdir(exist_ok=True, parents=True)
    ttl_path = OUT / "graph.ttl"
    g.serialize(destination=str(ttl_path), format="turtle")
    print(f"✅ Wrote {ttl_path}")
    return g

if __name__ == "__main__":
    build_graph()
