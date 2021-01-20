DEBUG = False

ALLOWED_HOSTS = [
    '0.0.0.0',
]

SITE_HOST = 'techmr'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'POSTGRES_DB',
        'USER': 'POSTGRES_USER',
        'PASSWORD': 'POSTGRES_PASSWORD',
        'HOST': 'POSTGRES_HOST',
        'PORT': 'POSTGRES_PORT'
    }
}
