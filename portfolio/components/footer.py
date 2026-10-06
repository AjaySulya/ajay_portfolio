import reflex as rx

from portfolio.components.common import social_link
from portfolio.data import SOCIALS


def footer() -> rx.Component:
    return rx.el.footer(
        rx.box(
            rx.box(
                rx.text("AJAY SULYA", class_name="logo"),
                rx.text("AI & Data Science Engineer", class_name="muted"),
            ),
            rx.box(*[social_link(s) for s in SOCIALS], class_name="social-row"),
            class_name="foot-top",
        ),
        rx.text("© 2026 Ajay Sulya. Built with Reflex.", class_name="copy"),
        class_name="footer container",
    )
