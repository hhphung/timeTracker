from nicegui import ui


# Sidebar Component
def sidebar():
    with ui.drawer(side='left') as drawer:  # Drawer opens from the left side
        with ui.column().classes('w-64 h-full bg-gray-800 text-white p-4'):
            ui.label('My Sidebar').classes('text-xl font-bold mb-4')
            ui.link('🏠 Home', '/').classes('hover:underline p-2')
            ui.link('ℹ️ About', '/about').classes('hover:underline p-2')
            ui.link('📞 Contact', '/contact').classes('hover:underline p-2')
            ui.button('Close', on_click=lambda: drawer.set_visibility(False)).classes('mt-auto bg-red-500')


# Main Page with Sidebar Toggle
@ui.page('/')
def homepage():
    # Top Navbar with Sidebar Toggle Button
    with ui.row().classes('w-full items-center bg-blue-500 text-white p-4'):
        ui.button(icon='menu', on_click=lambda: drawer.set_visibility(True)).classes('lg:hidden')
        ui.label('My Website').classes('text-xl font-bold')

    # Call the sidebar function
    sidebar()

    # Main content area
    with ui.column().classes('p-4'):
        ui.label('Welcome to My Website!').classes('text-2xl mt-4')
        ui.label('This is the main content area.')


ui.run()
