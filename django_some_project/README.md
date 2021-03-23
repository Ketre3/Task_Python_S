**Used dependencies:**
- django  
- djangorestframework  
- djangorestframework-simplejwt  

**Installation:**  
- `python3.8 -m venv venv`  
- `source venv/bin/activate`  
- `pip install -r requirements.txt`  
- `python manage.py makemigrations`  
- `python manage.py migrate`  
- `python manage.py runserver`  


**Urls:**
- `/api/post/all` - all posts
- `/api/post/{post_id}/like` - like (or unlike) post with {post_id}
- `/api/analytics/likes/?date_from={date_from}&date_to={date_to}` - analytics about how many likes were made aggregated by day
- `/api/analytics/user/{username}` - analytics about user last activity
- `/api/account/login`
- `/api/account/register`
- `/api/account/refresh` - refresh jwt token with refresh token
