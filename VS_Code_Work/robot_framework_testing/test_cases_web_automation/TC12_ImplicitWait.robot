*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      https://testautomationpractice.blogspot.com/

*** Test Cases ***
To Perform Select Option with Drop Down list

    Launch Browser
    ${implicit}=        Get Selenium Implicit Wait  #Default time is 0 (zero)
    log to console      ${implicit}

    Set Selenium Implicit Wait    10 seconds

    Wait Until Page Contains    Automation Testing Practice  # defult time is 5 second
    Select From List By Label   id=country       Australia
    Select From List By Index   id=country       1

    Select From List By Label   id=animals       Lion
    Select From List By Label   id=animals       Dog

    ${implicit}=        Get Selenium Implicit Wait
    log to console      ${implicit}

    Close All Browsers


*** Keywords ***
Launch Browser
    Open Browser     ${url}     ${browser}
    Maximize Browser Window


