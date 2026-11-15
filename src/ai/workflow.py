from langgraph.graph import StateGraph, START, END
from IPython.display import Image
from ai.states import WorkFlowState
from ai.nodes import (
    gather_requirements,
    get_human_response_from_gather_requirements,
    get_all_requirements,
    human_approval_all_requirements,
    interpret_human_response_for_all_requirements,
    generate_functional_requirements,
    human_approval_for_functional_requirements,
    interpret_human_response_for_functional_requirements,
    generate_non_functional_requirements,
    human_approval_for_non_functional_requirements,
    interpret_human_response_for_non_functional_requirements,
    generate_back_of_the_envelope_calculation,
    human_approval_for_back_of_the_envelope_calculation,
    interpret_human_response_for_back_of_the_envelope_calculation,
    generate_api_design,
    human_approval_for_api_design,
    interpret_human_response_for_api_design,
    generate_data_model,
    human_approval_for_data_model,
    interpret_human_response_for_data_model,
    generate_design_overview,
    human_approval_for_design_overview,
    interpret_human_response_for_design_overview,
    generate_diagram_code,
    human_approval_for_diagram_code,
    interpret_human_response_for_diagram_code,
)
from ai.edges import (
    continue_gathering_requirements,
    ContinueGatheringRequirementsType,
    ai_next_step_for_all_requirements_after_human_feedback,
    AINextStepForAllRequirementsAfterHumanFeedbackType,
    ai_next_step_for_functional_requirements_after_human_feedback,
    AINextStepForFunctionalRequirementsAfterHumanFeedbackType,
    ai_next_step_for_non_functional_requirements_after_human_feedback,
    AINextStepForNonFunctionalRequirementsAfterHumanFeedbackType,
    ai_next_step_for_back_of_the_envelope_calculation_after_human_feedback,
    AINextStepForBackOfTheEnvelopeCalculationAfterHumanFeedbackType,
    ai_next_step_for_api_design_after_human_feedback,
    AINextStepForApiDesignAfterHumanFeedbackType,
    ai_next_step_for_data_model_after_human_feedback,
    AINextStepForDataModelAfterHumanFeedbackType,
    ai_next_step_for_design_overview_after_human_feedback,
    AINextStepForDesignOverviewAfterHumanFeedbackType,
    ai_next_step_for_diagram_code_after_human_feedback,
    AINextStepForDiagramCodeAfterHumanFeedbackType,
)
from ai.utils import literal_type_to_dict

class WorkFlow:
    def __init__(self):
        self.workflow = StateGraph(WorkFlowState)
        self.app = None

    def build(self, checkpointer=None):
        # ------------------ Requirements Gathering ------------------
        self.workflow.add_node("GATHER_REQUIREMENTS", gather_requirements)
        self.workflow.add_node("HUMAN_RESPONSE_FROM_GATHER_REQUIREMENTS", get_human_response_from_gather_requirements)

        self.workflow.add_edge(START, "GATHER_REQUIREMENTS")
        self.workflow.add_edge("GATHER_REQUIREMENTS", "HUMAN_RESPONSE_FROM_GATHER_REQUIREMENTS")
        self.workflow.add_conditional_edges(
            "HUMAN_RESPONSE_FROM_GATHER_REQUIREMENTS",
            continue_gathering_requirements,
            literal_type_to_dict(ContinueGatheringRequirementsType),
        )

        # ------------------ Finalize All Requirements ------------------
        self.workflow.add_node("ALL_REQUIREMENTS", get_all_requirements)
        self.workflow.add_node("HUMAN_APPROVAL_FOR_ALL_REQUIREMENTS", human_approval_all_requirements)
        self.workflow.add_node("INTERPRET_HUMAN_RESPONSE_FOR_ALL_REQUIREMENTS", interpret_human_response_for_all_requirements)

        self.workflow.add_edge("ALL_REQUIREMENTS", "HUMAN_APPROVAL_FOR_ALL_REQUIREMENTS")
        self.workflow.add_edge("HUMAN_APPROVAL_FOR_ALL_REQUIREMENTS", "INTERPRET_HUMAN_RESPONSE_FOR_ALL_REQUIREMENTS")
        self.workflow.add_conditional_edges(
            "INTERPRET_HUMAN_RESPONSE_FOR_ALL_REQUIREMENTS",
            ai_next_step_for_all_requirements_after_human_feedback,
            literal_type_to_dict(AINextStepForAllRequirementsAfterHumanFeedbackType),
        )

        # ------------------ Functional Requirements ------------------
        self.workflow.add_node("FUNCTIONAL_REQUIREMENTS", generate_functional_requirements)
        self.workflow.add_node("HUMAN_APPROVAL_FOR_FUNCTIONAL_REQUIREMENTS", human_approval_for_functional_requirements)
        self.workflow.add_node("INTERPRET_HUMAN_RESPONSE_FOR_FUNCTIONAL_REQUIREMENTS", interpret_human_response_for_functional_requirements)

        self.workflow.add_edge("FUNCTIONAL_REQUIREMENTS", "HUMAN_APPROVAL_FOR_FUNCTIONAL_REQUIREMENTS")
        self.workflow.add_edge("HUMAN_APPROVAL_FOR_FUNCTIONAL_REQUIREMENTS", "INTERPRET_HUMAN_RESPONSE_FOR_FUNCTIONAL_REQUIREMENTS")
        self.workflow.add_conditional_edges(
            "INTERPRET_HUMAN_RESPONSE_FOR_FUNCTIONAL_REQUIREMENTS",
            ai_next_step_for_functional_requirements_after_human_feedback,
            literal_type_to_dict(AINextStepForFunctionalRequirementsAfterHumanFeedbackType),
        )

        # ------------------ Non-Functional Requirements ------------------
        self.workflow.add_node("NON_FUNCTIONAL_REQUIREMENTS", generate_non_functional_requirements)
        self.workflow.add_node("HUMAN_APPROVAL_FOR_NON_FUNCTIONAL_REQUIREMENTS", human_approval_for_non_functional_requirements)
        self.workflow.add_node("INTERPRET_HUMAN_RESPONSE_FOR_NON_FUNCTIONAL_REQUIREMENTS", interpret_human_response_for_non_functional_requirements)

        self.workflow.add_edge("NON_FUNCTIONAL_REQUIREMENTS", "HUMAN_APPROVAL_FOR_NON_FUNCTIONAL_REQUIREMENTS")
        self.workflow.add_edge("HUMAN_APPROVAL_FOR_NON_FUNCTIONAL_REQUIREMENTS", "INTERPRET_HUMAN_RESPONSE_FOR_NON_FUNCTIONAL_REQUIREMENTS")
        self.workflow.add_conditional_edges(
            "INTERPRET_HUMAN_RESPONSE_FOR_NON_FUNCTIONAL_REQUIREMENTS",
            ai_next_step_for_non_functional_requirements_after_human_feedback,
            literal_type_to_dict(AINextStepForNonFunctionalRequirementsAfterHumanFeedbackType),
        )

        # ------------------ Back of the Envelope Calculation ------------------
        self.workflow.add_node("BACK_OF_THE_ENVELOPE_CALCULATION", generate_back_of_the_envelope_calculation)
        self.workflow.add_node("HUMAN_APPROVAL_FOR_BACK_OF_THE_ENVELOPE_CALCULATION", human_approval_for_back_of_the_envelope_calculation)
        self.workflow.add_node("INTERPRET_HUMAN_RESPONSE_FOR_BACK_OF_THE_ENVELOPE_CALCULATION", interpret_human_response_for_back_of_the_envelope_calculation)

        self.workflow.add_edge("BACK_OF_THE_ENVELOPE_CALCULATION", "HUMAN_APPROVAL_FOR_BACK_OF_THE_ENVELOPE_CALCULATION")
        self.workflow.add_edge("HUMAN_APPROVAL_FOR_BACK_OF_THE_ENVELOPE_CALCULATION", "INTERPRET_HUMAN_RESPONSE_FOR_BACK_OF_THE_ENVELOPE_CALCULATION")
        self.workflow.add_conditional_edges(
            "INTERPRET_HUMAN_RESPONSE_FOR_BACK_OF_THE_ENVELOPE_CALCULATION",
            ai_next_step_for_back_of_the_envelope_calculation_after_human_feedback,
            literal_type_to_dict(AINextStepForBackOfTheEnvelopeCalculationAfterHumanFeedbackType),
        )

        # ------------------ API Design ------------------
        self.workflow.add_node("API_DESIGN", generate_api_design)
        self.workflow.add_node("HUMAN_APPROVAL_FOR_API_DESIGN", human_approval_for_api_design)
        self.workflow.add_node("INTERPRET_HUMAN_RESPONSE_FOR_API_DESIGN", interpret_human_response_for_api_design)

        self.workflow.add_edge("API_DESIGN", "HUMAN_APPROVAL_FOR_API_DESIGN")
        self.workflow.add_edge("HUMAN_APPROVAL_FOR_API_DESIGN", "INTERPRET_HUMAN_RESPONSE_FOR_API_DESIGN")
        self.workflow.add_conditional_edges(
            "INTERPRET_HUMAN_RESPONSE_FOR_API_DESIGN",
            ai_next_step_for_api_design_after_human_feedback,
            literal_type_to_dict(AINextStepForApiDesignAfterHumanFeedbackType),
        )

        # ------------------ Data Model ------------------
        self.workflow.add_node("DATA_MODEL", generate_data_model)
        self.workflow.add_node("HUMAN_APPROVAL_FOR_DATA_MODEL", human_approval_for_data_model)
        self.workflow.add_node("INTERPRET_HUMAN_RESPONSE_FOR_DATA_MODEL", interpret_human_response_for_data_model)

        self.workflow.add_edge("DATA_MODEL", "HUMAN_APPROVAL_FOR_DATA_MODEL")
        self.workflow.add_edge("HUMAN_APPROVAL_FOR_DATA_MODEL", "INTERPRET_HUMAN_RESPONSE_FOR_DATA_MODEL")
        self.workflow.add_conditional_edges(
            "INTERPRET_HUMAN_RESPONSE_FOR_DATA_MODEL",
            ai_next_step_for_data_model_after_human_feedback,
            literal_type_to_dict(AINextStepForDataModelAfterHumanFeedbackType),
        )

        # ------------------ Design Overview ------------------
        self.workflow.add_node("DESIGN_OVERVIEW", generate_design_overview)
        self.workflow.add_node("HUMAN_APPROVAL_FOR_DESIGN_OVERVIEW", human_approval_for_design_overview)
        self.workflow.add_node("INTERPRET_HUMAN_RESPONSE_FOR_DESIGN_OVERVIEW", interpret_human_response_for_design_overview)

        self.workflow.add_edge("DESIGN_OVERVIEW", "HUMAN_APPROVAL_FOR_DESIGN_OVERVIEW")
        self.workflow.add_edge("HUMAN_APPROVAL_FOR_DESIGN_OVERVIEW", "INTERPRET_HUMAN_RESPONSE_FOR_DESIGN_OVERVIEW")
        self.workflow.add_conditional_edges(
            "INTERPRET_HUMAN_RESPONSE_FOR_DESIGN_OVERVIEW",
            ai_next_step_for_design_overview_after_human_feedback,
            literal_type_to_dict(AINextStepForDesignOverviewAfterHumanFeedbackType),
        )

        # ------------------ Diagram Code ------------------
        self.workflow.add_node("DIAGRAM_CODE", generate_diagram_code)
        self.workflow.add_node("HUMAN_APPROVAL_FOR_DIAGRAM_CODE", human_approval_for_diagram_code)
        self.workflow.add_node("INTERPRET_HUMAN_RESPONSE_FOR_DIAGRAM_CODE", interpret_human_response_for_diagram_code)

        self.workflow.add_edge("DIAGRAM_CODE", "HUMAN_APPROVAL_FOR_DIAGRAM_CODE")
        self.workflow.add_edge("HUMAN_APPROVAL_FOR_DIAGRAM_CODE", "INTERPRET_HUMAN_RESPONSE_FOR_DIAGRAM_CODE")
        self.workflow.add_conditional_edges(
            "INTERPRET_HUMAN_RESPONSE_FOR_DIAGRAM_CODE",
            ai_next_step_for_diagram_code_after_human_feedback,
            literal_type_to_dict(AINextStepForDiagramCodeAfterHumanFeedbackType),
        )

        self.app = self.workflow.compile(checkpointer=checkpointer)
        return self.app
    
    def get_mermain_png(self):
        self.build()
        with open("hld_agent_workflow.png", "wb") as f:
            f.write(self.app.get_graph().draw_mermaid_png())
    
    def resume(self):
        pass