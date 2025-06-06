*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      http://demo.automationtesting.in/Windows.html

*** Test Cases ***
Handle Tabbed Windows

    Launch Browser
    Click Element    xpath://*[@id="Tabbed"]/a/button
    Switch Window    Selenium
    sleep   2
    Click Element   xpath=//span[contains(text(),'Downloads')]
    sleep   3
    Close All Browsers



*** Keywords ***
Launch Browser
    Open Browser     ${url}     ${browser}
    Maximize Browser Window


