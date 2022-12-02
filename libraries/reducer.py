def increment(state,payload):
    return {**state,"counter":int(state["counter"]) + 1 }
def decrement(state,payload):
    return {**state,"counter":int(state["counter"]) - 1 }
def newkey(state,payload):
    return {**state,**payload}
def default(state,key,val):
    return state

switcher = {
    "INCREMENT": increment,
    "DECREMENT": decrement,
    "NEWKEY": newkey,
    }

def reducer(state,action):
    #print(state,action["name"],action["payload"])
    return switcher.get(action["name"], default)(state,action["payload"])

#print(reducer("NEWKEY",{"one":20,"two":2}, "dupa", {"Kupa":[1,2,3]}))

testObj = {"counter":1,"two":"two"}
testPayload = {"name":"NEWKEY","payload":{"dupa":"dupa"}}
testInc = {"name":"INCREMENT","payload":{}}
testDec = {"name":"DECREMENT","payload":{}}
#print(reducer(testObj,testPayload))
#print(reducer(testObj,testInc))
#print(reducer(testObj,testDec))
