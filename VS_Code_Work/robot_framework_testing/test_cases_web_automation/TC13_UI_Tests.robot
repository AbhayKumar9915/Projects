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
    #Close Browser


Alert_Handling
    #Open Browser    ${URL}    browser=chrome
    Sleep    2s
    Click Element    id=alertBtn
    Sleep    2s
    Alert Should Be Present
    Sleep    2s
    Click Element    id=promptBtn
    Input Text Into Alert    Hello World!!!!!
    Sleep    5s
    #Close All Browsers


Window_Handling
    #Open Browser    ${URL}    browser=chrome
    Click Button    xpath=//button[contains(text(),'New Tab')]
    Sleep    2s
    Switch Window    title=SDET-QA Blog
    ${title}    Get Title
    Log To Console    ${title}
    Should Be Equal As Strings    ${title}    SDET-QA Blog
    Click Element    xpath=//a[contains(text(),'Manual Testing Materials')]
    Sleep    2s
    Switch Window    title=Automation Testing Practice
    #Close All Browsers


Mouse_Hover
    #Open Browser    url=${URL}    browser=chrome
    Scroll Element Into View    locator=//button[contains(text(),'Copy Text')]
    Sleep    2s
    Mouse Over    locator=//button[@class='dropbtn']
    Sleep    2s
    #Close All Browsers


Double_Click
    #Open Browser    url=${URL}    browser=chrome
    Scroll Element Into View    locator=//button[contains(text(),'Copy Text')]
    Double Click Element    locator=//button[contains(text(),'Copy Text')]
    Sleep    time_=2s
    #Close Browser


Drag_Drop_Slider
    #Open Browser    ${URL}    browser=chrome
    Scroll Element Into View    locator=//*[contains(text(),'Slider')]
    Drag And Drop    locator=id=draggable    target=id=droppable
    Sleep    time_=2s
    Scroll Element Into View    locator=//*[contains(text(),'SVG Elements')]
    Click Element At Coordinates    locator=xpath=(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]    xoffset=100    yoffset=0
    Sleep    time_=2s
    Close Browser

