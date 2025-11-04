# 💊 IDMP Mini Lab — CSV → RDF → SPARQL Pipeline

[![CI](https://github.com/Mohsen-safi-Najafabadi/idmp-mini-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/Mohsen-safi-Najafabadi/idmp-mini-lab/actions)


A compact demo project that transforms structured CSV data into RDF triples and runs SPARQL queries to extract useful insights.  
This project mimics a simplified **IDMP (Identification of Medicinal Products)** data pipeline as used in EMA’s RMS/OMS framework.

---

## 📂 Project Overview

### 🔹 Source Data
The input data consists of simplified CSVs based on EMA’s *Referentials Management Service (RMS)* structure, including:

| File | Description |
|------|--------------|
| `data/products.csv` | List of medicinal products with basic metadata |
| `data/substances.csv` | Active substances and identifiers |
| `data/routes_of_administration.csv` | Administration routes |
| `data/organizations.csv` | Organization master data |
| `mappings/products_mapping.yaml` | Defines how CSV columns are mapped to RDF predicates |

---

## 🔧 Pipeline Steps

### 1️⃣ Transform CSV → RDF
Using `src/transform.py`, the CSV files are converted into RDF triples (Turtle format).

```bash
python src/transform.py
<<<<<<< HEAD
=======

---

## Provenance & License

* The data sources are explained in **[PROVENANCE.md](PROVENANCE.md)** (EMA SPOR RMS + synthetic data).
* Usage license: **MIT** — see **[LICENSE](LICENSE)**.
>>>>>>> 971ba29 (docs: add PROVENANCE and MIT LICENSE; link from README)
