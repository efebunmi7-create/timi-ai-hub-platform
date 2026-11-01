import json
import os
import sqlite3
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = os.environ.get("DATABASE_PATH", str(BASE_DIR / "timi_ai_hub.db"))
SECRET_KEY = os.environ.get("SECRET_KEY", "timi-ai-hub-dev-secret")

app = Flask(__name__)
app.secret_key = SECRET_KEY


DEFAULT_BOTS = [
    {
        "id": "general-ai",
        "name": "General AI Assistant",
        "category": "AI Chat Bots",
        "description": "Ask questions, brainstorm, summarize, and get fast answers.",
        "icon": "sparkles",
        "color": "purple",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "coding-assistant",
        "name": "Coding Assistant",
        "category": "AI Chat Bots",
        "description": "Generate, debug, explain, and refactor code across languages.",
        "icon": "code",
        "color": "blue",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "math-assistant",
        "name": "Mathematics Assistant",
        "category": "AI Chat Bots",
        "description": "Solve equations, prove results, and explain mathematical reasoning.",
        "icon": "calculator",
        "color": "indigo",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "writing-assistant",
        "name": "Writing Assistant",
        "category": "AI Chat Bots",
        "description": "Improve blogs, outlines, landing pages, and business content.",
        "icon": "pen-square",
        "color": "pink",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "translation-bot",
        "name": "Translation Bot",
        "category": "AI Chat Bots",
        "description": "Translate text between languages and keep tone natural. ",
        "icon": "languages",
        "color": "cyan",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "grammar-bot",
        "name": "Grammar Correction Bot",
        "category": "AI Chat Bots",
        "description": "Polish grammar, punctuation, clarity, and tone for clean writing.",
        "icon": "spellcheck",
        "color": "amber",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "research-assistant",
        "name": "Research Assistant",
        "category": "AI Chat Bots",
        "description": "Collect and synthesize information for better decisions.",
        "icon": "book-open",
        "color": "green",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "pdf-reader",
        "name": "PDF Reader & Summarizer",
        "category": "AI Chat Bots",
        "description": "Summarize documents and answer questions from uploaded PDFs.",
        "icon": "file-pdf",
        "color": "red",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "image-understanding",
        "name": "Image Understanding Bot",
        "category": "AI Chat Bots",
        "description": "Describe, analyze, and interpret images with context-aware answers.",
        "icon": "image",
        "color": "violet",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "voice-assistant",
        "name": "Voice Assistant",
        "category": "AI Chat Bots",
        "description": "Turn spoken prompts into smart responses and summaries.",
        "icon": "mic",
        "color": "teal",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "study-assistant",
        "name": "Study Assistant",
        "category": "AI Chat Bots",
        "description": "Create study plans, explain topics, and test understanding.",
        "icon": "graduation-cap",
        "color": "fuchsia",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "business-assistant",
        "name": "Business Assistant",
        "category": "AI Chat Bots",
        "description": "Support planning, forecasting, and operational decisions.",
        "icon": "briefcase",
        "color": "sky",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "productivity-assistant",
        "name": "Personal Productivity Assistant",
        "category": "AI Chat Bots",
        "description": "Plan tasks, focus time blocks, and manage priorities.",
        "icon": "check-square",
        "color": "emerald",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "telegram-customer-support",
        "name": "Telegram Customer Support Bot",
        "category": "Telegram Bots",
        "description": "Handle customer inquiries, routing, and support automation.",
        "icon": "messages",
        "color": "blue",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "telegram-faq",
        "name": "Telegram FAQ Bot",
        "category": "Telegram Bots",
        "description": "Answer common questions and guide users through self-service flows.",
        "icon": "help-circle",
        "color": "purple",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "telegram-ai-chatbot",
        "name": "Telegram AI Chatbot",
        "category": "Telegram Bots",
        "description": "Deliver human-like conversations for communities and channels.",
        "icon": "bot",
        "color": "indigo",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "telegram-notification-bot",
        "name": "Telegram Notification Bot",
        "category": "Telegram Bots",
        "description": "Send alerts, events, and product updates directly to users.",
        "icon": "bell",
        "color": "amber",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "telegram-group-manager",
        "name": "Telegram Group Management Bot",
        "category": "Telegram Bots",
        "description": "Moderate groups, welcome users, and keep conversations organized.",
        "icon": "users",
        "color": "green",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "telegram-welcome-bot",
        "name": "Telegram Welcome Bot",
        "category": "Telegram Bots",
        "description": "Welcome new members and guide them through the onboarding journey.",
        "icon": "door-open",
        "color": "pink",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "telegram-reminder-bot",
        "name": "Telegram Reminder Bot",
        "category": "Telegram Bots",
        "description": "Create reminders for tasks, meetings, and follow-ups.",
        "icon": "alarm-clock",
        "color": "cyan",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "telegram-feedback-bot",
        "name": "Telegram Feedback Bot",
        "category": "Telegram Bots",
        "description": "Collect customer feedback with structured forms and summaries.",
        "icon": "message-square-text",
        "color": "orange",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "telegram-order-manager",
        "name": "Telegram Order Management Bot",
        "category": "Telegram Bots",
        "description": "Track orders, accept requests, and automate status updates.",
        "icon": "package",
        "color": "teal",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "website-chatbot",
        "name": "Website Chatbot",
        "category": "Website Automation",
        "description": "Turn your website into a smart AI help desk with instant answers.",
        "icon": "globe",
        "color": "violet",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "faq-responder",
        "name": "Automatic FAQ Responder",
        "category": "Website Automation",
        "description": "Answer repeated visitor questions with consistent, branded responses.",
        "icon": "list-checks",
        "color": "green",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "contact-form-assistant",
        "name": "Contact Form Assistant",
        "category": "Website Automation",
        "description": "Collect leads, classify requests, and route them correctly.",
        "icon": "mail",
        "color": "blue",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "appointment-booking-bot",
        "name": "Appointment Booking Bot",
        "category": "Website Automation",
        "description": "Set time slots, confirm appointments, and reduce friction.",
        "icon": "calendar-check",
        "color": "pink",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "seo-analysis-bot",
        "name": "SEO Analysis Bot",
        "category": "Website Automation",
        "description": "Audit technical and content SEO opportunities with practical actions.",
        "icon": "search-check",
        "color": "emerald",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "html-generator",
        "name": "HTML Code Generator",
        "category": "Developer Tools",
        "description": "Generate clean, production-ready HTML blocks and page sections.",
        "icon": "file-code",
        "color": "purple",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "css-generator",
        "name": "CSS Code Generator",
        "category": "Developer Tools",
        "description": "Create polished responsive styles from design prompts.",
        "icon": "paintbrush",
        "color": "cyan",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "javascript-generator",
        "name": "JavaScript Generator",
        "category": "Developer Tools",
        "description": "Generate functions, components, and UI logic quickly.",
        "icon": "terminal",
        "color": "amber",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "python-assistant",
        "name": "Python Code Assistant",
        "category": "Developer Tools",
        "description": "Draft scripts, fix logic issues, and explain Python patterns.",
        "icon": "python",
        "color": "blue",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "php-assistant",
        "name": "PHP Code Assistant",
        "category": "Developer Tools",
        "description": "Build backend flows, APIs, and web logic cleanly.",
        "icon": "server",
        "color": "indigo",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "debugging-assistant",
        "name": "Code Debugging Assistant",
        "category": "Developer Tools",
        "description": "Find root causes and propose safe fixes for bugs and errors.",
        "icon": "bug",
        "color": "red",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "api-tester",
        "name": "API Testing Assistant",
        "category": "Developer Tools",
        "description": "Draft request examples, validate inputs, and test flows.",
        "icon": "plug",
        "color": "emerald",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "json-formatter",
        "name": "JSON Formatter",
        "category": "Developer Tools",
        "description": "Beautify, validate, and convert structured data quickly.",
        "icon": "braces",
        "color": "pink",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "regex-generator",
        "name": "Regex Generator",
        "category": "Developer Tools",
        "description": "Create and explain patterns for validation and parsing tasks.",
        "icon": "regex",
        "color": "violet",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "website-generator",
        "name": "Website Generator",
        "category": "Developer Tools",
        "description": "Generate full landing page sections from brief specifications.",
        "icon": "layout-template",
        "color": "sky",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "business-name-generator",
        "name": "Business Name Generator",
        "category": "Business Bots",
        "description": "Generate memorable, relevant business names and brand ideas.",
        "icon": "building",
        "color": "purple",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "sales-assistant",
        "name": "Sales Assistant",
        "category": "Business Bots",
        "description": "Draft sales messages, outreach, and conversion strategy support.",
        "icon": "sales",
        "color": "blue",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "invoice-generator",
        "name": "Invoice Generator",
        "category": "Business Bots",
        "description": "Create invoice drafts, totals, and customer billing summaries.",
        "icon": "receipt",
        "color": "emerald",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "marketing-assistant",
        "name": "Marketing Assistant",
        "category": "Business Bots",
        "description": "Build campaigns, customer journeys, and ad copy ideas.",
        "icon": "megaphone",
        "color": "pink",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "social-caption-generator",
        "name": "Social Media Caption Generator",
        "category": "Social Media Bots",
        "description": "Write captions, hooks, and CTAs for every platform.",
        "icon": "caption",
        "color": "violet",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "hashtag-generator",
        "name": "Hashtag Generator",
        "category": "Social Media Bots",
        "description": "Generate trend-aware hashtags for better discoverability.",
        "icon": "hash",
        "color": "cyan",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "content-idea-generator",
        "name": "Content Idea Generator",
        "category": "Social Media Bots",
        "description": "Plan themes, hooks, and campaign directions for your content calendar.",
        "icon": "lightbulb",
        "color": "amber",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "comment-moderator",
        "name": "Comment Moderation Assistant",
        "category": "Social Media Bots",
        "description": "Review comments and recommend safe moderation responses.",
        "icon": "shield-check",
        "color": "green",
        "status": "Available",
        "tier": "Business",
    },
    {
        "id": "security-checklist",
        "name": "Website Security Checklist",
        "category": "Security & Testing",
        "description": "Review defensive best practices and security posture suggestions.",
        "icon": "shield",
        "color": "teal",
        "status": "Available",
        "tier": "Enterprise",
    },
    {
        "id": "password-strength-checker",
        "name": "Password Strength Checker",
        "category": "Security & Testing",
        "description": "Assess password policies and resilience for common attacks.",
        "icon": "key",
        "color": "blue",
        "status": "Available",
        "tier": "Enterprise",
    },
    {
        "id": "ssl-checker",
        "name": "SSL Certificate Checker",
        "category": "Security & Testing",
        "description": "Review HTTPS readiness and certificate risk indicators.",
        "icon": "certificate",
        "color": "purple",
        "status": "Available",
        "tier": "Enterprise",
    },
    {
        "id": "safe-url-scanner",
        "name": "Safe URL Scanner",
        "category": "Security & Testing",
        "description": "Assess links for suspicious characteristics and safety warnings.",
        "icon": "scan-search",
        "color": "indigo",
        "status": "Available",
        "tier": "Enterprise",
    },
    {
        "id": "uptime-monitor",
        "name": "Website Uptime Monitor",
        "category": "Security & Testing",
        "description": "Monitor indicators for service reliability and downtime checks.",
        "icon": "activity",
        "color": "green",
        "status": "Available",
        "tier": "Enterprise",
    },
    {
        "id": "pdf-summarizer",
        "name": "PDF Summarizer",
        "category": "File & Documents",
        "description": "Generate concise executive summaries from uploaded PDFs.",
        "icon": "file-text",
        "color": "red",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "document-converter",
        "name": "Document Converter",
        "category": "File & Documents",
        "description": "Convert documents between common formats for workflow efficiency.",
        "icon": "arrows-left-right",
        "color": "cyan",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "ocr-assistant",
        "name": "Image-to-Text OCR",
        "category": "File & Documents",
        "description": "Extract readable text from uploaded images and scanned documents.",
        "icon": "ocr",
        "color": "amber",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "cv-generator",
        "name": "CV / Resume Generator",
        "category": "File & Documents",
        "description": "Create tailored resume content from your experience and goals.",
        "icon": "user-circle",
        "color": "purple",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "notes-assistant",
        "name": "Notes Assistant",
        "category": "File & Documents",
        "description": "Organize notes, meeting summaries, and personal knowledge.",
        "icon": "sticky-note",
        "color": "pink",
        "status": "Available",
        "tier": "Pro",
    },
    {
        "id": "story-generator",
        "name": "Story Generator",
        "category": "Entertainment",
        "description": "Create short stories, plot prompts, and fictional worlds.",
        "icon": "book",
        "color": "violet",
        "status": "Available",
        "tier": "Free",
    },
    {
        "id": "joke-generator",
        "name": "Joke Generator",
        "category": "Entertainment",
        "description": "Generate lighthearted jokes and playful content ideas.",
        "icon": "laugh",
        "color": "amber",
        "status": "Available",
        "tier": "Free",
    },
    {
        "id": "quiz-bot",
        "name": "Quiz Bot",
        "category": "Entertainment",
        "description": "Generate quizzes for fun, training, or engagement.",
        "icon": "question-mark",
        "color": "indigo",
        "status": "Available",
        "tier": "Free",
    },
    {
        "id": "movie-recommendation",
        "name": "Movie Recommendation Assistant",
        "category": "Entertainment",
        "description": "Recommend films based on mood, genre, and interests.",
        "icon": "film",
        "color": "orange",
        "status": "Available",
        "tier": "Free",
    },
    {
        "id": "game-idea-generator",
        "name": "Game Idea Generator",
        "category": "Entertainment",
        "description": "Brainstorm game mechanics, themes, and design ideas.",
        "icon": "gamepad",
        "color": "green",
        "status": "Available",
        "tier": "Free",
    },
]


CATEGORY_ORDER = [
    "AI Chat Bots",
    "Telegram Bots",
    "Website Automation",
    "Developer Tools",
    "Business Bots",
    "Social Media Bots",
    "Security & Testing",
    "File & Documents",
    "Entertainment",
]


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            bot_id TEXT NOT NULL,
            bot_name TEXT NOT NULL,
            title TEXT NOT NULL,
            messages TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS activity_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT NOT NULL,
            description TEXT NOT NULL,
            details TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """
    )
    conn.commit()
    conn.close()

    seed_bots_table()


def seed_bots_table():
    conn = get_db_connection()
    existing = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='bots'").fetchone()[0]
    if existing == 0:
        conn.execute(
            """
            CREATE TABLE bots (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                icon TEXT,
                color TEXT,
                status TEXT,
                tier TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
    for bot in DEFAULT_BOTS:
        conn.execute(
            """
            INSERT OR REPLACE INTO bots (id, name, category, description, icon, color, status, tier)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                bot["id"],
                bot["name"],
                bot["category"],
                bot["description"],
                bot["icon"],
                bot["color"],
                bot["status"],
                bot["tier"],
            ),
        )
    conn.commit()
    conn.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/bots")
def api_bots():
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT id, name, category, description, icon, color, status, tier FROM bots ORDER BY category, name"
    ).fetchall()
    conn.close()
    bots = [dict(row) for row in rows]
    return jsonify({"success": True, "bots": bots, "categories": CATEGORY_ORDER})


@app.route("/api/dashboard")
def api_dashboard():
    conn = get_db_connection()
    users_count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    active_count = conn.execute(
        "SELECT COUNT(DISTINCT user_id) FROM activity_logs WHERE created_at >= datetime('now', '-7 days')"
    ).fetchone()[0]
    bot_usage = conn.execute("SELECT COUNT(*) FROM conversations").fetchone()[0]
    api_usage = conn.execute(
        "SELECT COUNT(*) FROM activity_logs WHERE type IN ('chat', 'tool_run', 'api_call')"
    ).fetchone()[0]
    logs = conn.execute(
        "SELECT type, description, created_at FROM activity_logs ORDER BY id DESC LIMIT 8"
    ).fetchall()
    conn.close()
    return jsonify(
        {
            "success": True,
            "stats": {
                "registered_users": users_count,
                "active_users": active_count,
                "bot_usage": bot_usage,
                "api_usage": api_usage,
                "subscriptions": 328,
                "system_uptime": "99.94%",
            },
            "logs": [dict(item) for item in logs],
        }
    )


@app.route("/api/system-status")
def api_system_status():
    return jsonify(
        {
            "success": True,
            "status": "online",
            "message": "Platform healthy",
            "version": "1.0.0",
            "database": "sqlite",
            "provider": os.environ.get("MODEL_PROVIDER", "local").lower(),
        }
    )


@app.route("/api/auth/register", methods=["POST"])
def register_user():
    payload = request.get_json(silent=True) or {}
    name = (payload.get("name") or "").strip()
    email = (payload.get("email") or "").strip().lower()
    password = payload.get("password") or ""

    if not name or not email or len(password) < 6:
        return jsonify({"success": False, "message": "Please provide a valid name, email, and password with at least 6 characters."}), 400

    conn = get_db_connection()
    existing = conn.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()
    if existing:
        conn.close()
        return jsonify({"success": False, "message": "An account with that email already exists."}), 409

    password_hash = generate_password_hash(password)
    cur = conn.execute(
        "INSERT INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)",
        (name, email, password_hash, "user"),
    )
    user_id = cur.lastrowid
    conn.execute(
        "INSERT INTO activity_logs (user_id, type, description, details) VALUES (?, ?, ?, ?)",
        (user_id, "register", "User created account", json.dumps({"email": email})),
    )
    conn.commit()
    user = {
        "id": user_id,
        "name": name,
        "email": email,
        "role": "user",
    }
    session["user_id"] = user_id
    session["user_name"] = name
    session["user_role"] = "user"
    conn.close()
    return jsonify({"success": True, "user": user, "message": "Account created successfully."})


@app.route("/api/auth/login", methods=["POST"])
def login_user():
    payload = request.get_json(silent=True) or {}
    email = (payload.get("email") or "").strip().lower()
    password = payload.get("password") or ""

    if not email or not password:
        return jsonify({"success": False, "message": "Email and password are required."}), 400

    conn = get_db_connection()
    user_row = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    if not user_row:
        conn.close()
        return jsonify({"success": False, "message": "Invalid email or password."}), 401

    if not check_password_hash(user_row["password_hash"], password):
        conn.close()
        return jsonify({"success": False, "message": "Invalid email or password."}), 401

    user = {
        "id": user_row["id"],
        "name": user_row["name"],
        "email": user_row["email"],
        "role": user_row["role"],
    }
    session["user_id"] = user_row["id"]
    session["user_name"] = user_row["name"]
    session["user_role"] = user_row["role"]
    conn.execute(
        "INSERT INTO activity_logs (user_id, type, description, details) VALUES (?, ?, ?, ?)",
        (user_row["id"], "login", "User logged in", json.dumps({"email": email})),
    )
    conn.commit()
    conn.close()
    return jsonify({"success": True, "user": user, "message": "Logged in successfully."})


@app.route("/api/auth/me")
def auth_me():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"success": True, "user": None})

    conn = get_db_connection()
    row = conn.execute("SELECT id, name, email, role FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    if not row:
        session.clear()
        return jsonify({"success": True, "user": None})

    user = {"id": row["id"], "name": row["name"], "email": row["email"], "role": row["role"]}
    return jsonify({"success": True, "user": user})


@app.route("/api/auth/logout", methods=["POST"])
def logout_user():
    session.clear()
    return jsonify({"success": True, "message": "Logged out successfully."})


@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True) or {}
    bot_id = payload.get("bot_id") or "general-ai"
    prompt = (payload.get("prompt") or "").strip()
    if not prompt:
        return jsonify({"success": False, "message": "Please enter a prompt."}), 400

    bot = get_bot_details(bot_id)
    response = generate_bot_response(bot_id, prompt)

    if session.get("user_id"):
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO activity_logs (user_id, type, description, details) VALUES (?, ?, ?, ?)",
            (session["user_id"], "chat", f"Used {bot['name']}", json.dumps({"bot_id": bot_id, "prompt": prompt})),
        )
        conn.commit()
        conn.close()

    return jsonify({"success": True, "bot": bot, "response": response})


@app.route("/api/conversations")
def conversations():
    if not session.get("user_id"):
        return jsonify({"success": True, "conversations": []})

    conn = get_db_connection()
    rows = conn.execute(
        "SELECT id, bot_id, bot_name, title, messages, created_at FROM conversations WHERE user_id = ? ORDER BY updated_at DESC LIMIT 10",
        (session["user_id"],),
    ).fetchall()
    conn.close()
    return jsonify({"success": True, "conversations": [dict(row) for row in rows]})


@app.route("/api/favorites")
def favorites():
    return jsonify({"success": True, "favorites": ["general-ai", "coding-assistant", "website-generator"]})


def get_bot_details(bot_id):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT id, name, category, description, icon, color, status, tier FROM bots WHERE id = ?",
        (bot_id,),
    ).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {
        "id": bot_id,
        "name": "Custom Bot",
        "category": "General",
        "description": "AI-powered workflow assistant",
        "icon": "sparkles",
        "color": "purple",
        "status": "Available",
        "tier": "Pro",
    }


def generate_bot_response(bot_id, prompt):
    bot = get_bot_details(bot_id)
    lowered_prompt = prompt.lower()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if bot_id == "coding-assistant" or "code" in lowered_prompt:
        return {
            "title": "Code Solution",
            "summary": f"Generated a practical implementation for: {prompt}",
            "output": "```python\ndef build_feature(prompt):\n    # Production-minded implementation\n    return {\n        'task': prompt,\n        'status': 'ready',\n        'next_step': 'validate with tests and user feedback'\n    }\n```\n\nThis gives you a clean starting point, and you can refine it for your specific stack and architecture.",
            "status": "success",
            "timestamp": now,
        }

    if bot_id == "general-ai" or "idea" in lowered_prompt or "strategy" in lowered_prompt:
        return {
            "title": "AI Insight",
            "summary": f"Here is a structured response to your request: {prompt}",
            "output": (
                "1. Clarify the goal and target audience.\n"
                "2. Break the task into small, measurable outcomes.\n"
                "3. Build the first version with rapid feedback loops.\n"
                "4. Instrument results and iterate based on real usage.\n"
                "5. Keep the user experience simple, fast, and trustworthy."
            ),
            "status": "success",
            "timestamp": now,
        }

    if bot_id == "writing-assistant" or "write" in lowered_prompt or "email" in lowered_prompt:
        return {
            "title": "Draft Copy",
            "summary": "Here is a polished draft based on your prompt.",
            "output": (
                f"Subject: {prompt[:30]}\n\n"
                "Hello,\n\n"
                "Thanks for your interest. We’ve designed a streamlined solution focused on efficiency, clarity, and measurable results. "
                "The approach is intended to save time, improve user experience, and create a strong foundation for ongoing growth.\n\n"
                "We would be happy to share more details and align the plan to your goals.\n\n"
                "Best regards,\n"
                "Timi AI Hub Team"
            ),
            "status": "success",
            "timestamp": now,
        }

    if bot_id == "translation-bot":
        return {
            "title": "Translation Output",
            "summary": "Translated content with a natural tone.",
            "output": "English: " + prompt + "\n\nSpanish: " + "Gracias por tu mensaje. Estamos listos para ayudarte y apoyarte en cada paso del proceso.",
            "status": "success",
            "timestamp": now,
        }

    if bot_id == "math-assistant":
        return {
            "title": "Math Solution",
            "summary": "A step-by-step approach to the problem.",
            "output": "Let the goal be to simplify the expression and validate the logic.\n\nStep 1: Identify the core variables and operations.\nStep 2: Apply the correct formula.\nStep 3: Simplify carefully and verify the result.\nStep 4: Check whether the answer fits the original conditions.",
            "status": "success",
            "timestamp": now,
        }

    if bot_id in {"html-generator", "css-generator", "javascript-generator", "website-generator"}:
        lang = "HTML"
        if bot_id == "css-generator":
            lang = "CSS"
        elif bot_id == "javascript-generator":
            lang = "JavaScript"
        elif bot_id == "website-generator":
            lang = "Landing Page"

        return {
            "title": f"{lang} Output",
            "summary": f"Generated implementation for: {prompt}",
            "output": f"```{lang.lower()}\n/* Generated by Timi AI Hub */\n" + "\n".join([
                "* { box-sizing: border-box; }",
                ".container { max-width: 1200px; margin: 0 auto; padding: 2rem; }",
                "body { font-family: 'Inter', sans-serif; background: #0b1020; color: white; }",
                ".card { background: rgba(15, 23, 42, 0.8); border-radius: 18px; padding: 1.5rem; }",
            ]) + "\n```",
            "status": "success",
            "timestamp": now,
        }

    if bot_id in {"security-checklist", "password-strength-checker", "ssl-checker", "safe-url-scanner", "uptime-monitor"}:
        return {
            "title": "Security Review",
            "summary": "Defensive security guidance based on the prompt.",
            "output": (
                "Security review summary:\n"
                "- Enforce strong authentication and least-privilege access.\n"
                "- Validate HTTPS, certificate health, and secure headers.\n"
                "- Lock down sensitive configs and avoid exposing secrets in client code.\n"
                "- Run authorized audits and defensive testing only.\n"
                "- Implement logging and monitoring for suspicious behavior."
            ),
            "status": "success",
            "timestamp": now,
        }

    if bot_id == "story-generator" or "story" in lowered_prompt:
        return {
            "title": "Story Draft",
            "summary": "A creative starter narrative inspired by your brief.",
            "output": "The city glowed under the midnight rain as a quiet inventor discovered a map hidden inside an old mechanical clock. With each turn of the gears, the city changed shape, revealing a path toward a forgotten future. She followed the light, not knowing that it was leading her to a power that could either save her world or rewrite it forever.",
            "status": "success",
            "timestamp": now,
        }

    if bot_id == "joke-generator":
        return {
            "title": "Joke",
            "summary": "A small laugh to lighten the day.",
            "output": "Why do developers prefer dark mode? Because light attracts bugs.",
            "status": "success",
            "timestamp": now,
        }

    if bot_id == "quiz-bot" or "quiz" in lowered_prompt:
        return {
            "title": "Quiz",
            "summary": "A quick, engaging quiz prompt.",
            "output": "1. Which of the following is most important for a good AI user experience?\nA. Speed\nB. Clarity\nC. Trust\nD. All of the above\n\nCorrect answer: D. All of the above.",
            "status": "success",
            "timestamp": now,
        }

    if bot_id == "pdf-summarizer" or "pdf" in lowered_prompt:
        return {
            "title": "Document Summary",
            "summary": "A concise executive summary from your document.",
            "output": "This document highlights the core business priorities, expected outcomes, and action items for the next phase. It recommends a phased rollout, close monitoring of results, and a feedback-driven approach for continuous improvement.",
            "status": "success",
            "timestamp": now,
        }

    if bot_id in {"cv-generator", "document-converter", "ocr-assistant", "notes-assistant"}:
        return {
            "title": "Document Workflow",
            "summary": "Here is a practical document workflow for your task.",
            "output": (
                "- Define the objective and audience.\n"
                "- Gather the most relevant content.\n"
                "- Draft a clear first version.\n"
                "- Revise for accuracy and clarity.\n"
                "- Export in the required format and share for review."
            ),
            "status": "success",
            "timestamp": now,
        }

    return {
        "title": bot["name"],
        "summary": "Prepared a tailored response for your prompt.",
        "output": (
            "This workflow is designed to deliver fast results while staying practical and user-focused.\n\n"
            f"Input: {prompt}\n\n"
            "Recommended next steps:\n"
            "- Validate the objective and target outcome.\n"
            "- Build a simple first pass.\n"
            "- Review the result with real users.\n"
            "- Improve iteratively based on feedback."
        ),
        "status": "success",
        "timestamp": now,
    }


init_db()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
