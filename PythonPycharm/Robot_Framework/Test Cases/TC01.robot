*** Variables ***
${my_var}    single_valriable
@{my_list}    apple    banana    orange    21
&{my_dict}    name=abhay    age=32
${my_var}    single_valriable
@{my_list}    apple    banana    orange    21
&{my_dict}    name=abhay    age=32

*** Test Cases ***
Test_TC01
    ${i}=   Set Variable    1
    WHILE   ${i} < 5
        Log To Console  ${i}
        ${i}=   Evaluate    ${1} + 1
    END

