*** Settings ***
Library    JSONLibrary
Library    os
Library    Collections

*** Test Cases ***
Testcase1:
    ${json_obj}=    load json from file    C:/Users/ab1kumar/VS_Code_Work/robot_api_automation/TestData/JsonTest.json
    ${name_val}=    get value from json    ${json_obj}    $.firstName
    log to console    ${name_val}
    should be equal    ${name_val[0]}    John

    ${street_address}=    get value from json    ${json_obj}    $.address.streetAddress
    should be equal    ${street_address[0]}    naist street

    ${phone_type}=    get value from json    ${json_obj}    $.phoneNumbers[0].type
    should be equal   ${phone_type[0]}    iPhone