*** Settings ***
Library    Collections
#Library    BuiltIn


*** Variables ***


*** Keywords ***
Add
    [Arguments]    ${a}    ${b}
    ${result}=    Evaluate    ${a} + ${b}
    RETURN    ${result}

Multiply
    [Arguments]    ${a}    ${b}
    ${result}=    Evaluate    ${a} * ${b}
    RETURN    ${result}

Add Numbers
    [Arguments]    ${a}    ${b}
    ${c}=    Add    ${a}    ${b}
    RETURN    ${c}
 
Multiply Numbers
    [Arguments]    ${a}    ${b}
    ${result}=    Add Numbers    ${a}    ${b}
    ${c}=    Multiply    ${result}    ${b}
    RETURN    ${c}
 
*** Test Cases ***
 
Example Test Case
    ${result}=    Multiply Numbers    2    3
    Should Be Equal As Integers    ${result}     15