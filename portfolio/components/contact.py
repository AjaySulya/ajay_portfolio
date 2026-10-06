import reflex as rx

from portfolio.components.common import section, social_link
from portfolio.data import SOCIALS

FORM_ENDPOINT = "https://formspree.io/f/mrpeebgr"  


def _form() -> rx.Component:
    return rx.el.form(
        rx.el.input(name="name", placeholder="Name", required=True, aria_label="Name", class_name="field"),
        rx.el.input(name="email", type="email", placeholder="Email", required=True, aria_label="Email", class_name="field"),
        rx.el.textarea(name="message", placeholder="Message", required=True, rows=5, aria_label="Message", class_name="field"),
        rx.el.button("Send Message", type="submit", class_name="btn btn-primary"),
        action=FORM_ENDPOINT,
        method="POST",
        class_name="form",
    )


def contact() -> rx.Component:
    return section(
        "contact",
        rx.box(
            rx.box(
                rx.heading("Let's Build Something Intelligent", as_="h2", class_name="h2"),
                rx.text(
                    "I'm open to internships, AI engineering opportunities, backend engineering roles, "
                    "and interesting AI projects.",
                    class_name="body",
                ),
                rx.box(*[social_link(s) for s in SOCIALS], class_name="social-row"),
                class_name="reveal",
            ),
            rx.box(_form(), class_name="card reveal"),
            class_name="contact-grid",
        ),
    )