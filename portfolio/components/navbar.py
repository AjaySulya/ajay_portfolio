import reflex as rx

from portfolio.data import NAV_LINKS


def _scroll(target: str):
    return rx.call_script(
        f"document.getElementById('{target}')?.scrollIntoView({{behavior:'smooth'}})"
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.box(
            rx.link("AJAY SULYA", href="#top", class_name="logo"),
            rx.el.nav(
                *[rx.link(l, href=f"#{l.lower()}", class_name="nav-link") for l in NAV_LINKS],
                class_name="nav-links",
                aria_label="Primary",
            ),
            rx.link("Let's Talk", href="#contact", class_name="btn btn-primary nav-cta"),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(rx.icon("menu", size=22), variant="ghost", aria_label="Open navigation menu", class_name="menu-btn")
                ),
                rx.menu.content(
                    *[rx.menu.item(l, on_click=_scroll(l.lower())) for l in NAV_LINKS],
                    rx.menu.item("Let's Talk", on_click=_scroll("contact")),
                ),
            ),
            class_name="nav-inner",
        ),
        class_name="navbar",
    )
