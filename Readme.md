# Fuel Route Optimization Project

## Project Overview

This project aims to calculate the optimal fuel stops along a driving route. It uses the OpenRouteService API to get the route between a start and end location, breaks the route into 500-mile segments, and suggests the most cost-effective fuel stops based on the price per gallon.

## Features:
1. Route Calculation: Calculates the driving route between two locations using the OpenRouteService API.
2. Fuel Stop Optimization: Finds the cheapest fuel stops along the route in 500-mile segments.
3. Django Admin Integration: Provides a simple Django admin panel to manage fuel stops and their details.


## Project Setup

Follow these steps to set up the project on your local machine.

### Prerequisites:
1. Python 3.x installed.
2. Django installed.
3. Django Rest Framework installed.
4. Requests library for making HTTP requests to APIs.
5. An OpenRouteService API key for route calculations.



### Step 1: Clone the Repository

Clone the project from your repository:

bash
git clone <repository_url>
cd <repository_name>




### Step 2: Create and Activate Virtual Environment

Create a virtual environment and activate it:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate




### Step 3: Install Dependencies

Install the required dependencies:

bash
pip install -r requirements.txt




### Step 4: Set Up the Database

Run migrations to set up the database:

bash
python manage.py migrate




### Step 5: Create Superuser for Admin Access

Create a superuser to access the Django admin panel:

bash
python manage.py createsuperuser


You will be prompted to enter the following:
- Username: admin
- Password: P@55word



### Step 6: Running the Development Server

Start the development server:

bash
python manage.py runserver


Access the project at `http://127.0.0.1:8000/` in your browser.



### Step 7: Accessing the Django Admin Panel

To manage fuel stop data, access the admin panel by navigating to:


http://127.0.0.1:8000/admin


## Login with the following credentials:
- Username: admin
- Password: P@55word

Here you can manage fuel stops, including adding new stops, editing existing stops, and deleting stops.



## API Usage

### Route Optimization Endpoint

To use the route optimization feature, send a `GET` request to:


/optimize-route/


Query Parameters:
- `start`: Coordinates for the starting location (longitude, latitude).
- `finish`: Coordinates for the finishing location (longitude, latitude).

Example Request:

/optimize-route/?start=-117.07986,34.867788&finish=-117.084285,34.853215


### OpenRouteService API Key

To use the OpenRouteService API, you need an API key. You can obtain an API key from the [OpenRouteService website](https://openrouteservice.org/sign-up/).

Once you have the API key, replace the existing API key in the code:

python
api_key = "your_openrouteservice_api_key_here"


### Notes:
- The OpenRouteService API will return the route distance, geometry, and other details.
- The project will use this data to divide the route into segments and calculate fuel stops.



## Project Structure

The project is structured as follows:


fuel/
│
├── migrations/               # Database migrations
├── models.py                 # Models for fuel stops
├── views.py                  # Logic for route optimization
├── urls.py                   # URL routing for views
└── admin.py                  # Admin panel configuration




## What We Did

1. Created a `FuelStop` model: This model stores information about each fuel stop, including the name, city, state, and price per gallon.

2. Implemented Route Optimization: The logic to fetch the route from the OpenRouteService API, divide it into 500-mile segments, and calculate fuel stops along the route was implemented in the `RouteOptimizationView` class.

3. Admin Panel Integration: We set up Django's admin panel to allow easy management of fuel stops.

4. API Testing: We ensured the API provides accurate responses with fuel stop details and calculates the optimal fuel cost.



## Troubleshooting

- If the route calculation fails, ensure that your OpenRouteService API key is valid.
- Ensure that the API rate limits are not exceeded.
- If you encounter a `"Failed to fetch the route from the API"` error, check the API request logs to see the exact issue (e.g., invalid coordinates, API quota exceeded, etc.).



## Future Enhancements

1. Improved Fuel Stop Matching: Currently, fuel stops are selected based on proximity to route segments and price. This can be improved by using better geospatial algorithms.
2. User Authentication: Integrate user authentication to allow users to create their own fuel stop databases.
3. Data Analysis: Add more data analysis and optimization techniques to find the best fuel stops.