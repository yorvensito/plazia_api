#!/bin/bash

# Abort on error
set -e

# 1. Crear directorio staticfiles con permisos adecuados
echo "🛠 Creando directorio staticfiles si no existe..."
mkdir -p /opt/render/project/src/staticfiles
chmod -R 755 /opt/render/project/src/staticfiles

echo "✅ Instalando dependencias..."
pip install -r requirements.txt

echo "📦 Aplicando migraciones..."
python manage.py migrate



echo "🎨 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput || {
    echo "⚠️ Advertencia: Problema al recolectar archivos estáticos (pero continuando)..."
    # Crea archivos mínimos para evitar errores
    touch /opt/render/project/src/staticfiles/.keep
    touch /opt/render/project/src/staticfiles/placeholder.txt
}


# echo "📥 Importando datos iniciales..."
# python manage.py loaddata plazia_seed_data.json

echo "🚀 Iniciando servidor..."
gunicorn plazia_api.wsgi:application --log-file -
