import reflex as rx

def nvbar_component() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.hstack(
                rx.image(
                    src="/logo.jpg",
                    w="2em",                # mismo ancho en todo lado
                    h="auto",
                    border_radius="25%"
                ),
                rx.heading(
                    "Reflex",
                    # Variante responsiva: 6 en móvil, 7 desde md (≥ 62 em)
                    size=rx.breakpoints(initial="6", md="7"),
                    weight="bold",
                ),
                spacing="2",
                align="center",
            ),
            # --- Buscador ---
             rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Search…",
                type="search",
                size="2",
                # ancho 60 % en móvil, 18 em en desktop
                w=rx.breakpoints(initial="60%", md="18em"),
                max_w="20em",
            ),
            justify="between",
            align="center",
            w="full",
        ),

        # Estilo del navbar
        bg=rx.color("accent", 3),
        padding_x = '2em', # padding left-right (eje x)            
        padding_y="0.7em", # padding top-bottom (altura de navbar eje y)
        shadow="md",

        # Fijar arriba
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="5",
    
    )