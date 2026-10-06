"""All portfolio content lives here. Edit this file to update the site."""

GITHUB = "https://github.com/AjaySulya"
LINKEDIN = "https://www.linkedin.com/in/ajay-sulya-06b53b292/"  
EMAIL = "ajaysulya06@gmail.com"  

NAV_LINKS = ["About", "Skills", "Projects", "Experience", "Contact"]

SOCIALS = [
    {"label": "GitHub", "icon": "github", "href": GITHUB},
    {"label": "LinkedIn", "icon": "linkedin", "href": LINKEDIN},
    {"label": "Email", "icon": "mail", "href": EMAIL},
]

STATS = [
    ("AI & Data Science", "Undergraduate"),
    ("100+", "LeetCode problems"),
    ("Multiple", "AI projects"),
    ("SIH", "Hackathon winner"),
]

SKILLS = [
    ("Programming", ["Python", "Java"]),
    ("AI / Machine Learning", ["Machine Learning", "Scikit-learn", "TensorFlow", "XGBoost", "CatBoost", "LightGBM", "Pandas", "NumPy"]),
    ("Generative AI", ["LLMs", "RAG", "Agentic AI", "LangChain", "LangGraph", "Hugging Face", "Sentence Transformers"]),
    ("Backend", ["FastAPI", "Flask", "REST APIs", "Pydantic"]),
    ("Databases", ["PostgreSQL", "ChromaDB", "FAISS", "Qdrant"]),
    ("DevOps / Tools", ["Docker", "Git", "GitHub", "Postman", "Linux", "VS Code"]),
]

PROJECTS = [
    {
        "category": "AI Infrastructure",
        "title": "AI LLM Gateway",
        "description": "An AI gateway and model routing platform designed to sit between applications and LLM providers, providing centralized routing, fallbacks, authentication, rate limiting, observability, and cost control.",
        "tech": ["Python", "FastAPI", "LiteLLM", "PostgreSQL", "Redis", "Docker", "SQLAlchemy"],
        "github": "https://github.com/AjaySulya/ai-gateway",
        "demo": None,
    },
    {
        "category": "Agentic AI / RAG",
        "title": "Enterprise Multi-Agent RAG System",
        "description": "A multi-agent AI system that intelligently routes user queries to specialized agents for document retrieval, SQL queries, and web research using RAG and LLM-powered workflows.",
        "tech": ["Python", "LangGraph", "LangChain", "FastAPI", "ChromaDB", "PostgreSQL", "Hugging Face", "Docker"],
        "github": "https://github.com/AjaySulya/EnterpriseMultiAgentRAGSystem", 
        "demo": None,
    },
    {
        "category": "Machine Learning",
        "title": "Suspicious Transaction Detection",
        "description": "A machine learning system for detecting suspicious financial transactions using feature engineering, graph-based features, and machine learning models.",
        "tech": ["Python", "Scikit-learn", "XGBoost", "CatBoost", "NetworkX", "Pandas", "Streamlit", "Docker"],
        "github": "https://github.com/AjaySulya/Suspicious-Transaction-Detection",
        "demo": None,
    },
    {
        "category": "Agentic AI",
        "title": "AI Research Agent",
        "description": "An AI-powered research agent that searches for information, processes relevant sources, and generates structured research reports using agentic workflows.",
        "tech": ["Python", "LangGraph", "Hugging Face", "FastAPI", "LLMs"],
        "github": "https://github.com/AjaySulya/research-ai-agent",  # TODO: point to the repo
        "demo": None,
    },
    {
        "category": "Machine Learning",
        "title": "Student Marks Predictor",
        "description": "A machine learning application that predicts student performance using multiple regression and ensemble learning models with a Flask-based interface.",
        "tech": ["Python", "Flask", "Scikit-learn", "XGBoost", "CatBoost", "Random Forest"],
        "github": "https://github.com/AjaySulya/studentmarkspredictor",  # TODO: point to the repo
        "demo": None,
    },
]

ACHIEVEMENTS = [
    {"icon": "trophy", "title": "Winner — Smart India Hackathon 2025", "text": "Won the national-level hackathon by building a working solution to a real problem statement as part of a team.", "secondary": False},
    {"icon": "code", "title": "100+ LeetCode Problems Solved", "text": "Regular data-structures and algorithms practice to keep problem-solving skills sharp.", "secondary": False},
    {"icon": "dribbble", "title": "Regional-level Basketball Player", "text": "Team sport that built discipline, communication, and performing under pressure.", "secondary": True},
]

JOURNEY = [
    ("AI & Data Science", "Foundations in data, statistics, and Python"),
    ("Machine Learning", "Classical models, feature engineering, ensembles"),
    ("LLM Applications", "Prompting, APIs, and Hugging Face models"),
    ("RAG Systems", "Embeddings, vector databases, retrieval pipelines"),
    ("Agentic AI", "Multi-agent workflows with LangGraph"),
    ("AI Infrastructure", "Gateways, routing, observability, and cost control"),
]
