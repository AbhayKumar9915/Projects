*** Settings ***
Documentation    Tests to verify that account succeed and fail correctly.
Library  SeleniumLibrary


*** Variables ***
${browser}   chrome
${url}      https://demo.automationtesting.in/Register.html


*** Test Cases ***
Validate_Check_box_and_Radio_buttons
    Open Browser  ${url}    ${browser}
    Maximize Browser Window
    Set Selenium Speed  2second

    Select Radio Button     radiooptions     Male
    Select Radio Button    group_name=radiooptions    value=FeMale

    Select Checkbox    locator=id=checkbox1
    Unselect Checkbox    locator=id=checkbox1
    Close All Browsers



