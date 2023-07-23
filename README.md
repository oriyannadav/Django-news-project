# Plus Resources: Django Project Starter

# Oriyan Nadav - She Codes News Project

## About This Project
She Codes News is a web application designed to provide a platform for users to share and read news stories. The application allows users to create an account or log in using their credentials. Once logged in, users can write news stories, including a title, content, and an optional image. The news stories are associated with the user who wrote them.

Users can also leave comments on news stories to engage in discussions with other users. Each news story can have multiple comments, and users can view and interact with these comments.

The application also includes features like the ability to search for specific news stories using a search bar and view the number of comments on each news story.

To use the She Codes News application, users can visit the website and create an account if they don't already have one. After logging in, they can write and publish their own news stories or read and interact with news stories written by others. They can leave comments, search for specific news stories, and view the comments on each story.

## How To Run This Code
To download and run the codebase, first, clone the repository to your local machine using the Git command git clone. Then, create a virtual environment to isolate the project dependencies by running python -m venv venv. Activate the virtual environment using the appropriate command for your operating system (e.g., venv\Scripts\activate on Windows or source venv/bin/activate on macOS/Linux). Next, install the required dependencies with pip install -r requirements.txt.

Once the dependencies are installed, migrate the database to set up the necessary tables using python manage.py migrate. To access the admin panel, create a superuser with python manage.py createsuperuser. Now, you're ready to run the development server by executing python manage.py runserver.

## Database Schema
![ERD](screenshots/ERD.png)

## Project Features
- [x] Order stories by date
    [Home_page-stories_ordered_by_date_1](she_codes_news/screenshots/home-page-screenshot1.png)
     [Home_page-stories_ordered_by_date_2](screenshots/home-page-screenshot2.png)
- [x] Styled "new story" form
    [Write-new-story](screenshots/write-new-story.png)
- [x] Story images
    ![Stories-images_1](screenshots/home-page-screenshot3.png)
     [Stories-images_2](screenshots/home-page-screenshot4.png)
- [x] Log-in/log-out[Login](screenshots/login.png)[Logout](screenshots/logout.png)
- [x] "Account view" page
    [Profile](screenshots/profile.png)
- [x] "Create Account" page
    ![Create-account_1](screenshots/create-account1.png)
     [Create-account_2](screenshots/create-account1.png)
- [x] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in
    ![Login](screenshots/login.png)
     [Logout](screenshots/logout.png)
- [x] "Create Story" functionality only available when user is  logged in
    ![Login](screenshots/login.png)
     [Logout](screenshots/logout.png)

## Additional Features:
- [x] Our form for creating stories requires you to add the publication date, update this to automatically save the publication date as the day the story was first published.
    ![Latest-news](screenshots/latest-news.png)
- [x] User can update they're profile.
    ![Update-profile](screenshots/update-profile.png)