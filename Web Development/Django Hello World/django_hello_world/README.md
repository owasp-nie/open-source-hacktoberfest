# Django Hello World

## Getting Started

Before you can work with this Django project, make sure you have the following prerequisites installed on your PC:

- [Python](https://www.python.org/downloads/)

### Create a Virtual Environment

It's a good practice to work within a virtual environment to isolate project dependencies. Follow these steps to create and activate a virtual environment:

1. Open your terminal/command prompt.

2. Navigate to the project directory where you want to create the virtual environment.

3. Create a virtual environment using the following command (replace `project-name` with your desired name):

```shell
python -m venv project-name
```

4. Activate the virtual environment:

For Windows:

```shell
project-name\Scripts\activate.bat
```

For macOS and Linux:

```shell
source project-name/bin/activate
```

### Install Project Dependencies

Inside your activated virtual environment, download and install the project's requirements using pip:

```shell
pip install -r requirements.txt
```

### Start the Development Server

To run the Django development server, navigate to the directory where `manage.py` is located and execute the following command:

```shell
python manage.py runserver
```

This will start the server, and you'll see output indicating that the server is running.

### Access the Application

Open your web browser and enter the following URL:

```
http://127.0.0.1:8000/
```

You should now be able to access the Django project at this URL in your local development environment.

That's it! You have successfully set up and started the Django project locally. You can now begin working with the project and making any necessary customizations or additions.