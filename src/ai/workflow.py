from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
from ai.states import WorkFlowState

class WorkFlow:
    def __init__(self):
        self.workflow = StateGraph(WorkFlowState)

    def build(self):
        pass

