*** Settings ***
Library    SeleniumLibrary
Variables    locators.py


*** Variables ***
${url}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${username}    Admin
${password}    admin123


*** Keywords ***
login
    #[Arguments]    ${username}    ${password}
    Open Browser    ${url}    service_log_path=${{os.path.devnull}}
    Maximize Browser Window
    #Sleep    2
    #Capture Page Screenshot
    Wait Until Element Is Visible    locator=${login_logo_xpath}    timeout=5s
    Input Text    ${username_xpath}    ${username}
    Input Password    ${password_xpath}    ${password}
    Click Button    locator=${login_button_xpath}
    Sleep    5s
    Set Screenshot Directory    path=Screenshots
    Capture Page Screenshot  


logout  
    Click Element    ${dropdown_xpath}
    Click Element    ${logout_btn_xpath}
    Sleep    3s
    Capture Page Screenshot
    Close Browser

    


