import reflex as rx

from portfolio.components.common import section, section_heading
from portfolio.data import ACHIEVEMENTS, JOURNEY


def achievement(a: dict) -> rx.Component:
    return rx.box(
        rx.box(rx.icon(a["icon"], size=20), class_name="ach-icon"),
        rx.box(rx.text(a["title"], class_name="ach-title"), rx.text(a["text"], class_name="muted")),
        class_name="card ach reveal" + (" secondary" if a["secondary"] else ""),
    )


def timeline() -> rx.Component:
    return rx.box(
        *[
            rx.box(
                rx.box(class_name="tl-dot"),
                rx.text(t, class_name="tl-title"),
                rx.text(d, class_name="muted"),
                class_name="tl-item reveal",
            )
            for t, d in JOURNEY
        ],
        class_name="timeline",
    )


def experience() -> rx.Component:
    return section(
        "experience",
        section_heading("Track record", "Achievements & Experience"),
        rx.box(
            rx.box(*[achievement(a) for a in ACHIEVEMENTS], class_name="stack"),
            rx.box(rx.text("Developer journey", class_name="card-label"), timeline()),
            class_name="exp-grid",
        ),
    )
