import reflex as rx

from portfolio.components.common import section, section_heading, tag
from portfolio.data import PROJECTS


def project_card(p: dict) -> rx.Component:
    links = [
        rx.link("GitHub", rx.icon("arrow-up-right", size=16), href=p["github"], target="_blank",
                rel="noopener noreferrer", class_name="card-link", aria_label=f"{p['title']} on GitHub")
    ]
    if p.get("demo"):
        links.append(rx.link("Demo", rx.icon("arrow-up-right", size=16), href=p["demo"], target="_blank",
                             rel="noopener noreferrer", class_name="card-link"))
    return rx.el.article(
        rx.text(p["category"], class_name="card-label"),
        rx.heading(p["title"], as_="h3", class_name="h3"),
        rx.text(p["description"], class_name="muted"),
        rx.box(*[tag(t) for t in p["tech"]], class_name="tags"),
        rx.box(*links, class_name="card-links"),
        class_name="card project reveal",
    )


def projects() -> rx.Component:
    return section(
        "projects",
        section_heading("Selected work", "Featured Projects"),
        rx.box(*[project_card(p) for p in PROJECTS], class_name="grid grid-2"),
    )
