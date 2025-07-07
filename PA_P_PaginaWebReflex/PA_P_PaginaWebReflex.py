import reflex as rx
from rxconfig import config
from .pages.index import index_page



# -------------------------------- INICIALIZACION DE LA APLICACION --------------------------------#
app = rx.App(
        theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="teal",
    )
) # init de la app 


# -------------------------------- LLAMADA A LAS PAGINAS  --------------------------------#
app.add_page(index_page, route="/Index", title='Index Page')
