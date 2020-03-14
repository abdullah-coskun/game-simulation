## To Run With Docker:
After you started the docker and be sure about docker is running you can simply 
run this commands :<br/>
docker-compose build<br/>
then<br/>
docker-compose up<br/>
in the first time you start the project. <br/>
After that only docker-compose up will be sufficient unless any database or<br/>
library change occurs. If this will be the case you should also run docker-compose build <br/>
before docker-compose up. Sometimes build does not install libraries that you need<br/>
if this is the case you need to run docker-compose down first then build then up.<br/>
## To Run With Virtual Environment:
Create Virtual environment with :<br/>
virtualenv "name_of_virtualenv"<br/>
or <br/>
python3 -m venv venv <br/>
*If you have both python3 and python2 you should specify the version outside of virtual environment<br/>
Then activate virtual environment:<br/>
for windows:<br/>
source env/bin/activate<br/>
for mac:<br/>
. venv/bin/activate<br/>
You should create virtual environment for only first time but activate every time. <br/>

Then you should install packages in requirements if any new package was added to project :<br/>
pip install -r requirements.txt<br/>

Then the project is ready to go. To create or update database:<br/>
python manage.py makemigrations --settings=api.settings.local<br/>
python manage.py migrate --settings=api.settings.local<br/>

After that you can run the project:<br/>
python manage.py runserver --settings=api.settings.local<br/>
*settings in manage.py actually for docker run so setting should be given by hand when running locally<br/>
## To Run Unit Tests:
 python manage.py test <"name_of_app"> --settings=api.settings.local<br/>

