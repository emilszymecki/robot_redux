from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from reducer import *

class RoboRedux:
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self):
        self.store = {"state":{},"listeners":[logger.console,logger.info]}

    def getState(self):
        BuiltIn().set_suite_variable('${STORE}',self.store)
        return self.store

    def createState(self,initialState):
        self.store["state"] = initialState

    def dispatch(self,method,key,val):
        #action_val = {key:self.store["state"][key] + val} if method == "INCREMENT" else self.store["state"]
        action_val = switch(method,self.store["state"],key,val)
        #logger.info("actionLogger")
        #logger.info(action_val)
        self.store["state"] = {**self.store["state"],**action_val}
        #logger.info(switch(method,self.store["state"],key,val))
        for listener in self.store["listeners"]:
            listener(self.store["state"])
