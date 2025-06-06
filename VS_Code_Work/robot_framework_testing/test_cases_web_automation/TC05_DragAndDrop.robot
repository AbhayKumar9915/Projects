*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      http://testautomationpractice.blogspot.com/

*** Test Cases ***
To Perform Drag and Drop
    Launch Browser
    drag and drop      id:draggable       id:droppable
    sleep    8

    Close All Browsers

*** Keywords ***
Launch Browser
    Open Browser     ${url}     ${browser}
    Maximize Browser Window


