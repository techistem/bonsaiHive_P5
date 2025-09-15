# bonsaiHive_P5

BonsaiHive Backend is the backbone of the BonsaiHive community platform, powering the features that bring bonsai enthusiasts together. While the frontend creates the interactive experience, the backend manages all the behind-the-scenes work — securely handling posts, profiles, comments, contacts, events, followers, likes, and reviews.

It ensures that only registered members can access content, allows users to create, update, and delete their contributions, and keeps all data organized and reliable. By providing a smooth and secure API for the frontend, the backend enables BonsaiHive to grow both bonsai knowledge and a connected, engaged community across West Sussex.

Deployed API Heroku: [API link](https://drf-bonsaihive-91939050de59.herokuapp.com/)

Deployed Frontend Heroku: [bonsaihive-react](https://bonsaihive-react-dbe9685329cb.herokuapp.com/#/)

Backend Github [Repository](https://github.com/techistem/bonsaiHive_P5)

Frontend Github [Repository] (https://github.com/techistem/bonsaihive-react)

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
- [Obsidian](https://code.visualstudio.com/) - To keep notes.
