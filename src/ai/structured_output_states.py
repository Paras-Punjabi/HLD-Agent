from pydantic import BaseModel, Field
from typing import Literal

InterpretHumanFeedbackFromRequirementsType = Literal["MOVE_TO_NEXT_STEP", "AGAIN_FINALIZE_REQUIREMENTS"]
InterpretHumanFeedbackFromFunctionalRequirementsType = Literal["MOVE_TO_NEXT_STEP", "AGAIN_FINALIZE_REQUIREMENTS"]
InterpretHumanFeedbackFromNonFunctionalRequirementsType = Literal["MOVE_TO_NEXT_STEP", "AGAIN_FINALIZE_REQUIREMENTS"]
InterpretHumanFeedbackFromBackOfTheEnvelopeCalculationType = Literal["MOVE_TO_NEXT_STEP", "AGAIN_FINALIZE_REQUIREMENTS"]
InterpretHumanFeedbackFromApiDesignType = Literal["MOVE_TO_NEXT_STEP", "AGAIN_FINALIZE_REQUIREMENTS"]
InterpretHumanFeedbackFromDataModelType = Literal["MOVE_TO_NEXT_STEP", "AGAIN_FINALIZE_REQUIREMENTS"]
InterpretHumanFeedbackFromDesignOverviewType = Literal["MOVE_TO_NEXT_STEP", "AGAIN_FINALIZE_REQUIREMENTS"]
InterpretHumanFeedbackFromDiagramCodeType = Literal["MOVE_TO_NEXT_STEP", "AGAIN_FINALIZE_REQUIREMENTS"]

class GatherRequirementsState(BaseModel):
    ask_another_question: bool = Field(description="Whether to ask another question or not")
    question: str = Field(description="Requirement gathering question")

class FinalizeRequirementsState(BaseModel):
    requirements: list[str] = Field(description="Initial Requirements for System")

class InterpretHumanFeedbackFromRequirementsState(BaseModel):
    next_step: InterpretHumanFeedbackFromRequirementsType = Field(
        description="Next Step from given human feedback. Can be MOVE_TO_NEXT_STEP or AGAIN_FINALIZE_REQUIREMENTS"
    )

class FinalizeFunctionalRequirementsState(BaseModel):
    functional_requirements: list[str] = Field(description="Functional Requirements for System")

class InterpretHumanFeedbackFromFunctionalRequirementsState(BaseModel):
    next_step: InterpretHumanFeedbackFromFunctionalRequirementsType = Field(
        description="Next Step from given human feedback. Can be MOVE_TO_NEXT_STEP or AGAIN_FINALIZE_REQUIREMENTS"
    )

class FinalizeNonFunctionalRequirementsState(BaseModel):
    non_functional_requirements: list[str] = Field(description="Non Functional Requirements for System")

class InterpretHumanFeedbackFromNonFunctionalRequirementsState(BaseModel):
    next_step: InterpretHumanFeedbackFromNonFunctionalRequirementsType = Field(
        description="Next Step from given human feedback. Can be MOVE_TO_NEXT_STEP or AGAIN_FINALIZE_REQUIREMENTS"
    )

class FinalizeBackOfTheEnvelopeCalculationState(BaseModel):
    calculation: str = Field(
        description="Back of the envelope calculation for the system estimating throughput, storage, bandwidth, and memory"
    )

class InterpretHumanFeedbackFromBackOfTheEnvelopeCalculationState(BaseModel):
    next_step: InterpretHumanFeedbackFromBackOfTheEnvelopeCalculationType = Field(
        description="Next Step from given human feedback. Can be MOVE_TO_NEXT_STEP or AGAIN_FINALIZE_REQUIREMENTS"
    )

class FinalizeApiDesignState(BaseModel):
    api_design: list[str] = Field(description="API Design specifications for the system")

class InterpretHumanFeedbackFromApiDesignState(BaseModel):
    next_step: InterpretHumanFeedbackFromApiDesignType = Field(
        description="Next Step from given human feedback. Can be MOVE_TO_NEXT_STEP or AGAIN_FINALIZE_REQUIREMENTS"
    )

class FinalizeDataModelState(BaseModel):
    data_model: str = Field(
        description="Describes what the data model looks like, including tables/collections, attributes, and schemas"
    )

class InterpretHumanFeedbackFromDataModelState(BaseModel):
    next_step: InterpretHumanFeedbackFromDataModelType = Field(
        description="Next Step from given human feedback. Can be MOVE_TO_NEXT_STEP or AGAIN_FINALIZE_REQUIREMENTS"
    )

class FinalizeDesignOverviewState(BaseModel):
    design_overview: str = Field(
        description="Full overview of the system design architecture and request flow"
    )

class InterpretHumanFeedbackFromDesignOverviewState(BaseModel):
    next_step: InterpretHumanFeedbackFromDesignOverviewType = Field(
        description="Next Step from given human feedback. Can be MOVE_TO_NEXT_STEP or AGAIN_FINALIZE_REQUIREMENTS"
    )

class FinalizeDiagramCodeState(BaseModel):
    diagram_code: str = Field(
        description="Code of HLD Diagram written using diagrams library in python"
    )

class InterpretHumanFeedbackFromDiagramCodeState(BaseModel):
    next_step: InterpretHumanFeedbackFromDiagramCodeType = Field(
        description="Next Step from given human feedback. Can be MOVE_TO_NEXT_STEP or AGAIN_FINALIZE_REQUIREMENTS"
    )
