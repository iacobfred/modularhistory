"""
Django settings for history project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# noinspection PyPackageRequirements
from decouple import config
from django.conf.locale.en import formats as en_formats

en_formats.DATETIME_FORMAT = 'Y-m-d H:i:s.u'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# https://docs.djangoproject.com/en/3.0/ref/settings#s-secret-key
SECRET_KEY = config('SECRET_KEY')

# DEBUG must be False in production (for security)
# https://docs.djangoproject.com/en/3.0/ref/settings#s-debug
DEBUG = config('DEBUG', default=True, cast=bool)

# https://docs.djangoproject.com/en/3.0/ref/settings#s-secure-ssl-redirect
SECURE_SSL_REDIRECT = not DEBUG

# https://docs.djangoproject.com/en/3.0/ref/settings#s-session-cookie-samesite
SESSION_COOKIE_SECURE = not DEBUG

# https://docs.djangoproject.com/en/3.0/ref/settings#s-secure-referrer-policy
# https://docs.djangoproject.com/en/3.0/ref/middleware/#referrer-policy
SECURE_REFERRER_POLICY = 'same-origin'

# https://docs.djangoproject.com/en/3.0/ref/settings#s-allowed-hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# https://docs.djangoproject.com/en/3.0/ref/settings#s-internal-ips
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configuring-internal-ips
INTERNAL_IPS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'admin_menu',  # Must come before django.contrib.admin; see https://github.com/cdrx/django-admin-menu
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.staticfiles',
    'django.forms',
    # 'django.contrib.gis',  # https://docs.djangoproject.com/en/3.0/ref/contrib/gis/
    'bootstrap_datepicker_plus',  # https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/
    'crispy_forms',  # https://django-crispy-forms.readthedocs.io/
    'debug_toolbar',  # https://django-debug-toolbar.readthedocs.io/en/latest/
    'django_select2',  # https://django-select2.readthedocs.io/en/latest/index.html
    'decouple',
    # TODO: https://django-file-picker.readthedocs.io/en/latest/index.html
    # 'file_picker',
    # 'file_picker.uploads',  # file and image Django app
    # 'file_picker.wymeditor',  # optional WYMeditor plugin
    # 'sorl.thumbnail',  # required
    'imagekit',  # https://github.com/matthewwithanm/django-imagekit
    'massadmin',  # https://github.com/burke-software/django-mass-edit
    'polymorphic',  # https://django-polymorphic.readthedocs.io/en/stable/
    'rest_framework',  # https://github.com/encode/django-rest-framework
    'sass_processor',  # https://github.com/jrief/django-sass-processor
    'social_django',  # https://python-social-auth.readthedocs.io/en/latest/configuration/django.html
    'tinymce',  # https://django-tinymce.readthedocs.io/en/latest/
    'account.apps.AccountConfig',
    'entities.apps.EntitiesConfig',
    'home.apps.HomeConfig',
    'search.apps.SearchConfig',
    'images.apps.ImagesConfig',
    'occurrences.apps.OccurrencesConfig',
    'places.apps.LocationsConfig',
    'quotes.apps.QuotesConfig',
    'sources.apps.SourcesConfig',
    'topics.apps.TopicsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#enabling-middleware
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'history.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django_settings_export.settings_export',
            ],
            'libraries': {
                # https://stackoverflow.com/questions/41376480/django-template-exceptions-templatesyntaxerror-static-is-not-a-registered-tag
                'staticfiles': 'django.templatetags.static',
            },
        },
    },
]

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

WSGI_APPLICATION = 'history.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        # 'PORT': '5432',
    }
}

AUTH_USER_MODEL = 'account.User'
SOCIAL_AUTH_USER_MODEL = 'account.User'
AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
# SOCIAL_AUTH_PIPELINE = (
#     'social_core.pipeline.social_auth.social_details',
#     'social_core.pipeline.social_auth.social_uid',
#     'social_core.pipeline.social_auth.auth_allowed',
#     'social_core.pipeline.social_auth.social_user',
#     'social_core.pipeline.user.get_username',
#     'social_core.pipeline.social_auth.associate_by_email',  # Enabled (disabled by default)
#     'social_core.pipeline.user.create_user',
#     'social_core.pipeline.social_auth.associate_user',
#     'social_core.pipeline.social_auth.load_extra_data',
#     'social_core.pipeline.user.user_details',
# )
LOGIN_URL = 'account/login'
LOGOUT_URL = 'account/logout'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/account/settings'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_POSTGRES_JSONFIELD = True
# TODO: https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html
# TODO: https://python-social-auth.readthedocs.io/en/latest/configuration/django.html
# SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'last_name', 'email']
# SOCIAL_AUTH_TWITTER_KEY = config('SOCIAL_AUTH_TWITTER_KEY', default='')
# SOCIAL_AUTH_TWITTER_SECRET = config('SOCIAL_AUTH_TWITTER_SECRET', default='')
SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY', default='')
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET', default='')
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'id, name, email', }
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', default='')
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', default='')
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'static')

# Media files (images, etc. uploaded by users)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

X_FRAME_OPTIONS = 'SAMEORIGIN'

# GDAL_LIBRARY_PATH

# https://github.com/jrief/django-sass-processor
SASS_PRECISION = 8

# https://django-tinymce.readthedocs.io/en/latest/usage.html
TINYMCE_JS_URL = 'https://cloud.tinymce.com/stable/tinymce.min.js'
TINYMCE_JS_ROOT = 'https://cloud.tinymce.com/stable/'
TINYMCE_DEFAULT_CONFIG = {
    # 'height': 100,
    'width': '100%',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': (
        'autolink, autoresize, autosave, blockquote, '
        # 'casechange, '  # Premium
        'charmap, code, contextmenu, emoticons, '
        # 'formatpainter, '  # Premium
        'fullscreen, hr, image, link, lists, media, paste, preview, '
        'searchreplace, spellchecker, textcolor, visualblocks, visualchars, wordcount'
    ),
    'toolbar1': (
        'bold italic | blockquote '
        # 'formatpainter | '
        'alignleft aligncenter alignright alignjustify | indent outdent | '
        'bullist numlist | visualblocks visualchars | '
        # 'charmap hr '
        'nonbreaking anchor | image media link | code | highlight | smallcaps | '
        'spellchecker preview | undo redo'
    ),
    'contextmenu': 'formats | highlight | smallcaps | link | media | image | code | pastetext',
    'menubar': True,
    'statusbar': True,
    'branding': False,
    'setup': ('''
        function (editor) {
            editor.addButton('highlight', {
                text: 'Highlight text',
                icon: false,
                onclick : function() {
                    editor.focus();
                    let content = editor.selection.getContent();
                    if (content.length) {
                        content = content.replace("<mark>", "").replace("</mark>", "");
                        editor.selection.setContent("<mark>" + editor.selection.getContent() + '</mark>');
                    }
                }
            });
            editor.addButton('smallcaps', {
                text: 'Small caps',
                icon: false,
                onclick : function() {
                    editor.focus();
                    let content = editor.selection.getContent();
                    if (content.length) {
                        let opening_tag = '<span style="font-variant: small-caps">';
                        let closing_tag = '</span>';
                        content = content.replace(opening_tag, '').replace(closing_tag, '');
                        editor.selection.setContent(opening_tag + editor.selection.getContent() + closing_tag);
                    }
                }
            });
        }
    ''')
}
TINYMCE_SPELLCHECKER = True

# https://pypi.org/project/django-bootstrap-datepicker-plus/
BOOTSTRAP4 = {
    'include_jquery': False,
}

# https://github.com/cdrx/django-admin-menu
ADMIN_LOGO = 'logo_head_white.png'
MENU_WEIGHT = {
    'Entities': 1,
    'Occurrences': 2,
    'Quotes': 3,
    'Sources': 4,
    'Topics': 5,
    'Facts': 6,
    'Images': 7,
    'Places': 8,
    'Accounts': 20
}
ADMIN_STYLE = {
    'primary-color': '#2B3746',
    'secondary-color': '#354151',
    'tertiary-color': '#F2F9FC'
}
# ADMIN_STYLE = {
#     'background': 'white',
#     'primary-color': '#205280',
#     'primary-text': '#d6d5d2',
#     'secondary-color': '#3B75AD',
#     'secondary-text': 'white',
#     'tertiary-color': '#F2F9FC',
#     'tertiary-text': 'black',
#     'breadcrumb-color': 'whitesmoke',
#     'breadcrumb-text': 'black',
#     'focus-color': '#eaeaea',
#     'focus-text': '#666',
#     'primary-button': '#26904A',
#     'primary-button-text':' white',
#     'secondary-button': '#999',
#     'secondary-button-text': 'white',
#     'link-color': '#333',
#     'link-color-hover': 'lighten($link-color, 20%)'
# }

# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html
CRISPY_FAIL_SILENTLY = not DEBUG
CRISPY_CLASS_CONVERTERS = {
    # 'textinput': "textinput inputtext"
}

# https://django-select2.readthedocs.io/en/latest/django_select2.html#module-django_select2.conf
# SELECT2_CSS = ''

MENU_ITEMS = [
    ['Occurrences', 'occurrences'],
    ['People', 'entities'],
    ['Places', 'places'],
    ['Quotes', 'quotes'],
    ['Sources', 'sources'],
    ['Topics', 'topics'],
]

SETTINGS_EXPORT = [
    'MENU_ITEMS',
]

# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'history.settings.show_debug_toolbar'
}


def show_debug_toolbar(request) -> bool:
    if DEBUG and 'showDebugToolbar=true' in request.GET:
        return True
    return False


X_RAPIDAPI_HOST = config('X_RAPIDAPI_HOST')
X_RAPIDAPI_KEY = config('X_RAPIDAPI_KEY')
