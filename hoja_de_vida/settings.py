from pathlib import Path
import os
import dj_database_url # [cite: 356]

# Construye rutas dentro del proyecto así: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Seguridad
# En producción, Render proporcionará la SECRET_KEY vía variable de entorno [cite: 315]
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-cambiar-en-produccion")

# DEBUG será False automáticamente al estar en Render [cite: 327, 330]
DEBUG = "RENDER" not in os.environ 

ALLOWED_HOSTS = []
# Captura la dirección que el servidor de la nube otorga [cite: 341, 343]
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
else:
    # Para desarrollo local
    ALLOWED_HOSTS = ["*"]

# 📦 Apps Instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "perfil",
]

# ⚙️ Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # Necesario para archivos estáticos [cite: 374]
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hoja_de_vida.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hoja_de_vida.wsgi.application"

# 🗄️ Base de Datos configurada para PostgreSQL en la nube [cite: 356, 359]
DATABASES = {
    "default": dj_database_url.config(
        # Si no existe DATABASE_URL (local), usa SQLite
        default='postgresql://postgresql_bd_ck9d_user:ZtbFEcfk7sjJtsx2bITZrvd7CZ7TVPty@dpg-d4v41uqli9vc73dghqlg-a/postgresql_bd_ck9d',
        conn_max_age=600,
    )
}

# 🔑 Validadores de Contraseña
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 🌍 Idioma y Zona Horaria
LANGUAGE_CODE = "es-ec"
TIME_ZONE = "America/Guayaquil"
USE_I18N = True
USE_TZ = True

# 📁 Archivos Estáticos (CSS, JS) [cite: 372, 374]
STATIC_URL = "/static/"
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 🖼️ Imágenes (MEDIA)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

X_FRAME_OPTIONS = 'SAMEORIGIN'