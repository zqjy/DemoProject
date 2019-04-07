"""
Django settings for Demo project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%jdh297n^c1w2mgh%2*p253!h$-g9zc0@c##!9k0+=9x-)o9ar'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # 跨域问题
    'DjangoUeditor',  # 富文本编辑器
    'crispy_forms',  # xadmin
    'xadmin',  # xadmin
    'django_filters',  # 过滤器
    'rest_framework',  # rest framework
    'rest_framework.authtoken',  # 用户权限 添加后需要makemigretins migrate 生成一张token表
    'upload.apps.UploadConfig',
    'users.apps.UsersConfig',
    'rest.apps.RestConfig',
    'trade.apps.TradeConfig',
    'user_operation.apps.UserOperationConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 跨域问题中间件配置  尽量放在csrf之前
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # 防止跨站攻击 前后端分离无需考虑  因为已经跨域
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True  # 跨域问题配置
ROOT_URLCONF = 'Demo.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'Demo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_demo',
        'HOST': '192.168.31.199',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root',
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB;'},
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 设置访问静态文件对应的url地址
STATIC_URL = '/static/'

# 设置静态文件存放的物理目录
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 设置上传文件的保存目录
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 修改django用户类
AUTH_USER_MODEL = 'users.UserProfile'

REST_FRAMEWORK = {
    # 分页  当前被自定义替代
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
    # 过滤器
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'ORDERING_PARAM': 'order',  # 排序参数名称
    'SEARCH_PARAM': 's',  # 搜索参数名称
    'DEFAULT_AUTHENTICATION_CLASSES': (  # 用户权限配置
        'rest_framework.authentication.BasicAuthentication',  # 浏览器调试使用
        'rest_framework.authentication.SessionAuthentication',  # 浏览器调试使用
        # 'rest_framework.authentication.TokenAuthentication',  # 前后端分离使用 全局token验证  不合理  被局部验证替代
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # JWT用户认证
    ),
}

import datetime

# JWT 配置
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),  # 过期时间
    'JWT_AUTH_HEADER_PREFIX': 'JWT',  # 认证方式
}

# 自定义用户认证函数
AUTHENTICATION_BACKENDS = (
    'apps.users.views.CustomBackend',
)

# 手机号码正则表达式
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"

#云片网设置
APIKEY = "b0402994353b2fc629ac4ef6501d079f"
