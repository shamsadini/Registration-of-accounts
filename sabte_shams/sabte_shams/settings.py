# sabte_shams/settings.py

import os
from pathlib import Path

# مسیر پایه پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# امنیت کلید رمزنگاری
SECRET_KEY = 'تغییر_این_کلید_با_یک_کلید_امن_دیگر'

# حالت DEBUG
DEBUG = True

# لیست میزبان‌های مجاز
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# اپلیکیشن‌های نصب شده
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jalali',  # برای تاریخ شمسی
    'accounting',  # اپلیکیشن حسابداری شما
    'rest_framework',
]

# میدلورهای پروژه
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # برای پشتیبانی از زبان‌های مختلف
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# روت‌های URL
ROOT_URLCONF = 'sabte_shams.urls'

# تنظیمات قالب‌ها
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

# تنظیمات WSGI
WSGI_APPLICATION = 'sabte_shams.wsgi.application'

# تنظیمات پایگاه داده
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# زمان و زبان
LANGUAGE_CODE = 'fa'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# مسیر استاتیک فایل‌ها
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# مسیر فایل‌های رسانه‌ای (برای آپلود فایل‌ها)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# مسیر فایل‌های استاتیک (برای فایل‌های جمع‌آوری شده)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# تنظیمات امنیتی
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
X_FRAME_OPTIONS = 'DENY'

# تنظیمات پشتیبان
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')

# تنظیمات مدیریتی
ADMINS = [('Admin', 'admin@example.com')]

# پیکربندی‌های اضافی (در صورت نیاز)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
