*** Test Cases ***
TC001_For_Loop_Continue
    FOR    ${i}    IN RANGE    6
        IF    ${i} == 4
            CONTINUE
        END
        Log To Console    ${i}
    END


TC002_For_Loop_Break
    FOR    ${i}    IN RANGE    1    6
        IF    ${i} == 4
            BREAK
        END
        Log To Console    ${i}
    END


TC003_For_Loop_Pass
    FOR    ${i}    IN RANGE    5
            Pass Execution If    ${i} == 3   ${i} is 3
        Log To Console    ${i}
    END

    
TC004_For_Loop_Nested
    FOR    ${i}    IN RANGE    5
        FOR    ${j}    IN RANGE    5
            Log Many    ${i}    ${j}
        END
    END


TC005_For_Loop_With_Step
    FOR    ${i}    IN RANGE    1    6    2
        Log To Console    ${i}
    END


TC006_For_Loop_With_Step_Negative
    FOR    ${i}    IN RANGE    6    1    -1
        Log To Console    ${i}
    END


TC007_While_Loop
    ${i}=    Set Variable    1
    WHILE    ${i} < 6
        Log To Console    ${i}
        ${i}=    Evaluate    ${i} + 1
    END


TC008_While_Loop_With_Break
    ${i}=    Set Variable    5
    WHILE    ${i} > 0
        Log To Console    ${i}
        ${i}=    Evaluate    ${i} - 1
        IF    ${i} == 3
            BREAK
        END
    END


TC009_For_Loop_Sum
    ${total}=    Set Variable    0
    FOR    ${i}    IN RANGE    1    6
        ${total}=    Evaluate    ${total} + ${i}
        Log To Console    ${total}
    END
    

