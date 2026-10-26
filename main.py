from nicegui import ui

@ui.page("/")
def main_page():
    ui.label("Hello World")

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(
        title='XPlus Docs',
        dark=True,
        reload=False,
        show=False,
    )