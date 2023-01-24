app = application

ALLOWED_HOSTS = ['.vercel.app', '.now.sh']

STATICFILES_DIRS = os.path.join(BASE_DIR,'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
