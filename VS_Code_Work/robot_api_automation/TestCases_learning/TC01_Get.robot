*** Settings ***
Library    RequestsLibrary


*** Variables ***
${Base_url_01}    https://thetestingworldapi.com/
${Student_ID}    10523326
${Base_Url_02}    https://reqres.in/


*** Test Cases ***
TC001_Get_Request
    Create Session    Get_Student_Details    ${Base_url_01}
    ${response}    GET On Session  Get_Student_Details    url=api/studentsDetails/${Student_ID}
    Log To Console    ${response.status_code}
    Should Be Equal As Integers    ${response.status_code}    200
    #Log To Console    ${response.content}


TC002_Get_Request
    Create Session    User_Details    ${Base_Url_02}
    ${response}    GET On Session    User_Details    url=/api/users/2             
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}  
    should contain    ${response.content}    janet    