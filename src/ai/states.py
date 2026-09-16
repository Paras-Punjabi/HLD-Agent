from pydantic import BaseModel, Field
from typing import Annotated
from langchain_core.messages import BaseMessage

class WorkFlowState(BaseModel):
    chat_id: Annotated[str, Field(description="Chat Id")]
    chat_title: Annotated[str, Field(description="Title for HLD Question")]
    user_prompt: Annotated[str, Field(description="User Prompt")]
    
    chat_history: list[BaseMessage]

    functional_requirements: list[Annotated[str, Field(description="Functional Requirement")]]

    non_functional_requirements: list[Annotated[str, Field(description="Non Functional Requirement")]]

    back_of_the_envelope_calculation: Annotated[str, Field(description="Back of the envelope calculation")]

    api_design: list[Annotated[str, Field(description="API Design of the System")]]

    data_model: Annotated[str, Field(description="Describes what does data model looks like")]

    design_overview: Annotated[str, Field(description="Full overview of the system design of the given HLD question")]

    diagram_code: Annotated[str, Field(description="Code of HLD Diagram written using diagrams library in python")]