*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${base_url}    https://reqres.in
${UserNum}    2

*** Test Cases ***
Get_UsersInfo
    create session     mysession    ${base_url}
    ${response}=    get request    mysession    /api/users/${UserNum}

    log to console    ${response.status_code}
    log to console    ${response.content}
    log to console    ${response.headers}

    #Validations

    ${status_code}=    convert to string    ${response.status_code}
    should be equal    ${status_code}    200

    ${status_content}=    convert to string    ${response.content}
    should contain    ${status_content}    Janet

    ${connection}    get from dictionary    ${response.headers}    Connection
    should be equal    ${connection}    keep-alive
