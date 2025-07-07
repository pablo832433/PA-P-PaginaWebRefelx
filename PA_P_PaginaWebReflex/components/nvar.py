import reflex as rx

def nvar_component() -> rx.Component:
    return rx.box(
            rx.desktop_only(
                rx.hstack(
                    rx.input(
                        rx.input.slot(rx.icon("search")),
                        placeholder="Search...",
                        type="search",
                        size="2",
                        width="50vw",
                        radius='large'
                    )
                )
            )
        ) 
    


    