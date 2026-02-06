# AULCE 🚀

> **A research‑grade, open‑source, lossless universal compression system inspired by (but not copying) the HBO *Silicon Valley* concept.**

AULCE is **not magic** and **not a single algorithm**. It is a *system*: a multi‑pipeline, ML‑assisted compression framework that **selects, composes, and validates optimal lossless strategies per file type**, with explainability via RAG and strong benchmarking discipline.

---

## Introduction

Classic compressors (ZIP, TAR.GZ, 7z, Zstd) apply *general heuristics*. Real‑world data is heterogeneous: PDFs, logs, CSVs, images, binaries, audio, and already‑compressed blobs behave very differently.

**AULCE** treats compression as a *decision problem*:

> *Given a file (or corpus), which lossless strategy—or chain of strategies—minimizes size while guaranteeing reversibility?*

Instead of promising impossible ratios, we focus on:

* smarter selection
* hybrid pipelines
* empirical guarantees
* transparent failure explanations

---

## Available Today vs What’s New

### Existing Tools

| Tool   | Strength   | Limitation    |
| ------ | ---------- | ------------- |
| ZIP    | Ubiquitous | Weak ratios   |
| TAR.GZ | Simple     | No adaptivity |
| 7z     | Strong     | Slow, opaque  |
| Zstd   | Fast       | Not universal |

---

## Core Design Goals

1. **Strictly lossless** (bit‑perfect round‑trip)
2. **Universal** (any file extension)
3. **Composable** (pipelines, not monoliths)
4. **Explainable** (why compression succeeded or failed)
5. **Benchmark‑driven** (no marketing ratios)
6. **Open & inspectable** (no black boxes)

---

## Model Overview (ML Strategy Selector)

The ML model does **not** compress data directly.

It predicts:

* which *pipeline* to apply
* expected compression ratio
* expected time/memory cost
* probability of improvement vs baseline

### Input Features

* Byte entropy
* N‑gram redundancy
* File magic + MIME
* Size distribution
* Symbol frequency skew
* Prior compression signals

### Output

```json
{
  "pipeline": "pdf → object‑stream → zstd",
  "expected_ratio": 2.14,
  "confidence": 0.82
}
```

---

## System Overview

AULCE is a **modular system**, not a single binary.

```text
              Upload
                │
                ▼
             Analyzer
                │
                ▼
            ML Selector
                │
                ▼
          Pipeline Engine
                │
                ▼
            Validator
                │
                ▼
            Explainer
```

---

## Tech Stack

| Tool                    | Choice                                  |
| ----------------------- | --------------------------------------- |
| Core                    Python 3.11, Rust (high‑perf codecs)      |
| Compression             zstd, brotli, lzma, custom entropy coders |
| ML                      PyTorch, scikit‑learn                     |
| RAG / Explainability    LangChain, Chroma, OpenAI‑compatible LLM  |
| Web UI                  FastAPI, React + Tailwind                 |
  
---

## Repository Structure

```text
piedpiperx/
├── backend/
│   ├── api/
│   ├── analyzer/
│   ├── selector/
│   ├── pipelines/
│   ├── validator/
│   └── explainer/
├── ml/
│   ├── datasets/
│   ├── feature_engineering/
│   ├── training/
│   ├── evaluation/
│   └── models/
├── rag/
│   ├── documents/
│   ├── index/
│   └── chains/
├── benchmarks/
│   ├── datasets/
│   ├── runners/
│   └── graphs/
├── frontend/
│   ├── src/
│   └── public/
├── scripts/
├── docs/
└── README.md
```

---

## ASCII Architecture Diagram

```text
                             ┌────────────┐
                             │   Web UI   │
                             └─────┬──────┘
                                   │
                             ┌─────▼──────┐
                             │  FastAPI   │
                             └─────┬──────┘
                                   │
                      ┌────────────▼────────────┐
                      │      File Analyzer      │
                      └────────────┬────────────┘
                                   │
                         ┌─────────▼─────────┐
                         │ ML Strategy Model │
                         └─────────┬─────────┘
                                   │
                         ┌─────────▼─────────┐
                         │  Pipeline Engine  │
                         └─────────┬─────────┘
                                   │
                      ┌────────────▼────────────┐
                      │    Lossless Validator   │
                      └────────────┬────────────┘
                                   │
                         ┌─────────▼─────────┐
                         │   RAG Explainer   │
                         └───────────────────┘
```

---

## ML Training Pipeline

1. Collect heterogeneous corpus
2. Extract statistical + structural features
3. Run all pipelines → ground truth ratios
4. Train multi‑label classifier + regressor
5. Validate on unseen file families
6. Persist model + feature schema

---

## RAG: Explaining Compression Failures

When compression underperforms:

> *"Why didn’t this file compress?"*

The system retrieves:

* entropy theory
* similar historical files
* codec limitations

Then generates grounded explanations via LangChain.

---

## Tool‑Aware Reasoning (Anti‑Hallucination)

The explainer **cannot invent reasons**.

Rules:

* Every claim must cite retrieved docs
* Metrics are computed, not guessed
* Pipelines are executed before explanation

---

## Evaluation & Hallucination Metrics

**Compression Metrics**

* Ratio
* Time
* Memory

**ML Metrics**

* Top‑1 accuracy
* Regret vs oracle

**RAG Metrics**

* Citation coverage
* Faithfulness score
* Contradiction rate

---

## Benchmarks

We benchmark against:

* ZIP
* TAR.GZ
* 7z
* Zstd

Graphs are auto‑generated and versioned.

---

## Legal & Ethics

This project is:

* Inspired by fiction
* Implements real, known techniques
* Makes no impossible claims

---

## Roadmap

* GPU‑assisted entropy analysis
* Streaming compression
* Distributed benchmarks
* Academic paper submission

---

## License

Apache‑2.0

---

## Final Note

**AULCE is a flagship portfolio project** meant to demonstrate:

* systems thinking
* ML + infra maturity
* scientific honesty

If it ever beats ZIP by 10× on *your* data—great.
If it doesn’t—we’ll explain *why*.
