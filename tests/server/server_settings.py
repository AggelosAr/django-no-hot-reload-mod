from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = "test-only-secret-key"
DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
ROOT_URLCONF = "server_urls"
INSTALLED_APPS = [
    "sample_app",
    "django_no_hot_reload_mod.src.code_modifier",
]
MIDDLEWARE = []
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": []},
    }
]
