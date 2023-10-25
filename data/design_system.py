
DESIGN_SYSTEM = '''
# Typography

Headings:

H1: text-4xl font-extrabold tracking-tight lg:text-5xl
H2: mt-10 text-3xl font-semibold tracking-tight transition-colors first:mt-0
H3: mt-8 text-2xl font-semibold tracking-tight

Paragraphs:

leading-7 [:not(:first-child)]:mt-6

Links:

font-medium text-primary underline underline-offset-4

Blockquote: 

mt-6 border-l-2 pl-6 italic

Lists:

my-6 ml-6 list-disc [:>li]:mt-2

Table:

Header: border px-4 py-2 text-left font-bold [:align=center]:text-center [:align=right]:text-right
Body: border px-4 py-2 text-left [:align=center]:text-center [:align=right]:text-right

# Buttons
Primary Button
bg-blue-500 text-white py-2 px-4 rounded
Secondary Button
bg-gray-200 text-gray-700 py-2 px-4 rounded

# Forms
Input Fields
border p-2 rounded

Checkboxes
form-checkbox text-teal-600

# Radio Buttons
form-radio text-teal-600

# Input Fields

# border p-2 rounded
Checkboxes
form-checkbox text-{accent_colour}-600
Radio Buttons
form-radio text-{accent_colour}-600

Spacing and Layout:
Padding: p-4
Margin: m-4
Flexbox: 
flex
flex-col
items-center

Grid:
grid
grid-cols-3

# Additional Components

Cards: p-4 border rounded shadow-md
Tooltips: bg-gray-200 text-sm rounded p-1
Alerts: text-white bg-red-500 p-2 rounded


'''
