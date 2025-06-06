*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://testautomationpractice.blogspot.com/

*** Test Cases ***
Launch_Browser
    Open Browser    ${URL}    browser=chrome
    #Maximize Browser Window
    Sleep    2s
    ${title}    Get Title
    Log To Console    ${title}
    Should Be Equal As Strings    ${title}    Automation Testing Practice
    Close Browser