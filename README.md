# CostFinder-using-REST-API

The Cost Finder App is a Django-based application that allows users to find the cost of various fruits and vegetables. 
The project consists of two parts: 
- A server that provides a REST API with the cost information
- A client application that fetches and displays this information based on user input.

# Description

This project demonstrates a simple client-server architecture where:
- The server hosts an API that returns the cost of various fruits and vegetables.
- The client provides a user interface to input the name of a fruit or vegetable and displays the cost by making a request to the server's API.

# Features

**REST API**: Provides cost data for 30 different fruits and vegetables.

**Client Application**: Allows users to input the name of a fruit or vegetable and fetch its cost.

**Responsive Design**: Ensures the application works well on different screen sizes.

**Simple Form Validation**: Ensures that the user inputs only alphabetic characters.


# Installation

**Prerequisites**
- Python 3.x
- Django 3.x
- Django REST framework

- pip install django
- pip install djangorestframework
- pip install requests

# How to Run

**Running the Server**:
    
    cd cf_project
    
1) Set Up the Database:
    ```
    python manage.py migrate
    ```

2) Create a Superuser:
    ```
    python manage.py createsuperuser
    ```
3) Start the server:
   ```
   python manage.py runserver
   ```
   The server will be running at http://127.0.0.1:8000/.

**Running the Client**:

    cd cfc_project
    
1) Start the client:
   ```
   python manage.py runserver
   ```
   The server will be running at http://127.0.0.1:8000/.

**Using the Application**
- Open your web browser and navigate to http://127.0.0.1:8000/.
- Enter the name of a fruit or vegetable in the input form and submit.
- View the cost of the entered item on the result page.

# Dependencies
- Django
- Django REST framework
- Requests

# Important Files

**Server**
- settings.py: Django settings file.
- urls.py: URL routing file.
- models.py: Defines the CostModel model.
- views.py: Contains the logic for the views.
- ser.py: Serializer for the CostModel.

**Client**
- settings.py: Django settings file.
- urls.py: URL routing file.
- views.py: Contains the logic for the views.
- templates/: Contains all HTML templates for the project.
- static/: Contains static files like CSS.

# Contributing
Contributions are welcome! 
Please fork this repository and submit pull requests for any features, enhancements, or bug fixes.

# License
This project is licensed under the MIT License. 
See the LICENSE file for details.

# Author
Sudarshan Thiruppathi



