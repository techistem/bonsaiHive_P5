# bonsaiHive_P5

BonsaiHive Backend is the backbone of the BonsaiHive community platform, powering the features that bring bonsai enthusiasts together. While the frontend creates the interactive experience, the backend manages all the behind-the-scenes work — securely handling posts, profiles, comments, contacts, events, followers, likes, and reviews.

It ensures that only registered members can access content, allows users to create, update, and delete their contributions, and keeps all data organized and reliable. By providing a smooth and secure API for the frontend, the backend enables BonsaiHive to grow both bonsai knowledge and a connected, engaged community across West Sussex.

Deployed API Heroku: [API link](https://drf-bonsaihive-91939050de59.herokuapp.com/)

Deployed Frontend Heroku: [bonsaihive-react](https://bonsaihive-react-dbe9685329cb.herokuapp.com/#/)

Backend Github [Repository](https://github.com/techistem/bonsaiHive_P5)

Frontend Github [Repository](https://github.com/techistem/bonsaihive-react)

## Contents

## Contents

- [Database Diagram](#database-diagram)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Deployment and Local Development](#deployment-and-local-development)
  - [Local Development](#local-development)
    - [How to fork](#how-to-fork)
    - [How to clone](#how-to-clone)
    - [Deployment](#deployment)
- [Testing](#testing)
- [Credits](#credits)

### User Stories

I have created tasks and included links to the [GitHub Issues](?????) for this project, as well as the [KANBAN board](??????).

## Database Diagram

[Database Diagram](?????)

## Technologies

- Django
  - Main framework used for application creation
- Django REST Framework
  - Framework used for creating API
- Heroku
  - Used for hosting the deployed application
- GitPod
  - Used for building and version control
- Github
  - Repository for storing code base and docs

### PostgreSQL Database

A PostgreSQL database was set up to handle all project data using the Code Institute database creation tool.

The database is linked to both the API and the frontend interface through Heroku’s Config Vars. To prevent sensitive information from being exposed on GitHub, the database URL is stored in an env.py file, which is excluded from the deployment build.

### Cloudinary

Cloudinary was used to store all images uploaded to the site, such as user profile pictures and post images.

The service is connected to both the API and the frontend via Heroku Config Vars. To ensure sensitive information is kept secure and not exposed on GitHub, the Cloudinary URL is stored in an env.py file, which is excluded from the deployment build.

### Secret Key

A unique secret key was generated using a [Django Secret Key Generator](https://djecrety.ir/)
and stored securely in the env.py file. This ensures that the key is kept private and is not exposed on GitHub or included in the deployed build.

## Python Packages

### Core Framework

- **Django==4.2.7** – Main framework used to start the project
- **djangorestframework==3.14.0** – Framework used to build the API endpoints
- **django-filter==23.5** – Used to filter API results in serializers

### Authentication & Authorization

- **django-allauth==0.50.0** – Authentication, registration, account management
- **dj-rest-auth==2.1.9** – REST API endpoints for authentication
- **djangorestframework-simplejwt==5.3.1** – JWT authentication for DRF
- **PyJWT==2.9.0** – JSON Web Token handling
- **oauthlib==3.2.2** – Dependency for OAuth support
- **requests-oauthlib==2.0.0** – Dependency for OAuth requests
- **python3-openid==3.2.0** – Dependency for OpenID authentication

### Database

- **dj-database-url==2.3.0** – Parse the `DATABASE_URL` connection settings
- **psycopg2==2.9.10** – PostgreSQL database adapter

### Static & Media Files

- **whitenoise==6.9.0** – Serve static files in production
- **cloudinary==1.43.0** – Cloud storage for images
- **django-cloudinary-storage==0.3.0** – Django integration with Cloudinary

### Deployment & Utilities

- **gunicorn==21.2.0** – WSGI HTTP server for deployment
- **Pillow==11.1.0** – Imaging library, used for image uploads

### Core Dependencies (installed automatically)

- **asgiref==3.8.1** – ASGI framework support for Django
- **sqlparse==0.5.3** – SQL parsing library (required by Django)

#### Programs Used

- [GitHub](https://github.com/) - To save and store files for the website.
- [VSCode](https://code.visualstudio.com/) - Code editor used for local development.
- [GitPod](https://gitpod.io/) - IDE used to create the site.
- [DBdiagram](/https://dbdiagram.io/home) - To create database diagrams.
- [Shields IO](https://shields.io/) - To add badges to README.

## Cloning the Repository

To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project: [bonsaiHive_P5](https://github.com/techistem/bonsaiHive_P5.git).
3. Click on the **Code** button, select one of HTTPS, SSH, or GitHub CLI, and copy the link shown.
4. Open the terminal in your code editor and navigate to the directory where you want the project to be cloned.
5. Run the following command:

   ```bash
   git clone <repository-link>
   ```

### Deployment

The finished program was initially hosted within a repository on Github, and then this Github repository was connected with Heroku, the site through which the program is deployed.

### Deployment to Heroku

The steps to deploy this project to **[Heroku](https://www.heroku.com/)** are as follows:

- Create Heroku app

  - Go to the [Heroku](https://www.heroku.com/) dashboard and click the "Create new app" button.
  - Name the app. Each app name on Heroku has to be unique.
  - Then select your region.
  - And then click "Create app".

- In the IDE file explorer or terminal

  - Create new env.py file on top level directory

- In env.py
  - Import os library
  - Set environment variables
  - Add database url
  - Add in secret key

```python
import os

os.environ['DEV'] = '1'
os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"
os.environ["CLOUDINARY_URL"] = "Paste in the API Environment variable"
```

If you don't already have an account to Cloudinary, create one [here](https://cloudinary.com/).

- Cloudinary

  - Go to the Cloudinary dashboard and copy the API Environment variable.
  - Paste in env.py variable CLOUDINARY_URL(see above)

- In settings.py and to the INSTALLED_APPS add :

```python
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',
'rest_framework',
'django_filters',
'rest_framework.authtoken',
'dj_rest_auth',
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
'corsheaders',
```

- Import the database, the regular expression module & the env.py

```python
import dj_database_url
import re
import os
if os.path.exists('env.py'):
    import env
Below the import statements, add the following variable for Cloudinary:
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

- Below INSTALLED_APPS, set site ID:

```python
SITE_ID = 1
```

- Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ else
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
```

- Set the default renderer to JSON:

```python
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```

- Beneath that, add the following:

```python
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```

- Then add:

```python
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}
```

- Update DEBUG variable to:

```python
DEBUG = 'DEV' in os.environ
```

- Update the DATABASES variable to:

```python
DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}
```

- Add the Heroku app to the ALLOWED_HOSTS variable:

```python
ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),
    'localhost',
]
```

- Below ALLOWED_HOST, add the CORS_ALLOWED variable:

```python
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if "CLIENT_ORIGIN_DEV" in os.environ:
    extracted_url = re.match(
        r"^.+-", os.environ.get("CLIENT_ORIGIN_DEV", ""), re.IGNORECASE
    )
```

- Also add to the top of MIDDLEWARE:

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]
```

Final requirements:

- Create a Procfile, & add the following two lines:

```text
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_name.wsgi
```

- Migrate the database:

```text
python3 manage.py makemigrations
python3 manage.py migrate
```

- Freeze requirements:

```text
pip3 freeze --local > requirements.txt
```

- In heroku app
  - Go to the settings tab.
  - In the settings click the button "Reveal Config Vars".
  - Click Add and use

| KEY               | VALUE                                             |
| ----------------- | ------------------------------------------------- |
| DATABASE_URL      | Paste in ElephantSQL database URL                 |
| SECRET_KEY        | Your own randomSecretKey                          |
| CLOUDINARY_URL    | Paste in the API Environment variable             |
| ALLOWED HOST      | api-app-name.herokuapp.com                        |
| CLIENT_ORIGIN     | <https://your-react-app-name.herokuapp.com>\*     |
| CLIENT_ORIGIN_DEV | <https://gitpod-browser-link.ws-eu54.gitpod.io>\* |

    *Check that the trailing slash \ at the end of both links has been removed.

- Go to the deploy tab.
- Choose the deployment method.
- Select Github, and confirm to connect to Github.
- Search for the Github repository name.
- Then click "connect".
- Scroll down and click "Deploy Branch".
