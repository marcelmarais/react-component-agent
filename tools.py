from typing import List
from data.shadcn_ui_docs import SHAD_CN_UI_DOCS
from langchain.agents import Tool
from config.data_models import GetDocumentationDataModel


class ToolsInitialiser:
    @staticmethod
    def get_component_info(component_names: List[str]) -> str:
        output = ""
        for component_name in component_names:
            output += SHAD_CN_UI_DOCS.get(component_name.lower(),
                                          f"No SHADCN UI component called: {component_name}, you need to make your own.")
            output += "/n"

        return output

    @staticmethod
    def initialize_tools() -> List:
        return [
            Tool.from_function(
                func=ToolsInitialiser.get_component_info,
                name="GetShadcnUiDocumentation",
                description="Retrieve comprehensive documentation for the SHADCN UI component library.",
                args_schema=GetDocumentationDataModel
            ),
        ]
