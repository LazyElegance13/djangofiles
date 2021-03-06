import os
import sys

from django.conf import settings

#DEBUG = os.environ.get('DEBUG', 'on') == 'on'

#SECRET_KEY = os.environ.get('SECRET_KEY', 'hm!h1#p181jg)pu7_)1f5s+xr21fv88#=m8f@z94p+o80*o#d2')

#ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=True,
    SECRET_KEY='hm!h1#p181jg)pu7_)1f5s+xr21fv88#=m8f@z94p+o80*o#d2',
    #ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=( ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
        'compressor',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        },
    ),
    STATIC_URL = '/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, "pages"),
    SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR,"_build"),
    STATIC_ROOT=os.path.join(BASE_DIR, "_build", "static"),
#    STATICFILES_STORAGE="django.contrib.staticfiles.storage.CachedStaticFilesStorage",
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    ) ,
)


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
