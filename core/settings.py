from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY
SECRET_KEY = 'django-insecure-%&prp^2$3-#d4-lb@n($e^z4r+at6w-^v!5a56x!&101p(fgeu'
DEBUG = True
ALLOWED_HOSTS = []


# APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'core_app',
    'accounts',
    'blog',
    'projects',
    'experience',
    'likes',
]


# MIDDLEWARE (TO‘G‘RI ORDER)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',  # 🌍 3 til uchun

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',  # 🔥 MUHIM

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URLS
ROOT_URLCONF = 'core.urls'


# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',  # 🔥 SHART
            ],
        },
    },
]


WSGI_APPLICATION = 'core.wsgi.application'


# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# 🌍 INTERNATIONALIZATION
LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('uz', 'Uzbek'),
    ('ru', 'Russian'),
    ('en', 'English'),
]

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True
USE_TZ = True


# STATIC FILES
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'


# MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# DEFAULT PK
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# LOGIN SYSTEM
LOGIN_URL = '/register/'
LOGIN_REDIRECT_URL = '/dashboard/'