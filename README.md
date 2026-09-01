# Enterprise RAG Platform

A production-oriented Retrieval-Augmented Generation (RAG) platform designed to demonstrate enterprise AI engineering practices: document ingestion, chunking, embeddings, vector retrieval, grounded generation, citations, evaluation, and observability.

## Status

🚧 **Phase 1 — Project foundation**

This repository is being built incrementally as a portfolio project. The goal is to demonstrate production software engineering around GenAI rather than a simple chatbot demo.

## Planned architecture

```text
                         ┌─────────────────┐
                         │   Client / UI   │
                         └────────┬────────┘
                                  │
                           REST / Streaming
                                  │
                         ┌────────▼────────┐
                         │     FastAPI     │
                         │    AI API       │
                         └────────┬────────┘
                                  │
               ┌──────────────────┴──────────────────┐
               │                                     │
        Query pipeline                       Ingestion pipeline
               │                                     │
        Query transformation                    Parsers
               │                                  Chunking
          Retrieval                              Embeddings
               │                                     │
          Reranking                              pgvector
               │
          LLM generation
               │
        Answer + citations
```

## Technology direction

- Python
- FastAPI
- LangChain / LangGraph
- PostgreSQL + pgvector
- Ollama for local development
- Configurable LLM and embedding providers
- Redis for application-level caching/state where appropriate
- Docker Compose
- Pytest
- GitHub Actions
- Prometheus-compatible metrics

## Engineering goals

- Ground answers in retrieved source material
- Return source citations with generated answers
- Keep model providers configurable
- Separate ingestion, retrieval, generation, and evaluation concerns
- Provide deterministic tests around the non-LLM portions of the system
- Measure retrieval and generation quality rather than relying on subjective testing
- Track latency, token usage, errors, and other operational signals
- Make the entire stack runnable locally with Docker

## Roadmap

- [x] Repository created
- [x] Initial architecture documented
- [ ] FastAPI application skeleton
- [ ] PostgreSQL + pgvector development environment
- [ ] Configuration and health endpoints
- [ ] Document ingestion API
- [ ] Document parsing and chunking
- [ ] Embedding pipeline
- [ ] Semantic retrieval
- [ ] Hybrid retrieval and metadata filtering
- [ ] Reranking
- [ ] Grounded answer generation
- [ ] Source citations
- [ ] Conversation support
- [ ] RAG evaluation dataset and metrics
- [ ] Observability and cost/latency tracking
- [ ] Integration tests with Testcontainers
- [ ] CI/CD

## Why this project exists

The project is intentionally designed around the problems encountered when taking RAG beyond a proof of concept: retrieval quality, grounding, evaluation, operational visibility, provider abstraction, testing, and reproducible local development.

## License

MIT
