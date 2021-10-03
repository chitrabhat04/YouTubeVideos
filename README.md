# YouTube download- REST API, Pagination-Metadata filters- REST API, Google Authentication-Authorization REST API
Requirements:
1. Python
2. PostMan

Create your virtual environment in your required directory and using cmd create a virtual environment by running *** python -m venv env *** and
Activate virtual environment by running *** .\env\Scripts\activate *** or 
Install required installments by running *** pip install -r /path/to/requirements.txt ***
Run settings.py, youtubeVideos.py, app.py.
1. API endpoint for downloading a YouTube video: http://127.0.0.1:5000/video/<urlid>/<resolution> <br />
	a. Enter the urlid of the required YouTube video; for instance the urlid for the given url https://www.youtube.com/watch?v=TnkdoEZhTbc is TnkdoEZhTbc, and resolution in the format '720p' <br />
	b. Set the method to GET, the video will be downloaded to the repository <br />
2. API endpoint to view all videos: http://127.0.0.1:5000/getall/ <br />
	a. Set the method to GET and on sending the request, all the videos will be displayed. <br />
3. API endpoint to get videos with pagination: http://127.0.0.1:5000/paginate/ <br />
	a. Pagination is set at 1 video/page. Can be changed by changing the limit in get_paginated_list in app.py. <br />
4. API endpoint to filter according to the metadata(length, ratings): http://127.0.0.1:5000/filters/<int:length>/<int:rating> <br />
	a. The two filters are according to length and ratings. <br />
	b. Set the method to GET to get entries satisfying the condition  <br />
5. Create your credentials at Google API console. API endpoint to login, to authorize, to logout: http://127.0.0.1:5000/(login/authorize/logout). 
