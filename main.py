from nicegui import ui

# Function to create the layout
def create_layout():
    # Full-page container (using flexbox for horizontal alignment of sidebar and right content)
    with ui.element().style('display: flex; flex-direction: row; height: 100vh; width: 100vw; background-color: #cfbdc8;'):
        
        # Left sidebar (takes 20% width, full height)
        with ui.column().style('width: 20%; height: 200%; background-color: #e5e7e8; padding: 20px; box-sizing: border-box;font-family: "Times New Roman", serif;'):
            ui.html('<span style ="background-color: #f1dae7;font-size: 20px; margin: 0; padding: 0;">String</span>')  # Light Blue
            ui.label('A sequence of characters used to represent text in programming.').style('margin: 0; padding: 0;')
            ui.html('<span style ="background-color: #c4d3e8;font-size: 20px;">Int</span>')  # Pastel Pink
            ui.label('A data type that represents whole numbers without decimal points.')
            ui.html('<span style ="background-color: #c4e8e6;font-size: 20px;">Float</span>')  # Pastel Green
            ui.label('A data type that represents numbers with decimal points.')
            ui.html('<span style ="background-color: #d3e8c4;font-size: 20px;">List</span>')  # Pastel Peach
            ui.label('A collection of ordered items that can store multiple values in a single variable.')
            ui.html('<span style ="background-color: #E6E6FA;font-size: 20px;">Tuple</span>')  # Pastel Lavender
            ui.label('A collection of ordered, immutable items, similar to a list but cannot be changed after creation.')
            ui.html('<span style ="background-color: #e8e4bf;font-size: 20px;">Bool</span>')  # Pastel Yellow
            ui.label('A data type that represents two values: True or False.')
            ui.html('<span style ="background-color: #f1e0c5;font-size: 20px;">Operator</span>')  # Pastel Light Blue
            ui.label('A symbol that performs an action on one or more operands (e.g., +, -, *, /).')
            ui.html('<span style ="background-color: #F4E0D7;font-size: 20px;">Keyword</span>')  # Pastel Pink Rose
            ui.label('A reserved word in a programming language that has a predefined function (e.g., if, else, while).')
            ui.html('<span style ="background-color: #C6D5CE;font-size: 20px;">If else</span>')  # Pastel Mint Green
            ui.label('A conditional statement used to execute code based on whether a condition is true or false.')
            ui.html('<span style ="background-color: #D2D9E9;font-size: 20px;">While Loop</span>')  # Pastel Coral
            ui.label('A control structure that repeatedly executes code as long as a given condition is true.')
            ui.html('<span style ="background-color: #C3DFE3;font-size: 20px;">For Loop</span>')  # Pastel Light Green
            ui.label('A control structure that iterates over a sequence of values or a range of numbers.')
          
        # Right content (contains the top bar and main content, takes 80% width)
        with ui.column().style('width: 80%; height: 200%; display: flex; flex-direction: column; margin: 0;'):
            
            # Top bar (takes 15% of the height and spans full width of the right content)
            with ui.row().style('height: 15%; width: 100%; background-color: #cfbdc8; padding: 20px; margin: 0; box-sizing: border-box;'): 
                # Create the textarea and define the on_change event to handle line breaks
                ui.textarea(
                    label='Enter code here',
                    on_change=lambda e: update_result(e.value)
                ).style('width:100%')
                
            # Main content area (remaining space, below the top bar)
            with ui.row().style('height: 185%; width: 100%; background-color: #cfbdc8; padding: 20px; margin: 0; box-sizing: border-box; overflow: auto;'):  
                result = ui.label().style('font-size: 20px; white-space: pre-wrap;')  # CSS property to handle new lines

        def update_result(text):
        # Split the text into lines, number them, and join back with new lines
            lines = text.split('\n')
            numbered_lines = [f"{i + 1}:   {line}" for i, line in enumerate(lines) if line]  # Number each line
            result.set_text('\n\n'.join(numbered_lines))  # Update the label with numbered lines

# Initialize the NiceGUI app
create_layout()

# Run the NiceGUI app
ui.run()
