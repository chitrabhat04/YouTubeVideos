from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask import Flask
from flask import render_template, request
from pytube import YouTube
from flask_mysqldb import MySQL
from flask_paginate import Pagination, get_page_parameter
from flask import jsonify

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'sys'

mysql = MySQL(app)
api = Api(app)

def downloadVideo(url, resolution):
    yt = YouTube(url)
    if yt.streams.filter(progressive = True, file_extension = 'mp4', res=resolution).first():
        yt.streams.filter(res=resolution).first().download('.')
    else: yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    return str(yt.video_id), str(yt.title), int(yt.length), str(yt.rating)


def get_paginated_list(results, url, start, limit):
        start = int(start)
        limit = int(limit)
        count = len(results)
        if count < start or limit < 0:
            abort(404)
        # make response
        obj = {}
        obj['start'] = start
        obj['limit'] = limit
        obj['count'] = count
        # make URLs
        # make previous url
        if start == 1:
            obj['previous'] = ''
        else:
            start_copy = max(1, start - limit)
            limit_copy = start - 1
            obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
        # make next url
        if start + limit > count:
            obj['next'] = ''
        else:
            start_copy = start + limit
            obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
        # finally extract result according to bounds
        obj['results'] = results[(start - 1):(start - 1 + limit)]
        return obj



class Todo(Resource):
    def get(self, url, resolution):
        id, title, length, rating = downloadVideo('https://www.youtube.com/watch?v='+url, resolution)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO youtubeVideos(id,title, length, rating) VALUES (%s, %s, %s, %s)", (id, title, length, rating))
        mysql.connection.commit()
        cur.close()
        return "Video downloaded"

class Todom(Resource):    
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * from youtubevideos')
        return cur.fetchall()
class videos(Resource):
    def get(self):
        return jsonify(get_paginated_list(
        Todom.get(self), 
        '/videos', 
        start = 1, 
        limit = 1
    ))


api.add_resource(Todo, '/todos/<url>/<resolution>')
api.add_resource(Todom, '/todom/')
api.add_resource(videos, '/videos/')


if __name__ == '__main__':
    app.run(debug=True)