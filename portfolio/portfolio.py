import reflex as rx

from portfolio.pages.home import home

app = rx.App(
    theme=rx.theme(appearance="dark", accent_color="violet", radius="large"),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&family=JetBrains+Mono:wght@400;500&display=swap",
        "/style.css",
    ],
)
app.add_page(
    home,
    route="/",
    title="Ajay Sulya | AI & Data Science Engineer",
    description="Portfolio of Ajay Sulya: Machine Learning, LLM applications, RAG and Agentic AI.",
)
