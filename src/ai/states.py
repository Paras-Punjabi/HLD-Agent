from pydantic import BaseModel, Field
from typing import Optional
from langchain_core.messages import BaseMessage

class WorkFlowState(BaseModel):
    chat_history: list[BaseMessage] = Field(default_factory=list)

    gathering_requirements_loop: bool = Field(default=True)
    requirements: list[str] = Field(default_factory=list, description="All Requirements")
    human_response_from_gather_requirements: Optional[str] = Field(default=None, description="Human Response for Gathering Requirement")
    all_requirements_human_feedback: Optional[str] = Field(default=None, description="Human Approval for All Requirements")
    ai_next_step_for_human_feedback_for_all_requirements: Optional[str] = Field(default=None, description="AI Next Step for Human Feedback for All Requirements")

    functional_requirements: list[str] = Field(default_factory=list, description="Functional Requirements")
    functional_requirements_human_feedback: Optional[str] = Field(default=None, description="Human Feedback for Functional Requirements")
    ai_next_step_for_human_feedback_for_functional_requirements: Optional[str] = Field(default=None, description="AI Next Step for Human Feedback for Functional Requirements")

    non_functional_requirements: list[str] = Field(default_factory=list, description="Non Functional Requirements")
    non_functional_requirements_human_feedback: Optional[str] = Field(default=None, description="Human Feedback for Non Functional Requirements")
    ai_next_step_for_human_feedback_for_non_functional_requirements: Optional[str] = Field(default=None, description="AI Next Step for Human Feedback for Non Functional Requirements")

    back_of_the_envelope_calculation: Optional[str] = Field(default=None, description="Back of the envelope calculation")
    back_of_the_envelope_calculation_human_feedback: Optional[str] = Field(default=None, description="Human Feedback for Back of the Envelope Calculation")
    ai_next_step_for_human_feedback_for_back_of_the_envelope_calculation: Optional[str] = Field(default=None, description="AI Next Step for Back of the Envelope Calculation")

    api_design: list[str] = Field(default_factory=list, description="API Design of the System")
    api_design_human_feedback: Optional[str] = Field(default=None, description="Human Feedback for API Design")
    ai_next_step_for_human_feedback_for_api_design: Optional[str] = Field(default=None, description="AI Next Step for Human Feedback for API Design")

    data_model: Optional[str] = Field(default=None, description="Describes what does data model looks like")
    data_model_human_feedback: Optional[str] = Field(default=None, description="Human Feedback for Data Model")
    ai_next_step_for_human_feedback_for_data_model: Optional[str] = Field(default=None, description="AI Next Step for Human Feedback for Data Model")

    design_overview: Optional[str] = Field(default=None, description="Full overview of the system design of the given HLD question")
    design_overview_human_feedback: Optional[str] = Field(default=None, description="Human Feedback for Design Overview")
    ai_next_step_for_human_feedback_for_design_overview: Optional[str] = Field(default=None, description="AI Next Step for Human Feedback for Design Overview")

    diagram_code: Optional[str] = Field(default=None, description="Code of HLD Diagram written using diagrams library in python")
    diagram_code_human_feedback: Optional[str] = Field(default=None, description="Human Feedback for Diagram Code")
    ai_next_step_for_human_feedback_for_diagram_code: Optional[str] = Field(default=None, description="AI Next Step for Human Feedback for Diagram Code")
