*** Settings ***
Library    SeleniumLibrary
Library    JSONLibrary


*** Variables ***
${url}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${url_02}    https://demo.automationtesting.in/Register.html


*** Test Cases ***
Launch_Browser
    Open Browser    ${url}    browser=Firefox
    Maximize Browser Window
    Sleep    2s
    Get Window Names
    ${title}    Get Title
    Should Be Equal    ${title}    OrangeHRM
    Close Browser
    #Close Window


Radio_Btn_Checkbox
    Open Browser    url=${url_02}    browser=chrome
    Select Radio Button    value=Male    group_name=radiooptions
    Set Screenshot Directory    path=Screenshots
    #Capture Page Screenshot
    Sleep    2s
    Select Radio Button    value=FeMale    group_name=radiooptions
    #Capture Page Screenshot
    Select Checkbox    xpath=//input[@value='Cricket']
    Select Checkbox    xpath=//input[@value='Hockey']
    Checkbox Should Be Selected    xpath=//input[@value='Cricket']
    Unselect Checkbox    xpath=//input[@value='Cricket']
    Close Browser


Handling_Dropdown
    Open Browser    ${url_02}    browser=chrome
    Maximize Browser Window
    Select From List By Index    xpath=//select[@id='Skills']    3
    Sleep    2s
    Select From List By Value    xpath=//select[@id='Skills']    Android
    Sleep    2s
    Select From List By Value    xpath=//select[@id='Skills']    CSS
    Close Browser