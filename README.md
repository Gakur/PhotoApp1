# PHOTOGRAM

>[Peter- Gakure](https://github.com/Gakur/PhotoApp1)  
  
# Description  
This is a clone of  Instagram website where people share their  images and videos for other users to view. 
Users can sign up, login, view and post photos, search and follow other users.
##  Live Link  
 Click [View Site]()  to visit the site
  
 
## User Story  
  
* Sign in to the application to start using.  
* Upload a pictures to the application. 
* Search for different users using their usernames.  
* See your profile with all your pictures.  
* Follow other users and see their pictures on my timeline.  
  
  
## Setup and Installation  
To get the project .......  
  
##### Clone the repository:  
 ```bash 
 https://github.com/Gakur/PhotoApp1
```
##### Navigate into the folder and install requirements  
 ```bash 
cd PhotoApp/
pip install -r requirements.txt 
```
##### Install and activate Virtual environment 
 ```bash 
- python3 -m venv virtual - 
source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, then make migrations
 ```bash 
python manage.py makemigrations
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 

##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django ](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [petergakure97@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Gakur/PhotoApp1/Picture-Globe/blob/master/LICENSE)  
* Copyright (c) 2021 **Peter Gakure**