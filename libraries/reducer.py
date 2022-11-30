def increment(state,key,val):
    return {key:int(state[key]) + int(val)}
def decrement(state,key,val):
    return {key:int(state[key]) - int(val)}
def newkey(state,key,val):
    return {key:val}
def thursday(state,key,val):
    return "thursday"
def friday(state,key,val):
    return "friday"
def saturday(state,key,val):
    return "saturday"
def sunday(state,key,val):
    return "sunday"
def default(state,key,val):
    return state

switcher = {
    "INCREMENT": increment,
    "DECREMENT": decrement,
    "NEWKEY": newkey,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(method,state,key,val):
    return switcher.get(method, default)(state,key,val)

#print(switch("NEWKEY",{"one":20,"two":2}, "dupa", {"Kupa":[1,2,3]}))