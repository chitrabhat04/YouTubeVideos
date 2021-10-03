# YouTube download- REST API, Pagination-Metadata filters- REST API, Google Authentication-Authorization REST API
Requirements:
1. Python
2. PostMan

Create your virtual environment in your required directory and using cmd create a virtual environment by running *** python -m venv env *** and
Activate virtual environment by running *** .\env\Scripts\activate *** or 
Install required installments by running *** pip install -r /path/to/requirements.txt ***
Run app.py, youtube.py, settings.py.
1. API endpoint for downloading a YouTube video: http://127.0.0.1:5000/video/<urlid>/<resolution>
	a. Enter the urlid of the required YouTube video; for instance the urlid for the given url https://www.youtube.com/watch?v=TnkdoEZhTbc is TnkdoEZhTbc, and resolution in the format '720p'
	b. Set the method to GET, the video will be downloaded to the repository
2. API endpoint to view all videos: http://127.0.0.1:5000/getall/
	a. Set the method to GET and on sending the request, all the videos will be displayed.
3. API endpoint to get videos with pagination: http://127.0.0.1:5000/paginate/
4. API endpoint to filter according to the metadata(length, ratings): http://127.0.0.1:5000/filters/<int:length>/<int:rating>
	a. The two filters are according to length and ratings.
	b. Set the method to GET to get entries satisfying the condition 
5. Create your credentials at Google API console. API endpoint to login, to authorize, to logout: http://127.0.0.1:5000/(login/authorize/logout). 
