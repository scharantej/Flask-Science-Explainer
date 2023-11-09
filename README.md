 ## Problem Analysis

The problem is to build a science explainer and come up with the design for a Flask application. The application should include the HTML files needed for the application along with different routes.

## Design

The application will have the following HTML files:

* `index.html`: This will be the home page of the application. It will contain a brief introduction to the application and links to the different sections.
* `science_explainer.html`: This will be the main page of the application. It will contain the different science explainers.
* `about.html`: This will contain information about the application and its developers.
* `contact.html`: This will contain contact information for the developers.

The application will have the following routes:

* `/`: This will redirect to the home page.
* `/science_explainer`: This will render the science explainer page.
* `/about`: This will render the about page.
* `/contact`: This will render the contact page.

## Implementation

The application can be implemented using the following steps:

1. Create a new Flask application.
2. Create the HTML files for the application.
3. Create the routes for the application.
4. Run the application.

## Testing

The application can be tested by visiting the different routes in a web browser. The application should render the correct HTML pages for each route.

## Deployment

The application can be deployed to a production server using a WSGI server such as Gunicorn or uWSGI.