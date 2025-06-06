*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${base_url}    http://localhost:8080

*** Test Cases ***
TC1_GET:Return all the videos games from DB
    create session    mysession    ${base_url}
    ${response}=    get request    mysession    app/videogames
    log to console    ${response.status_code}
    log to console    ${response.content}
    #Validations
    ${status_code}=    convert to string    ${response.status_code}
    should be equal    ${status_code}    200

TC2_POST:Add a new video game in DB
    create session    mysession    ${base_url}
    ${body}=    create dictionary    id=11    name=Grand Theft Auto V   releaseDate=2001-04-23   reviewScore=90    category=Driving     rating=Mature
    ${header}=    create dictionary    Content-Type=application/json
    ${response}=    post request    mysession    app/videogames    data=${body}    headers=${header}
    log to console    ${response.status_code}
    log to console    ${response.content}
    #Validations
    ${status_code}=    convert to string    ${response.status_code}
    should be equal    ${status_code}    200
    ${res_body}=    convert to string    ${response.content}
    should contain    ${res_body}    Record Added Successfully

TC3_GET:Returns the details of a single game by ID
    create session    mysession    ${base_url}
    ${response}=    get request    mysession    app/videogames/11
    log to console    ${response.status_code}
    log to console    ${response.content}
    #Validations
    ${status_code}=    convert to string    ${response.status_code}
    should be equal    ${status_code}    200
    ${res_body}=    convert to string    ${response.content}
    should contain    ${res_body}    Grand Theft Auto V

TC4_PUT:Update an existing video game record in the DB
    create session    mysession    ${base_url}
    ${body}=    create dictionary    id=11    name=PUBG   releaseDate=2001-04-23   reviewScore=90    category=Action     rating=Mature
    ${header}=    create dictionary    Content-Type=application/json
    ${response}=    put request    mysession    app/videogames/11    data=${body}    headers=${header}
    log to console    ${response.status_code}
    log to console    ${response.content}
    #Validations
    ${status_code}=    convert to string    ${response.status_code}
    should be equal    ${status_code}    200
    ${res_body}=    convert to string    ${response.content}
    should contain    ${res_body}    PUBG


TC5_DELETE:Delete a video game from DB
    create session    mysession    ${base_url}
    ${response}=    delete request    mysession    app/videogames/11
    log to console    ${response.status_code}
    log to console    ${response.content}
    #Validations
    ${status_code}=    convert to string    ${response.status_code}
    should be equal    ${status_code}    200
    ${res_body}=    convert to string    ${response.content}
    should contain    ${res_body}    Record Deleted Successfully
