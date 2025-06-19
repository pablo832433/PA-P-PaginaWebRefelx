import reflex as rx

def nvbar_component() -> rx.Component:
    return rx.container(
            rx.box(                      
                rx.desktop_only(
                    rx.hstack(
                        rx.hstack(
                            rx.image(
                                src="/logo.jpg",
                                width="2.25em",
                                height="auto",
                                border_radius="25%",
                            ),
                            rx.heading(
                                "Reflex", size="7", weight="bold"
                            ),
                            align_items="center",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("search")),
                            placeholder="Search...",
                            type="search",
                            size="2",
                            justify="end",
                        ),
                        justify="between",
                        align_items="center",
                    ),
                ),
                rx.mobile_and_tablet(
                    rx.hstack(
                        rx.hstack(
                            rx.image(
                                src="/logo.jpg",
                                width="2em",
                                height="auto",
                                border_radius="25%",
                            ),
                            rx.heading(
                                "Reflex", size="6", weight="bold"
                            ),
                            align_items="center",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("search")),
                            placeholder="Search...",
                            type="search",
                            size="2",
                            justify="end",
                        ),
                        justify="between",
                        align_items="center",
                    ),
                ),
                bg=rx.color("accent", 3),
                padding="1em",
                # position="fixed",
                # top="0px",
                # z_index="5",
                width="100vw",
            )
            
)