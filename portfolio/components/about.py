import reflex as rx

from portfolio.components.common import section, section_heading
from portfolio.data import STATS


def about() -> rx.Component:
    return section(
        "about",
        section_heading("Who I am", "About Me"),
        rx.box(
            rx.box(
                rx.text(
                    "I'm an AI & Data Science undergraduate who likes turning models into products people can use. "
                    "My work spans classical Machine Learning, LLM applications, retrieval-augmented generation (RAG), "
                    "and agentic workflows where several specialised agents cooperate on a task.",
                    class_name="body",
                ),
                rx.text(
                    "I also care about what sits around the model: backend APIs, routing, observability, "
                    "and cost control. I'm most interested in solving real-world problems with practical, "
                    "well-engineered AI systems.",
                    class_name="body",
                ),
                class_name="reveal",
            ),
            rx.box(
                *[
                    rx.box(rx.text(big, class_name="stat-big"), rx.text(small, class_name="stat-small"), class_name="stat")
                    for big, small in STATS
                ],
                class_name="stats reveal",
            ),
            class_name="about-grid",
        ),
    )
