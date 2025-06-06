*** Settings ***
Library    String


*** Variables ***
${string_name}    Abhayadcadada
&{dict}


*** Keywords ***
Reverse String
    [Arguments]    ${string}
    ${reversed_string}=    Evaluate    ''.join(reversed('${string}'))
    RETURN    ${reversed_string}


*** Test Cases ***
Reversed_String
    ${reversed_string}=    Reverse String    ${string_name}
    Log To Console    "Reversed string is: ${reversed_string}"


Total_Count_of_Char
    # Split String to Characters and count the total number of characters
    ${string_name}=    Split String To Characters    ${string_name}
    # Using @ with variable string_name to get the list of characters
    # @ is used for list variables.
    Log Many    @{string_name}
    ${count}=    Set Variable    0
    FOR    ${i}    IN    @{string_name}
        ${count}=    Evaluate    ${count} + 1
    END
    Log To Console    Count using for loop: ${count}
    # Using String Library
    ${count}=    Get Length    ${string_name}
    Log To Console    Count using pre-defined method: ${count}
    

Count_Each_Char
    ${string_name}=    Split String To Characters    ${string_name}
    ${count}=    Set Variable    0
    FOR    ${ch}    IN    @{string_name}
        ${count}=    Get Count    ${string_name}    ${ch} 
        Log To Console    '${ch}' ocuurance in string: ${count} 
        Create Dictionary    &{dict}    ${ch}=${count}
        Log Many    ${ch}    ${count}
    END
    

If_Conditin 
    ${count}=    Set Variable    1
    IF    ${count} == 0
        Pass Execution    message=This is a pass message
    ELSE IF    ${count} == 1
        Log To Console    "Count is 1"
    ELSE
        Log To Console    "Count is greater than 1"
        
    END

    
    
    
    
    