# Hello World Generative Application

This application was crafted using Python 3, Flask, and the OpenAI API. Below are the steps I followed to bring it to life.

## Initial Setup

- OpenAI's Python package was essential, which necessitated the installation of pip.
- `pip install openai`

Remember to generate a secret key from your OpenAI account and replace `your-own-api-key` with the actual key for security purposes.

- I also established a virtual environment for better isolation.
- Create a virtual environment: `python -m venv venv`
- Activate it:
  - For MAC/Linux: `source venv/bin/activate`
  - For Windows: `.\venv\Scripts\activate`



## Generative AI with Python

- I started by using the template code offered by my instructor. Encountering version compatibility issues, I updated to the latest OpenAI model and migrated my codebase accordingly. This allowed the generative AI to function within my terminal environment.

## Web Server with Flask

- To bring the generative messages to a web platform, I installed Flask and adapted my script to operate within a web server environment.
- `pip install flask`
-  Additionally, I crafted a template to display the messages on the web.


## Simple Styling and Dynamic Background

- To finalize the look, I applied basic CSS for styling and implemented a dynamic background that changes upon page refresh.

## Running the Application

Assuming you have already installed the necessary packages (pip, python3, flask, openAI), follow these steps to launch the application:

1. **Activate your virtual environment.**

2. **Set up the Flask application environment variable to the name of your python script.**

For Mac/Linux: `export FLASK_APP=hello_world_generator`
              `flask run`
For Windows: `set FLASK_APP=hello_world_generator`
             `flask run`


3. **Access the Application:** Flask will provide a local URL in the terminal (typically http://127.0.0.1:5000/). Navigate to this address in your web browser to interact with the application.

4. **View the Application:** The URL will render the "Hello World" message through the `index.html` template. The dynamic background can be viewed by refreshing the page.


