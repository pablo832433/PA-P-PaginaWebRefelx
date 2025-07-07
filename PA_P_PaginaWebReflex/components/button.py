import reflex as rx


# ==================== BUTTONS ====================
def login_button() -> rx.Component:
    return rx.hstack(
            rx.button(
            "Sign Up",
            size="2",
            variant="soft",
            color_scheme="jade",
            radius="large",
            type="button"
    )
    ),

def singup_button() -> rx.Component:
    return rx.hstack(
            rx.button(
            "Sign Up",
            size="2",
            variant="soft",
            color_scheme="jade",
            radius="large",
            type="button"
        )
    )

def askQuestion_button() -> rx.Component:
    return

def home_button() -> rx.Component:
    return 