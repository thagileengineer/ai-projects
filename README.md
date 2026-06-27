# Agentic AI Projects Monorepo

This repository is structured as a Python monorepo managed with `uv` workspaces for development of Agentic AI Capstone projects.

## Project Structure

```
ai-projects/
├── pyproject.toml              # Root workspace configuration
├── uv.lock                     # Auto-generated lockfile for all packages
├── rag-application/            # App: Document Q&A Copilot
│   ├── pyproject.toml          # App configuration & dependencies
│   └── src/                    # Source code (RAG logic)
└── packages/
    └── shared-core/            # Shared Library: Reusable core modules
        ├── pyproject.toml      # Package dependencies
        └── src/
            └── shared_core/    # Exported packages
```

---

## Workspace Setup

### Prerequisites
Make sure you have [uv](https://github.com/astral-sh/uv) installed on your system.

### Sync Dependencies
To initialize the unified virtual environment and link all packages in editable mode, run the following command from the repository root:
```bash
uv sync
```
This automatically sets up a shared `.venv` at the root and configures cross-project dependencies so that modifications in any shared package are immediately reflected inside the applications.

---

## Agentic AI Capstone Projects

1. **Document Q&A Copilot** (`rag-application`)
   A RAG-powered Copilot that answers questions from corporate PDFs with evaluated accuracy.

2. **Enterprise Intelligence Dashboard**
   Hybrid search + live SQL queries + knowledge graph, orchestrated by a DSPy reasoning engine.

3. **Autonomous Support Agent Swarm**
   Multi-agent system with persistent memory, live API integration, and human approval gates.

4. **Production AI Infrastructure Stack**
   Cost-optimized, observable inference layer with model routing, semantic caching, and failover.

5. **Mega Capstone — Enterprise Platform**
   Fully containerized, multi-tenant, RBAC-secured AI platform — load-tested under real concurrent traffic.

---

## Development Cheat Sheet

### Run an Application Tool/Script
Run scripts inside the virtual environment using `uv run`:
```bash
# Run RAG ingestion
uv run --project rag-application python rag-application/src/ingest.py

# Run RAG query
uv run --project rag-application python rag-application/src/main.py
```

### Adding New Shared Packages
1. Create a directory under `packages/` (e.g. `packages/my-utility`).
2. Add a `pyproject.toml` and your package source.
3. Reference the workspace package in your application's `pyproject.toml`:
   ```toml
   [project]
   dependencies = [
       "my-utility"
   ]

   [tool.uv.sources]
   my-utility = { workspace = true }
   ```
4. Run `uv sync` at the root workspace.
