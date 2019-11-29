import os

from configurations import Configuration, values
from datetime import timedelta
print(os.environ)


class Base(Configuration):

    DEBUG = values.BooleanValue(False)
    SECRET_KEY = values.SecretValue()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DATABASES = values.DatabaseURLValue()

    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "rest_framework",
        "rest_framework.authtoken",
        "corsheaders",
        "djoser",
        'django_celery_beat',
        'django_celery_results',
        "accounts",
        "apimb",
        "apism",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "autobets.urls"

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
                ]
            },
        }
    ]

    # WSGI

    WSGI_APPLICATION = "autobets.wsgi.application"

    # Password validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
        },
    ]

    AUTH_USER_MODEL = "accounts.User"

    # Internationalization

    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "UTC"
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Static files

    STATIC_URL = "/static/"

    # REST

    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework.authentication.BasicAuthentication",
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.TokenAuthentication",
        ),
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 100,
    }



# celery

CELERY_BROKER_URL = 'pyamqp://rabbitmq:5672'
CELERY_RESULT_BACKEND = 'django-db'
#CELERY_BROKER_URL = 'pyamqp://rabbitmq:5672'

#CELERY_BROKER_URL = 'redis://localhost:6379'
#CELERY_RESULT_BACKEND = 'redis://localhost:6379/'
CELERYD_HIJACK_ROOT_LOGGER = False
# use json format for everything
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
#CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


CELERY_BEAT_SCHEDULE = {

    'get_events': {
    'task': 'apimb.tasks.get_events' ,
    'schedule': timedelta(seconds=10) ,
    'args': ()
    } ,
    'get_orders': {
    'task': 'apimb.tasks.get_orders' ,
    'schedule': timedelta(seconds=10) ,
    'args': ()
    } ,

    'get_balance': {
    'task': 'apimb.tasks.get_balance' ,
    'schedule': timedelta(seconds=10) ,
    'args': ()
    } ,
    
    'get_reports': {
    'task': 'apimb.tasks.get_reports' ,
    'schedule': timedelta(seconds=10) ,
    'args': ()
    } ,
} 



class Development(Base):
    DEBUG = values.BooleanValue(True)
    CORS_ORIGIN_ALLOW_ALL = True
    ALLOWED_HOSTS = ["localhost", "django"]


class Production(Base):
    pass


class Testing(Base):
    pass
