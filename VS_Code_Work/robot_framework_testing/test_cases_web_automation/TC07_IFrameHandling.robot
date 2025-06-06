*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      	https://demo.automationtesting.in/Frames.html

*** Test Cases ***
To Perform To handle IFrame
    Launch Browser

    #Signle Frame
    Sleep   2s
    Select Frame     SingleFrame
    Input Text   xpath=//input[@type='text']    Abhay
    Sleep   time_=2s
    Unselect Frame

    #Multiple Frame
    Click Element    xpath=//a[contains(text(),'Iframe with in an Iframe')]
    Sleep   2s
    Select Frame     xpath=//iframe[@src='MultipleFrames.html']
    Select Frame    xpath=/html/body/section/div/div/iframe
    Input Text   xpath=//input[@type='text']    Akshita
    Sleep    2s
    unselect frame
    Close All Browsers


*** Keywords ***
Launch Browser
    Open Browser     ${url}     ${browser}
    Maximize Browser Window


