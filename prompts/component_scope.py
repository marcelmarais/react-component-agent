from langchain.prompts import PromptTemplate

component_scope_prompt = PromptTemplate.from_template('''
I've created a component called {component_description} you'll write detailed step-by-step micro prompts, as comments, for each block of code to be exchanged for real syntax code later:

The comments should look more or less like as follows, but with info and content related to each {component_description} and in the correct order necessary for its development:

// Briefly explain the purpose and functionality of the {component_description}.
// Import libraries and other components IF necessary. You can use your tools to look up documentation for SHADCN UI components, which you should use as much as possible. The components you can lookup are: {availible_components}
// Define the types/interface for the component IF in Typescript.
// Declare any constants or hooks holding data necessary for the functionality of the {component_description}
// Write the main logic for the {component_description}, including any conditionals or loops IF necessary.
// Write any sub-functions if necessary for the main logic, including parameters and return values of the {component_description}
// Return the final JSX for the {component_description} IF there is one.
// Export the {component_description} for use in other parts of the application.

Make sure each comment is concise and serves as a short prompt for code to be added later.

Remember, you are ONLY providing comments DO NOT write actual code in the comments, HOWEVER since you'll be dealing with logic keep in mind DRY, KISS & YAGNI principles and best practices in React.
''')
