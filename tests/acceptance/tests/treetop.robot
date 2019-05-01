*** Settings ***
Documentation  This is an automated test script using the robot framework.
Library  REST  http://0.0.0.0:5000

*** Test Cases ***
Get organization
    [Documentation]  We are retrieving one organization.
    GET  /organization/1
    Integer  response status                200
    Integer  response body id               1
    String   response body category         "Non-Profit"
    String   response body name             "Michigan Science Center"
    Integer  response body postal           48202
    String   response body state            "MI"

Get organizations with invalid state
    [Documentation]  We are trying to get organizations with an invalid state.
    GET  /organizations?state=pineapple
    Integer  response status        400
    String  response body error     'pineapple' does not match '^[A-Z]{2}$'
