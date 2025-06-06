*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}      chrome
${url}      http://testautomationpractice.blogspot.com/


*** Test Cases ***
To_Handle_Alert
    Launch_Browser
    Click Element    id=alertBtn
    sleep   2
    #Verifies that an alert is present and by default, accepts it
    Alert Should Be Present     I am an alert box!
    Click Element    id=confirmBtn
    Handle Alert    timeout=5    action=dismiss
    Sleep    2
    Click Button    id=promptBtn
    Input Text Into Alert    text=Hello Abhay!    timeout=10    action=accept
    Sleep    2
    Close Browser


*** Keywords ***
Launch_Browser
    Open Browser     ${url}     ${browser}
    Maximize Browser Window


