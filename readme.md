# Setting up Django Rest Framework

- Create new directory and open in Visual Studio Code.
- Create virtual environment.

  > python -m venv venv

- Activate the environment.

  > . venv/Scripts/Activate

- Check if you succesfully entered the virtual environment.
  > pip list
- Create a new file with name 'requirements.txt' and write down the name of python packages that you require for your projects.

  > - django
  > - django
  > - djangorestframework
  > - django-cors-headers
  > - django-jazzmin
  > - pillow
  > - psycopg2
  > - djangorestframework-simplejwt
  > - drf-spectacular

- Not all packages mentioned above are essential for Django Rest Framework, but I prefer to have them. We may have to install other packages along the way.
- Install packages from requirements.txt file

  > pip install -r requirements.txt

- After completing the installation, start new django project.
  > django-admin start project blog .
- This will create a new folder named blog in your current directory. The dot(.) at the end is needed to create the project folder in current directory. Otherwise it will create blog folder inside another blog folder.
- In the blog folder there will be some python files but most of the times we will work with settings.py and urls.py

## In settings.py

- In settings.py we will make some addition and changes.

- If you dont want to change you database you dont have to change anything in DATABASES part and leave as it is.
- If you want to change your database to postgress you need to create new database in postgress pgadmin application.
- Suppose you created a new database with name 'blog_api'.

- Now to change the database replace existing database dictionary with the following

```py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "blog_api", #Your database name
        "USER": "postgres", #Your postgress username
        "PASSWORD": "gopal", # Your postgress password
        "HOST": "localhost", #Your hostname
        "PORT": "5432", #Your port
    }
}
```
- For mySQL

```py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "e_learning",
        "USER": "root",
        "PASSWORD": "user",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

- This will change your database from dbSqlite to Postgress.

- In settings.py you need to import timedelta.

```py
from datetime import timedelta
```

- In INSTALLED_APPS, you need to write the apps that you have installed as follows:

```py
INSTALLED_APPS = [
    #apps that I installed
    "api",
    "jazzmin",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    #apps that were already here
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

- In setting.py you need to include the following code blocks as well

```py
# This code configures Django REST framework with the menthioned settings

REST_FRAMEWORK = {
"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    	"DEFAULT_AUTHENTICATION_CLASSES": (
"rest_framework_simplejwt.authentication.JWTAuthentication",
),
}
```

```py
# This code is to configure JSON Web Tokens that we need for authentication and authorization.

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
```

```py
# This code is for swagger UI documentation. When you visit 'your_endpoint/api', everything will look properly styled and beautiful.You will be able to see all of your endpoints at one place. You will also be able to request on particular endpoint and get response via swagger UI and you won't need additional apps like Postman.

SPECTACULAR_SETTINGS = {
    "TITLE": "<name_of_your_api>",
    "DESCRIPTION": "<description>",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

```

- In MIDDLEWARE, include CorsMiddleware.

```py
MIDDLEWARE = [
    # Newly Added Middlewares
    "corsheaders.middleware.CorsMiddleware",
    # Existing MIddlewares
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

```

- In the bottom where there is static_url, you need to add media url and media root. This allows you to store user uploaded images and files and also allows you to serve them to user.

````py
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")```
````

- This is all for now in settings.py

- Now let's create a new api for blog.
- In terminal, make sure youre inside virtual environment throughout the process.
- Start new app named 'api'

  > py manage.py startapp api

- This will create a new folder named api with some python files inside it.

- Create a new file inside api folder with name: urls.py

- Do not forget to add this 'api' new app in INSTALLED APPS

```py
INSTALLED_APPS = [
    # apps that I created
    "api",
    #apps that I installed
    "jazzmin",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    #apps that were already here
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

- Now in our blog folder, we already have one urls.py. We need to make some changes there.

- Add the following code in that urls.py

```py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # This should already be here for admin site
    path("admin/", admin.site.urls),
    # We have to include our urls.py from our api folder
    path("api/", include("api.urls")),
]

# We need to append a new url pattern for our media files.
# MEDIA_URL and MEDIA_ROOT was created by us in settings.py
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- In api/urls.py add the follwing code:

```py
from django.urls import path
# We need router for routing
from rest_framework.routers import DefaultRouter
# We need these for obtaining access and refresh tokens.
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# We need this for swagger UI
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

router = DefaultRouter()

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
]

# Append any routes that we might create using router
urlpatterns += router.urls

```

- After doing these you need to migrate the predefined data to database.

- In your terminal in virtual environment

> py manage.py makemigrations

> py manage.py migrate

- This will migrate all the data to your defined database.

- Create superuser or admin user using following command in terminal.

> py manage.py createsuperuser

- This will ask you email, username and password by default. You can change that but we havent done that. We may not even do that here.

- After creating user run command:

> py manage.py runserver

- you can visit localhost:8000/api and you will see a beautiful UI with swagger documentation. You will only see two endpoints. One for token obtain and one for token refresh because we have not defined any other routes.

### This is the initial setup you need to start with Django REST Framework.
