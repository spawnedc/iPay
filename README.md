# iPay
An app that helps you to track your monthly payments

Requirements:
Python version:2.6

Installation using virtualenv:

        $ curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py
        $ python virtualenv.py myApp
        $ . myApp/bin/activate

Note: with the above activation your prompt would change to notify that you are inside the virtualenv myApp

Installing pip inside the virtualenv:

        $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
        
Once the above pip installation is done, clone the github project

        $ git clone git@github.com:gkesavan/iPay.git

now that the repo is cloned, lets use pip to install all required modules to start the server
        $ cd iPay
        $ pip install -r requirements.txt
        $ ./manage.py startapp pay  # give it any name - I used pay
        $ ./manage.py runserver

This would start the ipay app on http://127.0.0.1:8000 

enjoy


