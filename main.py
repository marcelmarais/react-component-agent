import os
from operator import itemgetter

from langchain.agents import (initialize_agent, AgentType)
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_debug

from data.design_system import DESIGN_SYSTEM
from data.shadcn_ui_docs import SHAD_CN_UI_COMPONENTS_STR
from prompts.code_component import code_component_prompt
from prompts.component_scope import component_scope_prompt
from prompts.style_component import style_component_prompt
from prompts.system_prompt import system_message
from tools import ToolsInitialiser
from utils.cli_tools import print_header, get_valid_path, print_colored, remove_code_block_markers


def initialise_llm(model_name: str):
    return ChatOpenAI(
        openai_api_key=os.environ.get('OPENAI_API_KEY'),
        max_tokens=2056,
        model_name=model_name
    )


tools = ToolsInitialiser.initialize_tools()
llm = initialise_llm(model_name='gpt-4-0613')
agent = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True, agent_kwargs={"system_message": system_message})


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
    set_debug(True)
    print_header("REACT COMPONENT AGENT")

    print("\n--- Specify Components Directory ---")
    components_path = get_valid_path(
        "\nEnter the path to your components directory: ")

    while True:
        print("\n--- Create Your Component(s) ---")
        COMPONENT_DESCRIPTION = input(
            "\nEnter the description of the component you want to create ('exit' to quit): ")

        if COMPONENT_DESCRIPTION.lower() == 'exit':
            break

        react_component = generate_component(
            component_description=COMPONENT_DESCRIPTION)
        filename = "MyComponent.tsx"  # Customize this as needed
        full_path = os.path.join(components_path, filename)

        with open(full_path, "w") as text_file:
            cleaned_component = f"use client;\n{remove_code_block_markers(react_component.content)}"
            text_file.write(str(react_component.content))

        print_colored(
            f"Component has been generated and saved to {full_path}", color_code="94")

    print_header("Exiting the program.")
