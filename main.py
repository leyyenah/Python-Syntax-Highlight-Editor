from nicegui import ui
import re
import keyword

# Color mapping for syntax highlighting
SYNTAX_COLORS = {
    'String': 'background-color: #f1dae7;',  # Pink
    'int': 'background-color: #c4d3e8;',     # Blue
    'float': 'background-color: #c4e8e6;',   # Green
    'list': 'background-color: #d3e8c4;',
    'tuple': 'background-color: #E6E6FA;',  # Light Purple
    'bool': 'background-color: #e8e4bf;',
    'operator': 'background-color: #f1e0c5;',  # Light Yellow
    'keyword': 'background-color: #F4E0D7;',   # Light Orange
    'If-Else': 'background-color: #C6D5CE;',   # Light Green
    'While Loop': 'background-color: #D2D9E9;', # Light Blue
    'For Loop': 'background-color: #C3DFE3;',   # Light Teal
}

# Helper function to validate list elements
def is_valid_list_element(element):
    element = element.strip()
    return (
        (element.startswith(("'", '"')) and element.endswith(("'", '"')) and element[0] == element[-1]) or  # Valid string
        element.isdigit() or  # Integer
        ('.' in element and element.replace('.', '', 1).isdigit()) or  # Float
        element in ['True', 'False'] or  # Boolean
        not element  # Allow empty elements
    )

# Helper function to validate tuple elements
def is_valid_tuple_element(element):
    element = element.strip()
    return (
        (element.startswith(("'", '"')) and element.endswith(("'", '"')) and element[0] == element[-1]) or  # Valid string
        element.isdigit() or  # Integer
        ('.' in element and element.replace('.', '', 1).isdigit()) or  # Float
        element in ['True', 'False'] or  # Boolean
        not element  # Allow empty elements
    )

# Function to apply syntax highlighting to the code
def highlight_code(text):
    
    pattern = r'(\w+)\s*=\s*(\[[^\]]*\]|\([^)]*\)|["\'].*?["\']|\d+\.\d+|\d+|True|False|\w+\s*\(.*?\)|\w+)|(\+|-|\*|/|%|==|!=|<|>|=)|\b(if|else|elif|while|for)\b|(\d+\.\d+|\d+|["\'].*?["\'])'

    def replacer(match):
        variable_name = match.group(1)  # Variable name
        value = match.group(2)  # Value being assigned
        operator = match.group(3)  # Operator
        control_flow = match.group(4)  # Control flow keyword
        standalone_value = match.group(5)  # Standalone numbers or strings

        # Highlighting for assignments
        if value:
            if value.startswith("[") and value.endswith("]"):  # List
                elements = value[1:-1].split(",")
                if all(is_valid_list_element(e.strip()) for e in elements):
                    color = SYNTAX_COLORS['list']
                else:
                    return f'{variable_name} = {value}'
            elif value.startswith('(') and value.endswith(')'):  # Tuple
                elements = [e.strip() for e in value[1:-1].split(',')]
                if all(is_valid_tuple_element(e) for e in elements):
                    color = SYNTAX_COLORS['tuple']
                else:
                    return f'{variable_name} = {value}'
            elif value.startswith(("'", '"')) and value.endswith(("'", '"')):  # String
                if value[0] == value[-1]:
                    color = SYNTAX_COLORS['String']
                else:
                    return f'{variable_name} = {value}'
            elif '.' in value and value.replace('.', '', 1).isdigit():  # Float
                color = SYNTAX_COLORS['float']
            elif value.isdigit():  # Int
                color = SYNTAX_COLORS['int']
            elif value == 'True' or value == 'False':  # Bool
                color = SYNTAX_COLORS['bool']
            else:
                return f'{variable_name} = {value}'  # Invalid value, no highlighting
            
            return f'{variable_name} = <span style="{color}">{value}</span>'
        
        # Highlighting for operators
        elif operator:
            return f'<span style="{SYNTAX_COLORS["operator"]}">{operator}</span>'
        
        # Highlighting for control flow keywords
        elif control_flow:
            if control_flow in ['if', 'else', 'elif']:
                color = SYNTAX_COLORS['If-Else']
            elif control_flow == 'while':
                color = SYNTAX_COLORS['While Loop']
            elif control_flow == 'for':
                color = SYNTAX_COLORS['For Loop']
            return f'<span style="{color}">{control_flow}</span>'
        
        # Highlighting for standalone numbers and strings
        elif standalone_value:
            if '.' in standalone_value and standalone_value.replace('.', '', 1).isdigit():  # Float
                color = SYNTAX_COLORS['float']
            elif standalone_value.isdigit():  # Int
                color = SYNTAX_COLORS['int']
            elif standalone_value.startswith(("'", '"')) and standalone_value.endswith(("'", '"')):  # String
                color = SYNTAX_COLORS['String']
            else:
                return standalone_value
            
            return f'<span style="{color}">{standalone_value}</span>'
        
        else:
            return ''

    # Apply regex replacement and return highlighted HTML
    highlighted = re.sub(pattern, replacer, text)
    return highlighted

# Function to create and manage the app layout
def create_layout():
    # Outer container (flexbox)
    with ui.element().style('display: flex; flex-direction: row; height: 100vh; width: 100vw; background-color: #cfbdc8;'):
        
        # Left sidebar
        with ui.column().style('width: 20%; height: 200%; background-color: #e5e7e8; padding: 20px; box-sizing: border-box; font-family: "Times New Roman", serif;'):
            ui.html('<span style="background-color: #f1dae7;font-size: 20px;">String</span>')
            ui.label('A sequence of characters used to represent text in programming.')
            ui.html('<span style="background-color: #c4d3e8;font-size: 20px;">Int</span>')
            ui.label('A data type that represents whole numbers without decimal points.')
            ui.html('<span style="background-color: #c4e8e6;font-size: 20px;">Float</span>')
            ui.label('A data type that represents numbers with decimal points.')
            ui.html('<span style="background-color: #d3e8c4;font-size: 20px;">List</span>')
            ui.label('A collection of ordered items that can store multiple values in a single variable.')
            ui.html('<span style="background-color: #E6E6FA;font-size: 20px;">Tuple</span>')
            ui.label('A collection of ordered, immutable items, similar to a list but cannot be changed after creation.')
            ui.html('<span style="background-color: #e8e4bf;font-size: 20px;">Bool</span>')
            ui.label('A data type that represents two values: True or False.')
            ui.html('<span style="background-color: #f1e0c5;font-size: 20px;">Operator</span>')
            ui.label('A symbol that performs an action on one or more operands (e.g., +, -, *, /).')
            ui.html('<span style="background-color: #C6D5CE;font-size: 20px;">If Else</span>')
            ui.label('A conditional statement used to execute code based on whether a condition is true or false.')
            ui.html('<span style="background-color: #D2D9E9;font-size: 20px;">While Loop</span>')
            ui.label('A control structure that repeatedly executes code as long as a given condition is true.')
            ui.html('<span style="background-color: #C3DFE3;font-size: 20px;">For Loop</span>')
            ui.label('A control structure that iterates over a sequence of values or a range of numbers.')
        
        
        # Right main content area
        with ui.column().style('width: 80%;height: 200%; display: flex; flex-direction: column; padding: 20px; background-color: #cfbdc8; box-sizing: border-box;'):
            
            # Top bar with textarea
            textarea = ui.textarea(
                label='Enter code here',
                on_change=lambda e: update_content(e.value),
            ).style('font-family: "Courier New", monospace; font-size: 16px; width: 100%; height: 200px; margin-bottom: 20px; background-color: #cfbdc8; color: black; border: 1px solid transparent;')

            # Content display area with numbered lines
            content_display = ui.html().style('white-space: pre-wrap; font-family: "Courier New", monospace; font-size: 16px; color: black; background-color: #cfbdc8; border: none; padding: 10px;')
    
    # Function to update content in the display area
    def update_content(text):
        # Handle empty input
        if not text.strip():
            content_display.set_content('<span style="color: gray;">(No code entered yet)</span>')
            return

        # Split text into lines and add line numbers
        lines = text.split('\n')
        numbered_lines = [
            f'<span style="color: gray;">{i + 1}: </span>{highlight_code(line)}'
            for i, line in enumerate(lines)
        ]
        # Join numbered lines with line breaks
        highlighted_text = '<br>'.join(numbered_lines)
        content_display.set_content(highlighted_text)

# Initialize the app
create_layout()
ui.run()
