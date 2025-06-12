"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
#from .pages.info import pagina_info
from .pages.login import pagina_login
from .pages.singup import pagina_singup


# -------------------------------- INICIALIZACION DE LA APLICACION --------------------------------#
app = rx.App() # init de la app 


# -------------------------------- LLAMADA A LAS PAGINAS  --------------------------------#
#app.add_page(pagina_info, route="/info", title='Info pagina')
app.add_page(pagina_login, route='/login', title='Iniciar sesión')
app.add_page(pagina_singup, route='/singup', title='Registrarse')