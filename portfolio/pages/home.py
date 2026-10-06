import reflex as rx

from portfolio.components.about import about
from portfolio.components.contact import contact
from portfolio.components.experience import experience
from portfolio.components.footer import footer
from portfolio.components.hero import hero
from portfolio.components.navbar import navbar
from portfolio.components.projects import projects
from portfolio.components.skills import skills


def home() -> rx.Component:
    return rx.box(
        navbar(), hero(), about(), skills(), projects(), experience(), contact(), footer(),
        id="top",
        class_name="page",
    )
