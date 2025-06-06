*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Handle Browser Windows
    Open Browser     http://demo.automationtesting.in/Windows.html    chrome    alias=Window1
    Maximize Browser Window


    sleep   2
    Open Browser     https://www.selenium.dev/selenium/docs/api/java/index    chrome    alias=Window2
    #Maximize Browser Window

    Switch Browser    index_or_alias=Window1
    Click Element    xpath=//*[@id="header"]/nav/div/div[2]/ul/li[2]/a 
    ${title}=       Get Title
    log to console      ${title}
    
    Sleep   2
    #Switch to the second window
    Switch Browser      index_or_alias=Window2
    ${title}=       Get Title
    log to console      ${title}
    Sleep   2
    Close All Browsers



