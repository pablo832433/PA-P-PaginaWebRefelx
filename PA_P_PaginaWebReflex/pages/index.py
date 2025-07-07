import reflex as rx
from rxconfig import config
from PA_P_PaginaWebReflex.components.background_color import background_component
from PA_P_PaginaWebReflex.components.nvar import nvar_component
from PA_P_PaginaWebReflex.components.button import login_button, singup_button


def index_page():
    return rx.box(
        rx.box(
            rx.box(
                nvar_component(),
                flex="1",
                display="flex",
                justify_content="center"
            ),
            rx.box(
                login_button(),
                singup_button(),
                display="flex",
                gap="1em"  # Espacio entre botones
            ),
            display="flex",
            align_items="center",
            width="100%",
            padding="1em"
        )
    )


app = rx.App()
app.add_page(index_page)
