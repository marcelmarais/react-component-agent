from langchain.prompts import PromptTemplate

style_component_prompt = PromptTemplate.from_template('''

Your task is to enhance the visual aesthetics of the following component using TailwindCSS, while preserving its existing functionality. Please return all relevant code that achieves this. Adhere to the modern and minimalist design specified in the following design system.

Component to Style:
{component}
                                                      
Design System Specifications:
{design_system}

[CODE INSTRUCT] Make sure to return all the code needed to run this component with the Tailwind CSS styling included. DO NOT return any natural language. ONLY CODE. Retain all the original imports and functionality. that were included in the component to begin with. 
''')