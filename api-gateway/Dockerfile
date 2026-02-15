# Estágio 1: Builder
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Estágio 2: Final
FROM python:3.9-slim
WORKDIR /app

# --- CORREÇÃO: Instala curl para o Healthcheck funcionar ---
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
# -----------------------------------------------------------

COPY --from=builder /install /usr/local
COPY . .

# Segurança: Usuário não-root
RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]
