# ===========================
# STAGE 1 : Builder
# ===========================
FROM python:3.9-slim AS builder

WORKDIR /app

# Salin seluruh project
COPY . .

# ===========================
# STAGE 2 : Production
# ===========================
FROM python:3.9-alpine

WORKDIR /app

# Salin hasil dari stage builder
COPY --from=builder /app /app

CMD ["python", "app.py"]