*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      https://testautomationpractice.blogspot.com/

*** Test Cases ***
To Perform Select Option with Drop Down list
    Lunch Browser
    Scroll Element Into View    locator=//*[contains(text(),'Slider')]
    Drag And Drop    locator=id=draggable    target=id=droppable
    Sleep    time_=1s
    Scroll Element Into View    locator=//*[contains(text(),'SVG Elements')]
    Click Element At Coordinates    locator=xpath=(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]    xoffset=100    yoffset=0
    Sleep    time_=1s
    Close Browser


*** Keywords ***
Lunch Browser
    Open Browser     ${url}     ${browser}
    Maximize Browser Window
    Set Selenium Speed    1s

