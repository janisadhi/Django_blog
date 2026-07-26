"""
Django settings for mysite project.

Django 6.x settings.
"""

import os
from pathlib import Path


# =============================================================================
# BASE DIRECTORY
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =============================================================================
# SECURITY
# =============================================================================

# Use an environment variable in Docker.
# The fallback is only for local development.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-change-this-in-production",
)

# Convert environment variable string to boolean.
DEBUG = os.environ.get("DJANGO_DEBUG", "True").lower() in (
    "true",
    "1",
    "yes",
)


# Hosts allowed to access the Django application.
#
# For local/Docker development:
#   localhost
#   127.0.0.1
#
# You can add your server IP or domain later.
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
]


# =============================================================================
# APPLICATIONS
# =============================================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",

    # Third-party apps
    "debug_toolbar",
    "crispy_forms",
    "django_summernote",

    # Local apps
    "blog",
]


# =============================================================================
# MIDDLEWARE
# =============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise serves collected static files through Django/Gunicorn.
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "debug_toolbar.middleware.DebugToolbarMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =============================================================================
# URL / WSGI CONFIGURATION
# =============================================================================

ROOT_URLCONF = "mysite.urls"

WSGI_APPLICATION = "mysite.wsgi.application"


# =============================================================================
# DEBUG TOOLBAR
# =============================================================================

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]


# =============================================================================
# TEMPLATES
# =============================================================================

TEMPLATES_DIR = BASE_DIR / "templates"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            TEMPLATES_DIR,
        ],
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


# =============================================================================
# DATABASE
# =============================================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# =============================================================================
# PASSWORD VALIDATION
# =============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# =============================================================================
# INTERNATIONALIZATION
# =============================================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# =============================================================================
# STATIC FILES
# =============================================================================

# URL used by browsers to request static files.
#
# Example:
#   http://127.0.0.1:8000/static/css/style.css
#
# Do NOT use /app/static/ here.
STATIC_URL = "/static/"


# Directory where Django looks for additional static files
# in your project.
#
# Example:
#   /app/static/css/style.css
#
# This is the SOURCE directory.
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# Directory where "collectstatic" puts all collected static files.
#
# In Docker, this will normally be:
#   /app/staticfiles
#
# This is the DEPLOYMENT directory.
STATIC_ROOT = BASE_DIR / "staticfiles"


# WhiteNoise storage.
#
# This enables compressed static files and cache-friendly filenames.
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage.CompressedManifestStaticFilesStorage"
        ),
    },
}


# =============================================================================
# MEDIA FILES
# =============================================================================

# User-uploaded files.
#
# Browser URL:
#   http://127.0.0.1:8000/media/...
MEDIA_URL = "/media/"

# Physical location inside Docker:
#   /app/media/
MEDIA_ROOT = BASE_DIR / "media"


# =============================================================================
# CRISPY FORMS
# =============================================================================

CRISPY_TEMPLATE_PACK = "bootstrap4"


# =============================================================================
# OTHER SETTINGS
# =============================================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

X_FRAME_OPTIONS = "SAMEORIGIN"