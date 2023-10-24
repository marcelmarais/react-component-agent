from langchain.prompts import PromptTemplate

style_component_prompt = PromptTemplate.from_template('''

Your task is to enhance the visual aesthetics of the following component using TailwindCSS, while preserving its existing functionality. Please return all relevant code that achieves this. Adhere to the modern and minimalist design specified in the following design system.

Design System Specifications:
{design_system}

Component to Style:
{component}

Note: Make sure to return all the code needed to run this component.
''')