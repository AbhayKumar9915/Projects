*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/login_resources.robot
Library    DataDriver    ../test_data/LoginData.xlsx    sheet_name=Sheet1

Suite Setup  Setup    ${url}    ${browser}
Suite Teardown  closer
Test Template  Invalid Login


*** Variables ***
${browser}   chrome
${url}      https://admin-demo.nopcommerce.com/


*** Test Cases ***
Login Test Case From Excel Sheet    Default    UserData

*** Keywords ***
Invalid Login
    [Arguments]  ${username}    ${password}
    Input UserName      ${username}
    Input Password      ${password}
    Click To Login Button
    Error Message Should Be Visible







