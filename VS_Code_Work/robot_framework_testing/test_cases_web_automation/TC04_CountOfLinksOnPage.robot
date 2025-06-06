*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${browser}      chrome
${url}      https://google.com


*** Test Cases ***
Get All Links form Website
     Launch_Browser
     ${LinkCount}=  Get Element Count  xpath://a
     log to console     ${LinkCount}

     @{items}   Create List
     FOR    ${i}    IN RANGE    1   ${LinkCount}+1
         ${linkText}=   Get Text    xpath:(//a)[${i}]
         log to console  ${linkText}
     END
     Close All Browsers


*** Keywords ***
Launch_Browser
    Open Browser     ${url}     ${browser}
    Maximize Browser Window
