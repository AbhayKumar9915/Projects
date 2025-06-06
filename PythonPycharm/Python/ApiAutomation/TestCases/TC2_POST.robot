*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${base_url}    https://reqres.in

*** Test Cases ***
Put_UsersInfo
    create session    mysession    ${base_url}
    ${body}=    create dictionary    name=Abhay job=leader
    ${header}=    create dictionary    Content-Type=application/json
    ${response}=    post request    mysession    /api/users    data=${body}    headers=${header}

    log to console    ${response.status_code}
    log to console    ${response.content}

    #Validations

    ${status_code}=    convert to string    ${response.status_code}
    should be equal    ${status_code}    201

    ${res_body}=    convert to string    ${response.content}
    should contain    ${res_body}    id


