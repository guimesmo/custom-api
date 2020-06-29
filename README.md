# Django API and client examples

### Running the server
´´´
cd sever
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Running server tests
`python manage.py test`

### Running the client
´´´
cd client
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python client.py <command> <options>
```

Try `python client.py` with no action to see available options 

### Running client tests
`python -m unittest discover`




