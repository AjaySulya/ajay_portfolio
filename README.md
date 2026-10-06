# Ajay Sulya | AI & Data Science Engineer Portfolio

A modern, dark-themed developer portfolio for **Ajay Sulya**, an AI & Data Science undergraduate focused on Machine Learning, LLM applications, RAG systems, and Agentic AI.

The whole site is written in **Python** with [Reflex](https://reflex.dev), managed with **uv**, and hosted as a static site on **Vercel**.

**Live site:** `https://ajay-portfolio-sable.vercel.ap`

---

## About the portfolio

The site is a single page with these sections:

| Section | What it shows |
|---|---|
| **Navbar** | Fixed, blurred header with smooth-scroll links and a mobile menu |
| **Hero** | "Building Intelligent Systems with AI & Data", call-to-action buttons, and a code-card visual |
| **About Me** | Short introduction and highlights (AI & Data Science undergraduate, 100+ LeetCode problems, SIH winner) |
| **Technical Skills** | Skills grouped into Programming, AI/ML, Generative AI, Backend, Databases, and DevOps/Tools |
| **Featured Projects** | Five project cards with description, tech tags, and GitHub links |
| **Achievements & Experience** | Smart India Hackathon 2025 winner, competitive programming, basketball, plus a developer-journey timeline |
| **Contact** | Social links and a contact form |
| **Footer** | Name, role, links, and copyright |

### Featured projects

1. **AI LLM Gateway**: model routing between applications and LLM providers, with fallbacks, auth, rate limiting, observability, and cost control
2. **Enterprise Multi-Agent RAG System**: routes queries to specialised agents for documents, SQL, and web research
3. **Suspicious Transaction Detection**: ML-based fraud detection using graph features
4. **AI Research Agent**: agentic workflow that gathers sources and writes structured reports
5. **Student Marks Predictor**: ensemble-model predictions behind a Flask interface

### Design

- Dark, near-black theme with subtle violet, blue, and cyan accents
- Inter for text and JetBrains Mono for technical labels
- Fine grid background with soft radial glows
- Subtle motion only: a hero entrance, card hover lift, and a gentle scroll fade (disabled automatically for users who prefer reduced motion)
- Fully responsive: two-column layout on desktop, single column on mobile, with no horizontal scrolling
- Keyboard-visible focus states, readable contrast, and semantic HTML (`header`, `nav`, `section`, `article`, `footer`)

---

## How it is built

### Tech stack

- **[Reflex](https://reflex.dev)**: write the frontend entirely in Python. Reflex compiles it into a React app behind the scenes, so no JavaScript is written by hand.
- **Python 3.11+**
- **[uv](https://docs.astral.sh/uv/)**: fast Python package and project manager
- **Plain CSS** (`assets/style.css`) for the theme, layout, and animations
- **[Formspree](https://formspree.io)**: handles contact-form submissions without a backend
- **[Vercel](https://vercel.com)**: static hosting

### Project structure

```text
ajay-portfolio/
├── rxconfig.py              # Reflex configuration (app name)
├── pyproject.toml           # Dependencies, managed by uv
├── uv.lock
├── assets/
│   ├── style.css            # Global theme, layout, animations
│   └── images/
└── portfolio/
    ├── portfolio.py         # App entry point: theme, fonts, page registration
    ├── data.py              # ALL content: projects, skills, links, achievements
    ├── pages/
    │   └── home.py          # Composes all sections into the page
    └── components/
        ├── common.py        # Shared helpers (section wrapper, tags, social links)
        ├── navbar.py
        ├── hero.py
        ├── about.py
        ├── skills.py
        ├── projects.py
        ├── experience.py
        ├── contact.py
        └── footer.py
```

The architecture is component-based. Each section is its own function in its own file, and `pages/home.py` stitches them together:

```python
navbar(); hero(); about(); skills(); projects(); experience(); contact(); footer()
```

Content is separated from layout. To change a project, skill, or link, edit `portfolio/data.py`. You don't need to touch any component code.

---

## Running locally

**Prerequisites:** [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.

```bash
# 1. Install dependencies
uv sync

# 2. Start the dev server
uv run reflex run
```

Open `http://localhost:3000`. The page hot-reloads when you edit files.

---

## Customising

| I want to change... | Edit |
|---|---|
| Projects, skills, achievements, timeline, social links | `portfolio/data.py` |
| Hero text and code card | `portfolio/components/hero.py` |
| About text | `portfolio/components/about.py` |
| Colors, fonts, spacing, animations | `assets/style.css` (colors are CSS variables at the top) |
| Page title and description | `portfolio/portfolio.py` |

Before publishing, replace the `# TODO` placeholders in `portfolio/data.py`:

- `LINKEDIN`: your LinkedIn profile URL
- `EMAIL`: your `mailto:` address
- the `github` link on each project card that currently points to the profile

---

## Contact form

Vercel only hosts static files, so there is no Python backend to receive form submissions. The form posts directly to **Formspree** instead:

1. Create a free form at [formspree.io](https://formspree.io) and copy its endpoint, for example `https://formspree.io/f/abcd1234`.
2. Set `FORM_ENDPOINT` at the top of `portfolio/components/contact.py`.

Messages arrive in your email inbox.

---

## Author

**Ajay Sulya**: AI & Data Science Engineer
[GitHub](https://github.com/AjaySulya)

© 2026 Ajay Sulya. Built with Reflex.