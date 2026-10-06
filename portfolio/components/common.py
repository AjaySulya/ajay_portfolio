import reflex as rx


def section(section_id: str, *children, **kw) -> rx.Component:
    return rx.el.section(rx.box(*children, class_name="container"), id=section_id, class_name="section", **kw)


def section_heading(eyebrow: str, title: str) -> rx.Component:
    return rx.box(
        rx.text(eyebrow, class_name="eyebrow"),
        rx.heading(title, as_="h2", class_name="h2"),
        class_name="sec-head reveal",
    )


def tag(label: str) -> rx.Component:
    return rx.box(label, class_name="tag")


def social_link(s: dict) -> rx.Component:
    return rx.link(
        rx.icon(s["icon"], size=18),
        s["label"],
        href=s["href"],
        target="_blank",
        rel="noopener noreferrer",
        class_name="social",
    )
