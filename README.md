# Django-photo-app

Source code for the article  [Build a Django full stack Photo-Sharing app]().

## Features

- Django CRUD functionality

- User authentication 
    - Login
    - Logout
    - Sign-up

- Image Uploads

- Reused code with Django Template Language

- Stylized pages with Bootstrap 5


## SetUp

Clone the repository:

```bash
git clone https://github.com/DaniDiazTech/Django-photo-app.git

cd Django-photo-app/
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it

```bash
source .venv/bin/activate
```

![Virtual environment activated](https://uploads.sitepoint.com/wp-content/uploads/2021/06/1622669492venv.png)

Install all the project dependencies with the `requirements.txt` with the following command.

```bash
pip install -r requirements.txt
```

Run the migrations:

```bash
python manage.py migrate
```

Run the project.

```bash
python manage.py runserver
```

Visit your [localhost](http://localhost:8000/).

![Main Page](https://uploads.sitepoint.com/wp-content/uploads/2021/05/1622404676list.png)

## Screenshots


![Dashboard](https://camo.githubusercontent.com/b91eb6691fa1cf9f611ba0b203f2e6f3e0c858de72a4374d5307c2005aff511a/68747470733a2f2f75706c6f6164732e73697465706f696e742e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032312f30352f313632323430343637366c6973742e706e67)

![Tag Dashboard](https://camo.githubusercontent.com/2c72474471d3074367f0dbbd5a60f652ec56f450186793639d40dc84d360a068/68747470733a2f2f75706c6f6164732e73697465706f696e742e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032312f30352f313632323430343637397461672d6c6973742e706e67)

![Detail page](https://camo.githubusercontent.com/9f9726e296539c66c5bab09984a5e3d9e8b9745fa0b0ac061f07e81f3ebd3e69/68747470733a2f2f75706c6f6164732e73697465706f696e742e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032312f30352f3136323234303534303566697273742d70686f746f2e706e67)

![Delete page](https://camo.githubusercontent.com/c694125655898730707b4cd0f04c7775401db3e3bea8d035d743b271bf78f2e3/68747470733a2f2f75706c6f6164732e73697465706f696e742e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032312f30352f3136323234313930323164656c6574652e706e67)

![Signup page](https://camo.githubusercontent.com/7e78e06bdf833096bc4231740d8a48384042cab423038e08aae7624d6aeeb4e6/68747470733a2f2f75706c6f6164732e73697465706f696e742e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032312f30352f313632323431393439337369676e75702e706e67)
