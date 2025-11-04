#Mohsen

# IDMP Mini Lab (Demo)

A tiny, reproducible demo that **turns CSVs & public code lists into a documented RDF graph**, runs a couple of **SPARQL** queries, and produces clean, reviewable outputs.

> Focus: routes of administration (subset from EMA RMS), substances, organizations, and products.

## Why this stack?
- **Python (pandas + rdflib)** – clean ETL + RDF generation with minimal dependencies.
- **SPARQL** – show how the graph is queryable (lineage, lookups).
- **CSV in /data + mapping note in /mappings** – reviewers can audit sources and transformations.
- **Deterministic outputs in /outputs** – ideal for code reviews and POCs.

## Sources (for the demo)
- **Routes of Administration**: subset manually curated from EMA SPOR RMS terms (see`data/routes_of_administration.csv`).  
- **Products/Substances/Organizations**: synthetic sample for demo purposes only (no PHI).



## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 1) Build the RDF graph (outputs/graph.ttl)
python src/transform.py

# 2) Run SPARQL queries (writes CSVs in outputs/query_results)
python src/run_queries.py
```


## Repo layout
```
data/                         # source CSVs (routes from RMS subset + synthetic demo data)
mappings/                     # human-readable mapping notes
src/                          # Python ETL & SPARQL
  transform.py                # CSV -> RDF (Turtle)
  run_queries.py              # runs queries over the generated TTL
  queries/*.rq                # SPARQL queries
outputs/                      # generated files (ignored by git at first)
```

