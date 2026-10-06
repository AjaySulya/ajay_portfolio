import reflex as rx

from portfolio.components.common import section, section_heading, tag
from portfolio.data import SKILLS


def skill_card(category: str, items: list[str]) -> rx.Component:
    return rx.box(
        rx.text(category, class_name="card-label"),
        rx.box(*[tag(i) for i in items], class_name="tags"),
        class_name="card reveal",
    )


def skills() -> rx.Component:
    return section(
        "skills",
        section_heading("Toolbox", "Technical Skills"),
        rx.box(*[skill_card(c, i) for c, i in SKILLS], class_name="grid grid-3"),
    )
