from pydantic import BaseModel, Field, StrictBool
from typing import Annotated, Optional

class GatherRequirementsState(BaseModel):
    ask_another_question: StrictBool
    question: Annotated[str, Field(description="Requirement gathering question")]
    title: Optional[str] = Field(description="Title for HLD Interview question")

class FinalizeRequirementsState(BaseModel):
    requirements: list[Annotated[str, Field(description="Inital Requirements for System")]]




