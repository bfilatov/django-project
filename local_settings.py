SECRET_KEY = 'E1OgQWZNiaGXOE5jcKh4UdM8PMLADMTLMfPdnBke8e9eVkHd5u'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'example_project_development',
        'USER': 'example_project_development',
        'PASSWORD': 'rootpass',
        'HOST': 'development.crydfwocg0pu.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

