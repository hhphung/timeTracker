from nicegui import ui

# Define a counter variable
counter = 0

# Define a function to increment the counter
def increment():
    global counter
    counter += 1
    label.text = f"Counter: {counter}"

# Define a function to reset the counter
def reset():
    global counter
    counter = 0
    label.text = f"Counter: {counter}"

# Create a user interface
with ui.column():
    label = ui.label(f"Counter: {counter}")
    ui.button("Increment", on_click=increment)
    ui.button("Reset", on_click=reset)

# Run the app
ui.run()
