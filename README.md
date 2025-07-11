# 📱 Plazia API (Django + DRF + JWT + Swagger)

Esta es la API para la app móvil **Plazia**, desarrollada en Django REST Framework, con autenticación JWT y documentación OpenAPI 3 usando Swagger.

## 🚀 Tecnologías usadas

- Django 4+
- Django REST Framework
- Simple JWT
- drf-spectacular (OpenAPI 3)
- PostgreSQL / SQLite
- Docker y Render para despliegue

---

## 🛠️ Instalación local

```bash
# 1. Clonar el proyecto
$ git clone https://github.com/tu-usuario/plazia-api.git
$ cd plazia-api

# 2. Crear entorno virtual
$ python -m venv venv
$ source venv/bin/activate

# 3. Instalar dependencias
$ pip install -r requirements.txt

# 4. Configurar variables de entorno
$ cp .env.example .env

# 5. Migrar base de datos
$ python manage.py migrate

# 6. Crear superusuario
$ python manage.py createsuperuser

# 7. Ejecutar servidor
$ python manage.py runserver
```

Accede a la documentación en: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

---

## 🐳 Despliegue con Docker

```bash
# Construir imagen
$ docker build -t plazia-api .

# Ejecutar contenedor
$ docker run -p 8000:8000 plazia-api
```

---

## ☁️ Despliegue en Render

1. Sube el repositorio a GitHub.
2. Crea un servicio en https://render.com:
   - Web Service ➝ Python ➝ Conecta con tu repo.
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn plazia_api.wsgi:application --bind 0.0.0.0:8000`
3. Añade las variables del `.env` en Render.
4. En consola, ejecuta:

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## 📚 Endpoints útiles

| Ruta                  | Descripción                         |
| --------------------- | ----------------------------------- |
| `/api/docs/`          | Swagger UI                          |
| `/api/schema/`        | OpenAPI 3 JSON                      |
| `/api/token/`         | Obtener token JWT                   |
| `/api/users/profile/` | Perfil de usuario autenticado       |
| `/api/places/`        | Listar y administrar lugares        |
| `/api/places/top/`    | Listar top lugares por calificación |
| `/api/reviews/`       | Listar y crear reseñas              |
| `/api/favorites/`     | Marcar y consultar favoritos        |

---

## ✅ To Do futuro

- Agregar filtros por categoría, ubicación, tags.
- Integrar soporte de mapas geolocalizados.
- WebSockets para actividad en tiempo real.

---
