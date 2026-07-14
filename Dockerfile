# =============================================================================
# Stage: Production image
# Base: python:3.11-slim  — Debian-based, minimal footprint (~50MB base).
# We do NOT use alpine because HuggingFace / FAISS need glibc, not musl.
# =============================================================================
FROM python:3.11-slim

# ---------------------------------------------------------------------------
# 1. OS-level metadata & build-time labels (for registry traceability)
# ---------------------------------------------------------------------------
LABEL maintainer="AI Email Generator Copilot"
LABEL description="Streamlit + LangChain + Gemini + FAISS RAG email generator"
LABEL python.version="3.11"

# ---------------------------------------------------------------------------
# 2. System dependencies
#    - gcc / g++ / build-essential: needed by some Python wheels (e.g. faiss-cpu)
#    - curl: used by the health-check below
#    We clean apt cache in the SAME layer to keep image size down.
# ---------------------------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        build-essential \
        curl \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------------------------
# 3. Create a non-root user for security best practices.
#    Running as root inside a container is a security risk.
# ---------------------------------------------------------------------------
RUN useradd --create-home --shell /bin/bash appuser

# ---------------------------------------------------------------------------
# 4. Set the working directory inside the container.
# ---------------------------------------------------------------------------
WORKDIR /app

# ---------------------------------------------------------------------------
# 5. Install Python dependencies BEFORE copying source code.
#    Docker caches layers. By copying requirements.txt first and running pip,
#    we only re-run pip install when requirements.txt actually changes —
#    not on every source code edit. This dramatically speeds up rebuilds.
# ---------------------------------------------------------------------------
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---------------------------------------------------------------------------
# 6. Copy application source files into the container.
#    We copy explicitly (not COPY . .) so that:
#    - .env is NEVER accidentally included (secrets must NOT be baked in)
#    - .git/, __pycache__/ and dev artifacts are excluded
#
#    Files copied:
#      streamlit_app.py  — Streamlit UI (primary entry point)
#      api.py            — FastAPI backend (kept for completeness)
#      app.py            — CLI entry point (kept for completeness)
#      rag/              — RAG retriever + vectorstore builder
#      prompts/          — Email prompt templates
#      faiss_index/      — Pre-built FAISS index (index.faiss + index.pkl)
#      Email_Templates_idea/ — Raw .txt template files used to build the index
#      .streamlit/       — Streamlit server config (headless, port, address)
# ---------------------------------------------------------------------------
COPY streamlit_app.py  ./streamlit_app.py
COPY api.py            ./api.py
COPY app.py            ./app.py
COPY rag/              ./rag/
COPY prompts/          ./prompts/
COPY faiss_index/      ./faiss_index/
COPY Email_Templates_idea/ ./Email_Templates_idea/
COPY .streamlit/       ./.streamlit/

# ---------------------------------------------------------------------------
# 7. Transfer ownership of all app files to the non-root user.
# ---------------------------------------------------------------------------
RUN chown -R appuser:appuser /app

# ---------------------------------------------------------------------------
# 8. Switch to the non-root user for all subsequent commands.
# ---------------------------------------------------------------------------
USER appuser

# ---------------------------------------------------------------------------
# 9. Expose port 8501 — the Streamlit default port.
#    AWS App Runner will route HTTPS traffic to this port.
#    docker run -p 8501:8501 maps this port to your host machine.
# ---------------------------------------------------------------------------
EXPOSE 8501

# ---------------------------------------------------------------------------
# 10. Health check — AWS App Runner and orchestrators use this to verify
#     the container is alive before routing traffic to it.
#     We poll the Streamlit health endpoint every 30 seconds.
# ---------------------------------------------------------------------------
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# ---------------------------------------------------------------------------
# 11. Container entry point.
#     We use the exec form (JSON array) — NOT shell form — so that
#     Streamlit receives Unix signals (SIGTERM) correctly for graceful shutdown.
#
#     --server.headless=true      — no browser, no welcome screen
#     --server.address=0.0.0.0   — listen on all interfaces (required in Docker)
#     --server.port=8501          — explicit port
#     --server.enableCORS=false   — App Runner handles TLS/routing
# ---------------------------------------------------------------------------
CMD ["streamlit", "run", "streamlit_app.py", \
     "--server.headless=true", \
     "--server.address=0.0.0.0", \
     "--server.port=8501", \
     "--server.enableCORS=false"]
