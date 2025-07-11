#!/bin/bash

# Abort on error
set -e

echo "✅ Instalando dependencias..."
pip install -r requirements.txt

echo "📦 Aplicando migraciones..."
python manage.py migrate

echo "🎨 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "📥 Importando datos iniciales..."
python manage.py loaddata plazia_seed_data.json

echo "🚀 Iniciando servidor..."
gunicorn plazia_api.wsgi:application --log-file -
