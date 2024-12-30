from nicegui import ui
from datetime import datetime

# Define the main page layout
@ui.page('/')
def page_layout():
    # HEADER
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        ui.label('HEADER').style('color: white; font-size: 20px;')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')

    # LEFT DRAWER
    with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4') as left_drawer:
        ui.label('Time Sheet')
        ui.label('Time Sheet')

    # RIGHT DRAWER
    with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
        ui.label('RIGHT DRAWER')

    # MAIN CONTENT
    with ui.column().classes('w-full items-center'):


        # Date Picker Section
        today = datetime.today().strftime('%Y-%m-%d')
        ui.date(value=today, on_change=lambda e: result.set_text(f'Selected date: {e.value}'))
        result = ui.label('Selected date will appear here.')

    # FOOTER
    with ui.footer().style('background-color: #3874c8'):
        ui.label('FOOTER').style('color: white; font-size: 16px;')


# Run the app
ui.run()
