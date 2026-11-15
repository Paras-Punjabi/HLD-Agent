from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.types import interrupt
from ai.prompts import (
    GATHERING_REQUIREMENTS_PROMPT,
    FINALIZE_REQUIREMENTS_PROMPT,
    FUNCTIONAL_REQUIREMENTS_PROMPT,
    NON_FUNCTIONAL_REQUIREMENTS_PROMPT,
    BACK_OF_THE_ENVELOPE_CALCULATIONS_PROMPT,
    API_DESIGN_PROMPT,
    DATA_MODEL_PROMPT,
    DESIGN_OVERVIEW_PROMPT,
    DIAGRAM_CODE_PROMPT,
)
from ai.structured_output_states import (
    GatherRequirementsState,
    FinalizeRequirementsState,
    InterpretHumanFeedbackFromRequirementsState,
    FinalizeFunctionalRequirementsState,
    InterpretHumanFeedbackFromFunctionalRequirementsState,
    FinalizeNonFunctionalRequirementsState,
    InterpretHumanFeedbackFromNonFunctionalRequirementsState,
    FinalizeBackOfTheEnvelopeCalculationState,
    InterpretHumanFeedbackFromBackOfTheEnvelopeCalculationState,
    FinalizeApiDesignState,
    InterpretHumanFeedbackFromApiDesignState,
    FinalizeDataModelState,
    InterpretHumanFeedbackFromDataModelState,
    FinalizeDesignOverviewState,
    InterpretHumanFeedbackFromDesignOverviewState,
    FinalizeDiagramCodeState,
    InterpretHumanFeedbackFromDiagramCodeState,
)
from ai.states import WorkFlowState
from ai.llm_factory import LLMFactory
from config.env import config

# ------------------ Requirements Gathering ------------------

def gather_requirements(state: WorkFlowState):
    chat_history = list(state.chat_history)
    messages = [
        SystemMessage(content=GATHERING_REQUIREMENTS_PROMPT),
        *chat_history
    ]
    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, GatherRequirementsState)
    chat_history.append(AIMessage(content=result.question))
    return {
        "chat_history": chat_history,
        "gathering_requirements_loop": result.ask_another_question,
    }

def get_human_response_from_gather_requirements(state: WorkFlowState):
    last_message = state.chat_history[-1].content if state.chat_history else "Requirement Gathering"
    human = interrupt(f"Human Response for {last_message}")
    chat_history = list(state.chat_history)
    chat_history.append(HumanMessage(content=human))
    return {
        "chat_history": chat_history,
        "human_response_from_gather_requirements": human
    }

# ------------------ Finalize All Requirements ------------------

def get_all_requirements(state: WorkFlowState):
    chat_history = list(state.chat_history)
    messages = [
        SystemMessage(content=FINALIZE_REQUIREMENTS_PROMPT),
        *chat_history
    ]
    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, FinalizeRequirementsState)
    reqs_summary = "\n".join(f"- {req}" for req in result.requirements)
    chat_history.append(AIMessage(content=f"All Requirements:\n{reqs_summary}"))
    return {
        "chat_history": chat_history,
        "requirements": result.requirements
    }

def human_approval_all_requirements(state: WorkFlowState):
    human = interrupt("Human Approval for All Requirements")
    chat_history = list(state.chat_history)
    chat_history.append(HumanMessage(content=human))
    return {
        "chat_history": chat_history,
        "all_requirements_human_feedback": human
    }

def interpret_human_response_for_all_requirements(state: WorkFlowState):
    messages = [
        SystemMessage(content=FINALIZE_REQUIREMENTS_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        HumanMessage(content=f"Human Approval: {state.all_requirements_human_feedback}"),
        HumanMessage(content="Interpret what will be the next step from given human feedback for the given requirements provided by you.")
    ]
    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, InterpretHumanFeedbackFromRequirementsState)
    return {
        "ai_next_step_for_human_feedback_for_all_requirements": result.next_step
    }

# ------------------ Functional Requirements ------------------

def generate_functional_requirements(state: WorkFlowState):
    chat_history = list(state.chat_history)
    messages = [
        SystemMessage(content=FUNCTIONAL_REQUIREMENTS_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}")
    ]
    if state.functional_requirements_human_feedback:
        messages.append(HumanMessage(content=f"Previous Feedback: {state.functional_requirements_human_feedback}"))

    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, FinalizeFunctionalRequirementsState)
    func_summary = "\n".join(f"- {fr}" for fr in result.functional_requirements)
    chat_history.append(AIMessage(content=f"Functional Requirements:\n{func_summary}"))
    return {
        "chat_history": chat_history,
        "functional_requirements": result.functional_requirements
    }

def human_approval_for_functional_requirements(state: WorkFlowState):
    human = interrupt("Human Approval for Functional Requirements")
    chat_history = list(state.chat_history)
    chat_history.append(HumanMessage(content=human))
    return {
        "chat_history": chat_history,
        "functional_requirements_human_feedback": human
    }

def interpret_human_response_for_functional_requirements(state: WorkFlowState):
    messages = [
        SystemMessage(content=FUNCTIONAL_REQUIREMENTS_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        AIMessage(content=f"Functional Requirements: {state.functional_requirements}"),
        HumanMessage(content=f"Human Approval: {state.functional_requirements_human_feedback}"),
        HumanMessage(content="Interpret what will be the next step from given human feedback for the given functional requirements provided by you.")
    ]
    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, InterpretHumanFeedbackFromFunctionalRequirementsState)
    return {
        "ai_next_step_for_human_feedback_for_functional_requirements": result.next_step
    }

# ------------------ Non-Functional Requirements ------------------

def generate_non_functional_requirements(state: WorkFlowState):
    chat_history = list(state.chat_history)
    messages = [
        SystemMessage(content=NON_FUNCTIONAL_REQUIREMENTS_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        HumanMessage(content=f"All Functional Requirements: {state.functional_requirements}")
    ]
    if state.non_functional_requirements_human_feedback:
        messages.append(HumanMessage(content=f"Previous Feedback: {state.non_functional_requirements_human_feedback}"))

    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, FinalizeNonFunctionalRequirementsState)
    non_func_summary = "\n".join(f"- {nfr}" for nfr in result.non_functional_requirements)
    chat_history.append(AIMessage(content=f"Non Functional Requirements:\n{non_func_summary}"))
    return {
        "chat_history": chat_history,
        "non_functional_requirements": result.non_functional_requirements
    }

def human_approval_for_non_functional_requirements(state: WorkFlowState):
    human = interrupt("Human Approval for Non Functional Requirements")
    chat_history = list(state.chat_history)
    chat_history.append(HumanMessage(content=human))
    return {
        "chat_history": chat_history,
        "non_functional_requirements_human_feedback": human
    }

def interpret_human_response_for_non_functional_requirements(state: WorkFlowState):
    messages = [
        SystemMessage(content=NON_FUNCTIONAL_REQUIREMENTS_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        AIMessage(content=f"Functional Requirements: {state.functional_requirements}"),
        AIMessage(content=f"Non Functional Requirements: {state.non_functional_requirements}"),
        HumanMessage(content=f"Human Approval: {state.non_functional_requirements_human_feedback}"),
        HumanMessage(content="Interpret what will be the next step from given human feedback for the given non functional requirements provided by you.")
    ]
    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, InterpretHumanFeedbackFromNonFunctionalRequirementsState)
    return {
        "ai_next_step_for_human_feedback_for_non_functional_requirements": result.next_step
    }

# ------------------ Back of the Envelope Calculations ------------------

def generate_back_of_the_envelope_calculation(state: WorkFlowState):
    chat_history = list(state.chat_history)
    messages = [
        SystemMessage(content=BACK_OF_THE_ENVELOPE_CALCULATIONS_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        HumanMessage(content=f"Functional Requirements: {state.functional_requirements}"),
        HumanMessage(content=f"Non Functional Requirements: {state.non_functional_requirements}")
    ]
    if state.back_of_the_envelope_calculation_human_feedback:
        messages.append(HumanMessage(content=f"Previous Feedback: {state.back_of_the_envelope_calculation_human_feedback}"))

    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, FinalizeBackOfTheEnvelopeCalculationState)
    chat_history.append(AIMessage(content=f"Back of the Envelope Calculation:\n{result.calculation}"))
    return {
        "chat_history": chat_history,
        "back_of_the_envelope_calculation": result.calculation
    }

def human_approval_for_back_of_the_envelope_calculation(state: WorkFlowState):
    human = interrupt("Human Approval for Back of the Envelope Calculation")
    chat_history = list(state.chat_history)
    chat_history.append(HumanMessage(content=human))
    return {
        "chat_history": chat_history,
        "back_of_the_envelope_calculation_human_feedback": human
    }

def interpret_human_response_for_back_of_the_envelope_calculation(state: WorkFlowState):
    messages = [
        SystemMessage(content=BACK_OF_THE_ENVELOPE_CALCULATIONS_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        HumanMessage(content=f"Functional Requirements: {state.functional_requirements}"),
        HumanMessage(content=f"Non Functional Requirements: {state.non_functional_requirements}"),
        AIMessage(content=f"Back of the Envelope Calculation: {state.back_of_the_envelope_calculation}"),
        HumanMessage(content=f"Human Approval: {state.back_of_the_envelope_calculation_human_feedback}"),
        HumanMessage(content="Interpret what will be the next step from given human feedback for the given back of the envelope calculation provided by you.")
    ]
    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, InterpretHumanFeedbackFromBackOfTheEnvelopeCalculationState)
    return {
        "ai_next_step_for_human_feedback_for_back_of_the_envelope_calculation": result.next_step
    }

# ------------------ API Design ------------------

def generate_api_design(state: WorkFlowState):
    chat_history = list(state.chat_history)
    messages = [
        SystemMessage(content=API_DESIGN_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        HumanMessage(content=f"Functional Requirements: {state.functional_requirements}"),
        HumanMessage(content=f"Non Functional Requirements: {state.non_functional_requirements}"),
        HumanMessage(content=f"Back of the Envelope Calculation: {state.back_of_the_envelope_calculation}")
    ]
    if state.api_design_human_feedback:
        messages.append(HumanMessage(content=f"Previous Feedback: {state.api_design_human_feedback}"))

    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, FinalizeApiDesignState)
    api_summary = "\n".join(f"- {api}" for api in result.api_design)
    chat_history.append(AIMessage(content=f"API Design:\n{api_summary}"))
    return {
        "chat_history": chat_history,
        "api_design": result.api_design
    }

def human_approval_for_api_design(state: WorkFlowState):
    human = interrupt("Human Approval for API Design")
    chat_history = list(state.chat_history)
    chat_history.append(HumanMessage(content=human))
    return {
        "chat_history": chat_history,
        "api_design_human_feedback": human
    }

def interpret_human_response_for_api_design(state: WorkFlowState):
    messages = [
        SystemMessage(content=API_DESIGN_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        HumanMessage(content=f"Functional Requirements: {state.functional_requirements}"),
        AIMessage(content=f"API Design: {state.api_design}"),
        HumanMessage(content=f"Human Approval: {state.api_design_human_feedback}"),
        HumanMessage(content="Interpret what will be the next step from given human feedback for the given API design provided by you.")
    ]
    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, InterpretHumanFeedbackFromApiDesignState)
    return {
        "ai_next_step_for_human_feedback_for_api_design": result.next_step
    }

# ------------------ Data Model ------------------

def generate_data_model(state: WorkFlowState):
    chat_history = list(state.chat_history)
    messages = [
        SystemMessage(content=DATA_MODEL_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        HumanMessage(content=f"Functional Requirements: {state.functional_requirements}"),
        HumanMessage(content=f"Non Functional Requirements: {state.non_functional_requirements}"),
        HumanMessage(content=f"Back of the Envelope Calculation: {state.back_of_the_envelope_calculation}"),
        HumanMessage(content=f"API Design: {state.api_design}")
    ]
    if state.data_model_human_feedback:
        messages.append(HumanMessage(content=f"Previous Feedback: {state.data_model_human_feedback}"))

    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, FinalizeDataModelState)
    chat_history.append(AIMessage(content=f"Data Model:\n{result.data_model}"))
    return {
        "chat_history": chat_history,
        "data_model": result.data_model
    }

def human_approval_for_data_model(state: WorkFlowState):
    human = interrupt("Human Approval for Data Model")
    chat_history = list(state.chat_history)
    chat_history.append(HumanMessage(content=human))
    return {
        "chat_history": chat_history,
        "data_model_human_feedback": human
    }

def interpret_human_response_for_data_model(state: WorkFlowState):
    messages = [
        SystemMessage(content=DATA_MODEL_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        HumanMessage(content=f"API Design: {state.api_design}"),
        AIMessage(content=f"Data Model: {state.data_model}"),
        HumanMessage(content=f"Human Approval: {state.data_model_human_feedback}"),
        HumanMessage(content="Interpret what will be the next step from given human feedback for the given data model provided by you.")
    ]
    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, InterpretHumanFeedbackFromDataModelState)
    return {
        "ai_next_step_for_human_feedback_for_data_model": result.next_step
    }

# ------------------ Design Overview ------------------

def generate_design_overview(state: WorkFlowState):
    chat_history = list(state.chat_history)
    messages = [
        SystemMessage(content=DESIGN_OVERVIEW_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        HumanMessage(content=f"Functional Requirements: {state.functional_requirements}"),
        HumanMessage(content=f"Non Functional Requirements: {state.non_functional_requirements}"),
        HumanMessage(content=f"Back of the Envelope Calculation: {state.back_of_the_envelope_calculation}"),
        HumanMessage(content=f"API Design: {state.api_design}"),
        HumanMessage(content=f"Data Model: {state.data_model}")
    ]
    if state.design_overview_human_feedback:
        messages.append(HumanMessage(content=f"Previous Feedback: {state.design_overview_human_feedback}"))

    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, FinalizeDesignOverviewState)
    chat_history.append(AIMessage(content=f"Design Overview:\n{result.design_overview}"))
    return {
        "chat_history": chat_history,
        "design_overview": result.design_overview
    }

def human_approval_for_design_overview(state: WorkFlowState):
    human = interrupt("Human Approval for Design Overview")
    chat_history = list(state.chat_history)
    chat_history.append(HumanMessage(content=human))
    return {
        "chat_history": chat_history,
        "design_overview_human_feedback": human
    }

def interpret_human_response_for_design_overview(state: WorkFlowState):
    messages = [
        SystemMessage(content=DESIGN_OVERVIEW_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        HumanMessage(content=f"Data Model: {state.data_model}"),
        AIMessage(content=f"Design Overview: {state.design_overview}"),
        HumanMessage(content=f"Human Approval: {state.design_overview_human_feedback}"),
        HumanMessage(content="Interpret what will be the next step from given human feedback for the given design overview provided by you.")
    ]
    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, InterpretHumanFeedbackFromDesignOverviewState)
    return {
        "ai_next_step_for_human_feedback_for_design_overview": result.next_step
    }

# ------------------ Diagram Code ------------------

def generate_diagram_code(state: WorkFlowState):
    chat_history = list(state.chat_history)
    messages = [
        SystemMessage(content=DIAGRAM_CODE_PROMPT),
        HumanMessage(content=f"All Requirements: {state.requirements}"),
        HumanMessage(content=f"Functional Requirements: {state.functional_requirements}"),
        HumanMessage(content=f"Non Functional Requirements: {state.non_functional_requirements}"),
        HumanMessage(content=f"Back of the Envelope Calculation: {state.back_of_the_envelope_calculation}"),
        HumanMessage(content=f"API Design: {state.api_design}"),
        HumanMessage(content=f"Data Model: {state.data_model}"),
        HumanMessage(content=f"Design Overview: {state.design_overview}")
    ]
    if state.diagram_code_human_feedback:
        messages.append(HumanMessage(content=f"Previous Feedback: {state.diagram_code_human_feedback}"))

    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, FinalizeDiagramCodeState)
    chat_history.append(AIMessage(content=f"Diagram Code:\n```python\n{result.diagram_code}\n```"))
    return {
        "chat_history": chat_history,
        "diagram_code": result.diagram_code
    }

def human_approval_for_diagram_code(state: WorkFlowState):
    human = interrupt("Human Approval for Diagram Code")
    chat_history = list(state.chat_history)
    chat_history.append(HumanMessage(content=human))
    return {
        "chat_history": chat_history,
        "diagram_code_human_feedback": human
    }

def interpret_human_response_for_diagram_code(state: WorkFlowState):
    messages = [
        SystemMessage(content=DIAGRAM_CODE_PROMPT),
        HumanMessage(content=f"Design Overview: {state.design_overview}"),
        AIMessage(content=f"Diagram Code: {state.diagram_code}"),
        HumanMessage(content=f"Human Approval: {state.diagram_code_human_feedback}"),
        HumanMessage(content="Interpret what will be the next step from given human feedback for the given diagram code provided by you.")
    ]
    llm = LLMFactory(provider=config.PROVIDER)
    result = llm.invoke(messages, InterpretHumanFeedbackFromDiagramCodeState)
    return {
        "ai_next_step_for_human_feedback_for_diagram_code": result.next_step
    }
