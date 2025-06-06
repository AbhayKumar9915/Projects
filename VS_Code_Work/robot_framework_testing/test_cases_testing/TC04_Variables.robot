*** Variables ***
${my_var}    single_valriable
@{my_list}    apple    banana    orange    21
&{my_dict}    name=abhay    age=32


*** Test Cases ***
Test_Variables
    Log To Console   ${my_var}
    #List Operations
    Log To Console   ${my_list}
    Log To Console   Indexed list: ${my_list}[2]
    Log To Console   **** Printing List ****
    FOR    ${i}    IN    @{my_list}
        Log To Console    ${i}    
    END

    #Dictionary Operations
    Log To Console   **** Printing Dictonary ****
    Log To Console   ${my_dict}
    Log To Console   ${my_dict}[name]
    FOR    ${key}    ${value}    IN    &{my_dict}
        Log Many    ${key}    ${value}    
    END
    My_Keyword


Log_Multiple_Values
    Log Many    @{my_list}


*** Keywords ***
My_Keyword
    Log Many    ${my_var}    ${my_list}    ${my_dict}
    
    


