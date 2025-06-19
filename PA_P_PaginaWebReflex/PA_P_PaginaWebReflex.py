"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from .pages.index import index_page



# -------------------------------- INICIALIZACION DE LA APLICACION --------------------------------#
app = rx.App() # init de la app 


# -------------------------------- LLAMADA A LAS PAGINAS  --------------------------------#
app.add_page(index_page, route="/Index", title='Index Page')
