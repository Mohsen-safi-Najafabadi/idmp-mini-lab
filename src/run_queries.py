
from pathlib import Path
from rdflib import Graph

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "src" / "queries"
OUT = ROOT / "outputs" / "query_results"
OUT.mkdir(parents=True, exist_ok=True)

def run_query(name: str):
    g = Graph()
    g.parse(ROOT / "outputs" / "graph.ttl", format="turtle")
    q = (QDIR / name).read_text(encoding="utf-8")
    res = g.query(q)
    # Write CSV
    out = OUT / (name.replace(".rq", ".csv"))
    with open(out, "w", encoding="utf-8") as f:
        # header
        f.write(",".join(res.vars) + "\n")
        for row in res:
            f.write(",".join(str(x) for x in row) + "\n")
    print(f"✅ {name} -> {out}")

if __name__ == "__main__":
    # run both queries
    run_query("product_substance_route.rq")
    run_query("substance_synonyms.rq")
