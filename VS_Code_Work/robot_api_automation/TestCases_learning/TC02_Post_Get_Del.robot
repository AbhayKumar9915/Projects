*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${Base_url}    https://thetestingworldapi.com/
${ID_01}

*** Test Cases ***
TC001_Post_Request
    Create Session    Post_Student_Details    ${Base_url}
    &{body}    Create Dictionary    first_name=Abhay    middle_name=Kumar    last_name=Verma    date_of_birth=1994-12-25
    #${headers}    Create Dictionary    Content-Type=application/json
    ${response}    POST On Session    Post_Student_Details    api/studentsDetails    data=${body}
    Log To Console    ${response.status_code}
    Should Be Equal As Integers    ${response.status_code}    201
    Log To Console    ${response.content}
    # Validating one of key from dictonary
    Dictionary Should Contain Key    ${response.json()}    first_name
    # Validating one of value from dictonary
    Dictionary Should Contain Value    ${response.json()}    Abhay

TC002_Get_Request
    Create Session    Get_Student_Details    ${Base_url}
    ${response}    GET On Session  Get_Student_Details    url=api/studentsDetails
    Log To Console    ${response.status_code}
    Should Be Equal As Integers    ${response.status_code}    200
    ${value}    Get Dictionary Values    ${response.json()}[0]
    ${ID}=    Get From List    index=2    list_=${value}
    Set Global Variable    ${ID_01}    ${ID}
    Log To Console    ${ID}

#This works only if run with TC002 due to global variable
TC003_Delete_Request
    Log To Console    ${ID_01}
    Create Session    Delete_Student_Details    ${Base_url}
    ${response}    DELETE On Session    Delete_Student_Details    api/studentsDetails/${ID_01}
    Log To Console    ${response.status_code}
    Should Be Equal As Integers    ${response.status_code}    200

    