# Receipt Generation System

This application takes in user input in the form `name` , `address`, `phone number`, `total cost` and then generates a receipt in Pdf format then stores it on the backend server.

## Tools Used
Python, Django, Django Rest Framework, Swagger UI and xhtml2pdf

## Code Usage
- Clone the repository
- Create your environment 
 ```shell
       python3 -m venv env
 ```
 - Activate your environment 
 ```shell
       source env/bin/activate
 ```
 - Install all requirements
 ```shell
       pip install -r requirements.txt
 ```
 - Make migrations
```shell
       python3 manage.py makemigrations
 ```
 - Migrate changes
```shell
       python3 manage.py migrate
 ```
 - Run the following command to run the code in development mode
```shell
       python3 manage.py runserver
 ```

## Link to deployed application
Application was deployed on the heroku server and it can be accessed via [this link](https://receipt-generation-system.herokuapp.com/)

## Preview
Below is an image of the Swagger UI for the application
<br>
<img src="./static/images/Screenshot.png"> 
