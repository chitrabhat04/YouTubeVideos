from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from settings import *


# Initializing our database
db = SQLAlchemy(app)




# the class Movie will inherit the db.Model of SQLAlchemy
class youTubeVideos(db.Model):
    __tablename__ = 'youtubeVideos'  # creating a table name
    id = db.Column(db.String(), primary_key=True)  # this is the primary key
    title = db.Column(db.String(), nullable=False)
    # nullable is false so the column can't be empty
    ratings = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer)
    def json(self):
        return {'id': self.id, 'title': self.title,
                'ratings': self.ratings, 'length': self.length}
        # this method we are defining will convert our output to json
    def add_video(_id, _title, _ratings, _length):
        '''function to add movie to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our Movie constructor
        new_movie = youTubeVideos(id = _id, title=_title, ratings = _ratings, length = _length)
        db.session.add(new_movie)  # add new movie to database session
        db.session.commit()  # commit changes to session
    def get_all_videos():
        '''function to get all movies in our database'''
        return [youTubeVideos.json(video) for video in youTubeVideos.query.all()]
    def delete_video(_id):
        '''function to delete a movie from our database using
           the id of the movie as a parameter'''
        youTubeVideos.query.filter_by(id=_id).delete()
        # filter movie by id and delete
        db.session.commit()  # commiting the new change to our database

# class videos(Resource):
#     def get(self):
#         return jsonify(get_paginated_list(
#         Todom.get(self), 
#         '/videos', 
#         start = 1, 
#         limit = 1
#     ))


# api.add_resource(Todo, '/todos/<url>/<resolution>')
# api.add_resource(Todom, '/todom/')
# api.add_resource(videos, '/videos/')


# if __name__ == '__main__':
#     app.run(debug=True)