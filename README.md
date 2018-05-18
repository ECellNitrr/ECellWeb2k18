# ECellWeb2k18
Back end repository of E-Cell NITRR made in 2k18.

# Steps to test in localhost
```
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ ./manage.py migrate
    $ ./manage.py createsuperuser # creates superuser
    $ ./manage.py runserver
```

# Database
For the sake of development the database is still on sqlite. You may change anytime with mySQL or any similar database server.

# Development
Fork the repo and the development is done in dev branch. Create a new feature branch from dev branch and create a pull request.