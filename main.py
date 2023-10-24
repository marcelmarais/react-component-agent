from typing import List
from operator import itemgetter
from pydantic import BaseModel, Field
from langchain.agents import (Tool, AgentExecutor, BaseMultiActionAgent,
                              initialize_agent, AgentType)
from langchain.utilities import SerpAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import StrOutputParser
from langchain.globals import set_debug
from data.design_system import DESIGN_SYSTEM
from data.shadcn_ui_docs import SHAD_CN_UI_COMPONENTS_STR
from prompts.code_component import code_component_prompt
from prompts.component_scope import component_scope_prompt
from prompts.style_component import style_component_prompt

from tools import ToolsInitialiser

import os


def initialise_llm(model_name: str):
    return ChatOpenAI(
        openai_api_key=os.environ.get('OPENAI_API_KEY'),
        max_tokens=2056,
        model_name=model_name
    )


tools = ToolsInitialiser.initialize_tools()
llm = initialise_llm(model_name='gpt-4-0613')

agent = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True
)


def create_main_chain(agent, llm):
    scope_component_chain = component_scope_prompt | llm

    code_component_chain = {
        'documentation': scope_component_chain,  'availible_components': itemgetter("availible_components")} | code_component_prompt | agent

    style_component_chain = {'component': code_component_chain, 'design_system': itemgetter(
        "design_system")} | style_component_prompt | llm

    return style_component_chain


main_chain = create_main_chain(agent, llm)
print(main_chain.input_schema.schema())

def generate_component(component_description):
    return main_chain.invoke(
        {"component_description": component_description, "availible_components": SHAD_CN_UI_COMPONENTS_STR,  "design_system": DESIGN_SYSTEM})


if __name__ == '__main__':
    COMPONENT_DESCRIPTION = "Centered hero text with an input text field below, there should be some indication that an API key needs to be entered"
    react_component = generate_component(
        component_description=COMPONENT_DESCRIPTION)
    with open("example.txt", "w") as text_file:
        text_file.write(str(react_component))
