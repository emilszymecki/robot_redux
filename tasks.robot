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
    ${dict}=    Create Dictionary    key=key    one=1
    createState    ${dict}
    #${xxx}=    getState
    dispatch    method=INCREMENT    key=one    val=2
    dispatch    method=NEWKEY    key=random    val=${my_variable}
    #dispatch    type=INCREMENT    one=2
    ${xxx}=    getState
    Log    ${STORE}

