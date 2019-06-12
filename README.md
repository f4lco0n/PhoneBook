# PhoneBook
Simply webapp in Django which displays users and their emails and phones.

**Setup:**

Virtualenv:

*pip install virtualenv*

*mkdir project*

*cd project*

*virtualenv venv*

*source venv/bin/activate*

**Install requriments:**

*pip install -r requriments.txt*

**Load data from fixtures:**

*python manage.py loaddata fixturex.json*

**Endpoints:**

*server:port/people* -> return list of current users in db with their emails and phones if exist

*server:port/people/new* -> here we can create new user (only PersonModel)

**Update user:**
Click on his link
