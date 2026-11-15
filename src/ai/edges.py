from typing import Literal
from langgraph.graph import END
from ai.states import WorkFlowState

ContinueGatheringRequirementsType = Literal["GATHER_REQUIREMENTS", "ALL_REQUIREMENTS"]
AINextStepForAllRequirementsAfterHumanFeedbackType = Literal["ALL_REQUIREMENTS", "FUNCTIONAL_REQUIREMENTS"]
AINextStepForFunctionalRequirementsAfterHumanFeedbackType = Literal["NON_FUNCTIONAL_REQUIREMENTS", "FUNCTIONAL_REQUIREMENTS"]
AINextStepForNonFunctionalRequirementsAfterHumanFeedbackType = Literal["NON_FUNCTIONAL_REQUIREMENTS", "BACK_OF_THE_ENVELOPE_CALCULATION"]
AINextStepForBackOfTheEnvelopeCalculationAfterHumanFeedbackType = Literal["BACK_OF_THE_ENVELOPE_CALCULATION", "API_DESIGN"]
AINextStepForApiDesignAfterHumanFeedbackType = Literal["API_DESIGN", "DATA_MODEL"]
AINextStepForDataModelAfterHumanFeedbackType = Literal["DATA_MODEL", "DESIGN_OVERVIEW"]
AINextStepForDesignOverviewAfterHumanFeedbackType = Literal["DESIGN_OVERVIEW", "DIAGRAM_CODE"]
AINextStepForDiagramCodeAfterHumanFeedbackType = Literal["DIAGRAM_CODE", "__end__"]

def continue_gathering_requirements(state: WorkFlowState) -> ContinueGatheringRequirementsType:
    if state.gathering_requirements_loop:
        return "GATHER_REQUIREMENTS"
    return "ALL_REQUIREMENTS"

def ai_next_step_for_all_requirements_after_human_feedback(state: WorkFlowState) -> AINextStepForAllRequirementsAfterHumanFeedbackType:
    if state.ai_next_step_for_human_feedback_for_all_requirements == "MOVE_TO_NEXT_STEP":
        return "FUNCTIONAL_REQUIREMENTS"
    return "ALL_REQUIREMENTS"

def ai_next_step_for_functional_requirements_after_human_feedback(state: WorkFlowState) -> AINextStepForFunctionalRequirementsAfterHumanFeedbackType:
    if state.ai_next_step_for_human_feedback_for_functional_requirements == "MOVE_TO_NEXT_STEP":
        return "NON_FUNCTIONAL_REQUIREMENTS"
    return "FUNCTIONAL_REQUIREMENTS"

def ai_next_step_for_non_functional_requirements_after_human_feedback(state: WorkFlowState) -> AINextStepForNonFunctionalRequirementsAfterHumanFeedbackType:
    if state.ai_next_step_for_human_feedback_for_non_functional_requirements == "MOVE_TO_NEXT_STEP":
        return "BACK_OF_THE_ENVELOPE_CALCULATION"
    return "NON_FUNCTIONAL_REQUIREMENTS"

def ai_next_step_for_back_of_the_envelope_calculation_after_human_feedback(state: WorkFlowState) -> AINextStepForBackOfTheEnvelopeCalculationAfterHumanFeedbackType:
    if state.ai_next_step_for_human_feedback_for_back_of_the_envelope_calculation == "MOVE_TO_NEXT_STEP":
        return "API_DESIGN"
    return "BACK_OF_THE_ENVELOPE_CALCULATION"

def ai_next_step_for_api_design_after_human_feedback(state: WorkFlowState) -> AINextStepForApiDesignAfterHumanFeedbackType:
    if state.ai_next_step_for_human_feedback_for_api_design == "MOVE_TO_NEXT_STEP":
        return "DATA_MODEL"
    return "API_DESIGN"

def ai_next_step_for_data_model_after_human_feedback(state: WorkFlowState) -> AINextStepForDataModelAfterHumanFeedbackType:
    if state.ai_next_step_for_human_feedback_for_data_model == "MOVE_TO_NEXT_STEP":
        return "DESIGN_OVERVIEW"
    return "DATA_MODEL"

def ai_next_step_for_design_overview_after_human_feedback(state: WorkFlowState) -> AINextStepForDesignOverviewAfterHumanFeedbackType:
    if state.ai_next_step_for_human_feedback_for_design_overview == "MOVE_TO_NEXT_STEP":
        return "DIAGRAM_CODE"
    return "DESIGN_OVERVIEW"

def ai_next_step_for_diagram_code_after_human_feedback(state: WorkFlowState) -> str:
    if state.ai_next_step_for_human_feedback_for_diagram_code == "MOVE_TO_NEXT_STEP":
        return END
    return "DIAGRAM_CODE"
