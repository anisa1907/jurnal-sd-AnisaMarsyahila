#!/bin/sh

echo "=== Pull image terbaru ==="
docker pull ghcr.io/anisa1907/mvc-app:v2-prod

echo "=== Menghentikan container lama ==="
docker stop app-v1 2>/dev/null
docker rm app-v1 2>/dev/null

echo "=== Menjalankan container baru ==="
docker run -d --name app-v1 -p 8080:5000 ghcr.io/anisa1907/mvc-app:v2-prod

echo "=== Deployment selesai ==="
docker ps