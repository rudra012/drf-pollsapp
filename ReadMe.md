## Polls App with drf

### Install requirements
```
pip install -r requirements.txt
```

### Migrate and start server
```
python pollsapp/manage.py makemigrations

python pollsapp/manage.py migrate

python pollsapp/manage.py runserver
```

### Swagger link
* http://localhost:8000/swagger_doc/

* Create endpoint to perform CRUD operations for track. >> http://localhost:8000/api/tracks/
* Create an API endpoint to fetch a list of all questions belonging to a particular track. >> GET: http://localhost:8000/api/tracks/{id}/
* Create an API endpoint to fetch count of total correct answers and count of total wrong answers for a question. >> http://localhost:8000/api/questions/answer_summary/


- Create new Tracks with questions. 
- POST: http://localhost:8000/api/tracks/

- Get Listing and details of Tracks
- GET: http://localhost:8000/api/tracks/


