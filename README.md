# 🍍 AULCE

**Adaptive Universal Lossless Compression Engine (AULCE)** is a research-grade, open-source **lossless universal compression system** inspired by the *ideas* behind the fictional Pied Piper in HBO’s *Silicon Valley* — but built **entirely in the open**, using modular pipelines, ML-based strategy selection, and explainable RAG reasoning.

It is designed to be **universal, infra-aware, ML-driven, and explainable**, not just another ZIP replacement.

> This is not a fictional magic compressor. It is a full, end-to-end system with multi-stage compression pipelines, ML strategy selection, RAG explanations, evaluation, and live benchmarks.

---

## 🚀 Why AULCE Exists

There is **no open-source Pied Piper-like system**:

* No public repo for universal, adaptive, lossless compression
* No ML-assisted strategy selection for all file types
* No explainable system showing *why compression succeeds or fails*

**AULCE fills that gap** with:

* ML-based strategy selector for heterogeneous file types
* Multi-stage hybrid compression pipelines
* Retrieval-Augmented Generation (RAG) to explain failures
* Tool-aware reasoning to prevent hallucination
* Transparent evaluation & benchmarking

All built in a **reproducible, research-grade way**.

---

## 🧠 Core Design Goals

* 🧩 **Universal** – supports any file extension
* ⚡ **Fast & adaptive** – selects pipelines per file type
* 🔍 **Explainable** – RAG explains compression outcomes
* 🎯 **Benchmark-first** – compares against ZIP, TAR, 7z, Zstd
* 🛠️ **Tool-aware** – integrates analysis, logs, file context
* 🔓 **Fully open** – MIT/Apache 2.0 license

---

## 📐 System Overview

PiedPiperX treats compression as a **decision problem**, not a single algorithm.

| Stage                | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| Ingestion            | Reads files, extracts metadata                              |
| Feature Extraction   | Entropy, size, symbol distribution, MIME type               |
| ML Strategy Selector | Predicts best compression pipeline                          |
| Pipeline Engine      | Applies hybrid compression strategy                         |
| Validator            | Ensures lossless round-trip                                 |
| Explainer (RAG)      | Generates human-readable explanation when compression fails |
| Benchmarking         | Evaluates against ZIP / 7z / Zstd                           |

---

## 📊 ML Model Overview

The ML model **does not compress data directly**, but predicts:

* Optimal pipeline for a file
* Expected compression ratio
* Execution time & memory
* Likelihood of improvement vs baseline

| Attribute  | Value                                                         |
| ---------- | ------------------------------------------------------------- |
| Model type | Random Forest / PyTorch hybrid                                |
| Inputs     | Entropy, file size, MIME, symbol frequency, prior compression |
| Outputs    | Pipeline selection, expected ratio, confidence                |
| Library    | scikit-learn, PyTorch                                         |
| License    | MIT / Apache 2.0                                              |

---

## 🔍 Retrieval-Augmented Generation (RAG)

RAG explains **why compression failed** using:

* Embedded documentation
* Historical file comparisons
* Entropy & codec theory

RAG ensures **anti-hallucination reasoning**:

* Only cites retrieved documents
* References prior benchmarks
* Provides actionable explanations

---

## 🏗️ Tech Stack

| Layer             | Choice                            |
| ----------------- | --------------------------------- |
| Backend           | FastAPI, Python 3.11              |
| ML                | scikit-learn, PyTorch             |
| Compression       | Zstd, Brotli, LZMA, custom codecs |
| Embeddings        | OpenAI / Hugging Face embeddings  |
| RAG               | LangChain + FAISS / Chroma        |
| Frontend UI       | React + Tailwind                  |
| PDF/Image Parsing | PyMuPDF, Pillow                   |
| Evaluation        | Benchmark & hallucination metrics |
| Deployment        | Docker, Docker Compose, AWS EC2   |

---

## 🧱 Repository Structure

```text
PiedPiperX/
├── README.md
├── LICENSE
├── backend/
│   ├── api.py
│   ├── analyzer/
│   ├── compressors/
│   ├── selector/
│   ├── validator/
│   └── explainer/
├── ml/
│   ├── training/
│   ├── feature_engineering/
│   └── models/
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│   └── explainer.py
├── benchmarks/
│   ├── datasets/
│   ├── runner.py
│   └── plot.py
├── frontend/
│   ├── src/
│   └── public/
├── scripts/
│   ├── run_benchmarks.py
│   └── prepare_data.py
└── docker-compose.yml
```

---

## 🧱 ASCII Architecture Diagram

```text
                     ┌─────────────────────┐
                     │   User / Client     │
                     │ (CLI, Web UI, API)  │
                     └─────────┬───────────┘
                               │
                               ▼
                     ┌─────────────────────┐
                     │    FastAPI Backend  │
                     └─────────┬───────────┘
                               │
           ┌───────────────────┼───────────────────┐
           │                   │                   │
           ▼                   ▼                   ▼
     ┌────────────┐      ┌───────────────┐   ┌────────────┐
     │   Analyzer │      │   ML Selector │   │  Pipeline  │
     └─────┬──────┘      └──────┬────────┘   └─────┬──────┘
           │                    │                  │
           ▼                    ▼                  ▼
     ┌────────────┐      ┌───────────────┐   ┌────────────┐
     │ Validator  │      │ RAG Explainer │   │ Benchmark  │
     └────────────┘      └───────────────┘   └────────────┘
```

---

## 🧪 Training Pipeline

1. Collect diverse file corpus (PDF, images, audio, binaries, text)
2. Extract features (entropy, MIME type, symbol frequency)
3. Execute all pipelines → record compression ratios
4. Train ML strategy selector (Random Forest / PyTorch)
5. Validate on unseen file families
6. Persist model + feature schema

---

## 🛠️ Tool-Aware Reasoning

* Checks system context (logs, OS, APIs)
* Requests missing information instead of guessing
* Grounded answers for explainability

---

## 📊 Evaluation & Hallucination Metrics

* Compression ratio vs baseline (ZIP, 7z, Zstd)
* Execution time & memory
* ML strategy regret
* RAG faithfulness / hallucination score

Run batch evaluation:

```bash
python benchmarks/runner.py
```

Visualize:

```bash
python benchmarks/plot.py
```

---

## 🌐 Quick Start (Docker)

```bash
docker build -t piedpiperx .
docker run -p 8000:8000 piedpiperx
```

Visit: `http://localhost:8000`

---

## ⚖️ License

MIT 

---

## ⚠️ Disclaimer

* Inspired by fiction, implemented in reality
* No magic compression claims
* Fully transparent and reproducible

---
