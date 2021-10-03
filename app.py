from flask import Flask, json
from flask_restful import reqparse, abort, Api, Resource
from flask import render_template, request
from pytube import YouTube
from flask import jsonify
from youtubevideos import db
from youtubevideos import *

db.create_all()

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
class video(Resource):
    def get(self, urlid, resolution):
        id, title, length, rating = downloadVideo('https://www.youtube.com/watch?v='+urlid, resolution)
        youTubeVideos.add_video(id, title, rating, length)
        response = Response("Video downloaded", 200, mimetype='application/json')
        return response

class paginate(Resource):
    def get(self):
        return jsonify(get_paginated_list(
        youTubeVideos.get_all_videos(), 
        '/videos', 
        start = 1, 
        limit = 1))

@app.route('/getall/')
def getallvideos():
    response = Response(jsonify(youTubeVideos.get_all_videos()), 200, mimetype='application/json')
    return jsonify(youTubeVideos.get_all_videos())

@app.route('/filters/<int:length>/<int:rating>')
def filter(length, rating):
    required_length = length
    required_rating = rating
    res = youTubeVideos.query.filter((youTubeVideos.length <= required_length) & (youTubeVideos.ratings > required_rating)).all()
    return jsonify([youTubeVideos.json(video) for video in res])


api.add_resource(video,'/video/<urlid>/<resolution>')
api.add_resource(paginate, '/paginate')

if __name__ == '__main__':
    app.run(debug=True)