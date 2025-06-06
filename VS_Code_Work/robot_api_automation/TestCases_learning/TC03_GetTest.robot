*** Settings ***
Library    RequestsLibrary


*** Variables ***
${BASE_URL}    https://reqres.in/
${ID}    2


*** Test Cases ***
TC01_GetTest
    Create Session    reqres    ${BASE_URL}
    ${response1}    GET On Session    reqres    api/users/${ID}
    Log To Console    ${response1.status_code}
    #Log To Console    ${response1.json()}
    Log To Console    ${response1.content}
    Should Be Equal As Strings    ${response1.status_code}    200
    Should Be Equal As Strings    ${response1.json()['data']['id']}    ${ID}