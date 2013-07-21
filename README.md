sidar
=====

Repository for Shenkar Institute of Design and Research

The site is available for viewing at: http://morning-beach-2325.herokuapp.com/

Development database is availabe at: https://dl.dropboxusercontent.com/u/2794286/sqlite3.db
username: admin
password: admin

Quick Start
-----------
1. Clone the repository:
  git clone https://github.com/danielbraun/sidar.git
2. Change your working directory
    `cd sidar`
3. Install the dependencies globally:
	`sudo pip install django`
	`sudo pip install -r requirements.txt`
4. Create the database:
    `python manage.py syncdb`
5. Run the development server:
    `python manage.py runserver`
