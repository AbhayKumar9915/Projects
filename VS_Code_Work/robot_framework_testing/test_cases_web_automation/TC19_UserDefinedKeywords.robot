*** Settings ***
Documentation    Tests to verify that account succeed and fail correctly.
Library  SeleniumLibrary
Resource  ../resources/project_resource.robot

*** Variables ***
${browser}   chrome
${url}      https://admin-demo.nopcommerce.com/

*** Test Cases ***
Login With Valid Credentials

    ${title}=     Setup    ${url}    ${browser}
    log to console    ${title}

    Title Should Be  nopCommerce demo store. Login
    ${"username_input"}  set variable     id:Email

    Element Should Be Visible   ${"username_input"}
    Element Should Be Enabled     ${"username_input"}
    input text  id:Email    admin@yourstore.com
    sleep   2
    Clear Element Text    ${"username_input"}
    sleep    2

    closer