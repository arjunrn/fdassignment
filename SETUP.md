
###Steps to Run the application

1. Create a virtualenv with Python3.
2. Install the requirements from the requirements.txt file `pip install -r requirements.txt`
3. Then run `python manage.py synddb` to create the tables in the database.
4. Create a superuser if required.
5. Import the words into the data with the management command `python manage.py dictionary <name_of_file>`
6. Run the server using `python manage.py runserver`