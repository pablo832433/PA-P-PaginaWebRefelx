import reflex as rx

def background_component(*children):
    return rx.box(
        *children,
        background_color="#181c24",
        width="100vw",
        min_height="100vh",
        margin="0",
        padding="0"
    )
    
    