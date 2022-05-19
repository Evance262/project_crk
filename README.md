**Crk Desisgn**

**System model**
    
    This web app uses the social network model.
    for instance:

    • An authentication system for users to register, log in, edit their profile,
    and change or reset their password
    • A follow system to allow users to follow each other on the website
    • A functionality to display shared images and implement a bookmarklet
    for users to share images from any website
    • An activity stream that allows users to see the content uploaded by the
    people that they follow

**Environment setup**

    run the following commands to set up the project:

    python3 get-pip.py

    pip install virtualenv

    python3 -m venv virtualenv_name

    source virtualenv_name/bin/activate  # (On Linux server)

    virtualenv_name\scripts\activate     # (On Windows machine)

    pip install requirements.txt

    python3 manage.py runserver

**Note:**

    Once te server is running on you can go in your browser and
    request http://127.0.0.1:8000 to get to the web app's landing page.