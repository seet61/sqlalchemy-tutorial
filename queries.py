# coding=utf-8

# 1 - imports
from models.actor import Actor
from models.base import Session
from models.contact_details import ContactDetails
from models.movie import Movie


# 2 - extract a session
session = Session()

# 3 - extract all movies
movies = session.query(Movie).all()

# 4 - print movies' details
print '\n### All movies:'
for movie in movies:
    print '%s was released on %s' % (movie.title, movie.release_date)
print ''