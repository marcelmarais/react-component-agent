from langchain.prompts import PromptTemplate

code_component_prompt = PromptTemplate.from_template('''
Given the following documentation for a React functional component:
{documentation}

I want you to implement it. Providing all the code necessary. You can use your tools to look up documentation for SHADCN UI components, which you should use as much as possible. The components you can lookup are: {availible_components}
''')
