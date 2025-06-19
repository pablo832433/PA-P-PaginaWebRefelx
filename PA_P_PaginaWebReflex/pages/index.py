import reflex as rx
from rxconfig import config
from PA_P_PaginaWebReflex.components.background_color import background_component
from PA_P_PaginaWebReflex.components.navbar import nvbar_component


def index_page():
    return background_component(
        background_component(),
        nvbar_component()
        
    )


app = rx.App()
app.add_page(index_page)
