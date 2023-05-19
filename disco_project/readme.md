# Image Hosting API
<div id="top"></div>

Project Requirements
1. Skip the registration part, assume users are created via the admin panel.
2. Users should be able to do the following:
a. Upload images via HTTP request
b. List their images
3. There are three account tiers – Basic, Premium and Enterprise.
    - Users that have a "Basic" plan after uploading an image get:
        - A link to a thumbnail that's 200px in height
    - Users that have a "Premium" plan get:
        - A link to a thumbnail that's 200px in height
        - A link to a thumbnail that's 400px in height
        - A link to the originally uploaded image
    - Users that have an "Enterprise" plan get:
        - A link to a thumbnail that's 200px in height
        - A link to a thumbnail that's 400px in height
        - A link to the originally uploaded image
        - Ability to fetch a link for a previously uploaded image that expires after a number of seconds (user can specify any number between 300 and 30000)

4. Admins should be able to create arbitrary plans with the following
configurable attributes:
    - Thumbnail sizes
    - Presence of the link to the originally uploaded file
    - Ability to generate expiring links
5. Admin UI should be done via django-admin
6. There should be NO custom user UI (just browsable API from DRF)


This is based on the **Django Rest Framework** application 
It provides onlu api endpoints, so please follow the docs to see available URLS. 

## Table of contents
* [Technologies Used](#technologies-used)
* [Features implemented](#features-implemented)
* [Available Urls](#available-urls)

## Technologies Used
* Python 3.10
* Django 4.1.7
* Django REST 3.14
* MySQL 


## Features Implemented
- users can upload images via HTTP request
- users can list their uploaded images
- three builtin `account tiers Basic, Premium and Enterprise`
  - users that have a `"Basic"` plan after uploading an image get: 
    - a link to a thumbnail that's 200px in height
  - users that have a `"Premium"` plan get:
    - a link to a thumbnail that's 200px in height
  - a link to a thumbnail that's 400px in height
    - a link to the originally uploaded image
  - users that have a `"Enterprise"` plan get
    - a link to a thumbnail that's 200px in height
    - a link to a thumbnail that's 400px in height
    - a link to the originally uploaded image
    - the ability to fetch a link to the (binary) image that **expires** after several seconds (user can specify any number between 300 and 30000) and download it


## Available Urls

- http://localhost:8000/images
- http://localhost:8000/admin

