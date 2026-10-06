import reflex as rx

CODE = '''class Agent:
    def route(self, query: str):
        intent = classify(query)
        tool = self.tools[intent]   # rag | sql | web
        return tool.run(query)

gateway.fallback("gpt", "llama")
gateway.limit(rpm=60, budget=25.0)'''


def hero() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.box(
                rx.box(rx.box(class_name="dot"), "Open to internships & AI roles", class_name="badge"),
                rx.heading(
                    "Building Intelligent Systems",
                    rx.el.br(),
                    rx.el.span("with AI & Data", class_name="grad"),
                    as_="h1",
                    class_name="h1",
                ),
                rx.text(
                    "I'm Ajay Sulya, an AI & Data Science engineer focused on Machine Learning, "
                    "LLM applications, RAG systems, and Agentic AI.",
                    class_name="lead",
                ),
                rx.box(
                    rx.link("View Projects", href="#projects", class_name="btn btn-primary"),
                    rx.link("Contact Me", href="#contact", class_name="btn btn-primary btn-alt"),
                    rx.link(rx.icon("github", size=18), "GitHub", href="https://github.com/AjaySulya",
                            target="_blank", rel="noopener noreferrer", class_name="btn btn-ghost"),
                    class_name="cta-row",
                ),
                class_name="hero-copy",
            ),
            rx.box(
                rx.box(
                    rx.box(rx.box(class_name="wdot"), rx.box(class_name="wdot"), rx.box(class_name="wdot"),
                           rx.text("agent.py", class_name="fname"), class_name="win-bar"),
                    rx.el.pre(CODE, class_name="code"),
                    class_name="code-card",
                ),
                rx.box("RAG", class_name="chip chip-a"),
                rx.box("LangGraph", class_name="chip chip-b"),
                rx.box("FastAPI", class_name="chip chip-c"),
                class_name="hero-visual",
            ),
            class_name="container hero-grid",
        ),
        class_name="hero",
    )
