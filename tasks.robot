*** Settings ***
Documentation       Template robot main suite.

Library             Collections
Library             RoboRedux
Library             RPA.FileSystem
Resource            keywords.robot
Variables           MyVariables.py


*** Variables ***
${my_variable}      ${{ round(random.random()) }}

*** Test Cases ***
Example
    Log to console    Executing!
    ${dict}=    Create Dictionary    key=key    counter=1
    createState    ${dict}

    ${newkey}=    Create Dictionary    dupa="Dupa"

    Dispatch Action    INCREMENT
    Dispatch Action    INCREMENT
    Dispatch Action    INCREMENT
    Dispatch Action    DECREMENT
    Dispatch Action    NEWKEY    ${newkey}
    #${xxx}=    getState
    #dispatch    name=NEWKEY    payload={"dupa":"dupa"}
    #dispatch    type=INCREMENT    one=2
    ${xxx}=    getState
    Log    ${STORE}

*** Keywords ***
Dispatch Action
    [Arguments]    ${name}    ${payload}={}
    &{action}=    Create Dictionary    name=${name}    payload=${payload}
    dispatch    ${action}

