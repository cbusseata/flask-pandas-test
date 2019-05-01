# treetop-test

## Running the test

### Prerequisites
* [docker](https://docs.docker.com/v17.09/engine/installation/)
* [docker-compose](https://docs.docker.com/compose/install/)

### Starting up the container
To start up the container:
````bash
make
````

Once up and running, it will stream logs from the app.  You can use CTL+C to get out of it.

To start the container without viewing logs:
````bash
make up
````

Once up, the API will be available at http://0.0.0.0:5000

To stop the container:
````bash
make down
````

### API testing

#### Automated testing with Robot

You can run the automated test scripts (there's only a couple, it's a demo) by following these steps:

Entering the app container:
````bash
make enter
````
and enter "app" when prompted.

Then issue the following command to run the robot tests:
````bash
tests/acceptance/robot.sh
````

#### Manual testing with Postman

You can use the Postman collection in `docs/TreeTop-Test.postman_collection.json`.

The endpoints are:
http://0.0.0.0:5000/test - general test endpoint just to make sure the API is up
http://0.0.0.0:5000/organization/1 - get data for a single organization
http://0.0.0.0:5000/organizations - get data for all or a subset of organizations

Note that the accepted parameter names are the same as in the instruction sheet, but all lower-case (matches the CSV this way).

## Things I would improve or add if I had more time

1.  Provide a swagger file, documenting the API
2.  Break the code into modules with classes for working with the pandas dataframe.  This way I could unit test the filtering.
3.  Unit tests.
4.  More automated API testing.  I added a couple using the robot framework to demonstrate, but it needs more coverage.
5.  Provide more detailed error responses in case of invalid request parameters.
6.  Consider using the CSV to seed a database, rather than just accessing it directly.
7.  Deploy to AWS.
8.  Secure the API with an API key or an IP whitelist, or both.