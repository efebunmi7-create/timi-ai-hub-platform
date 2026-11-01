# Timi AI Hub Platform

Timi AI Hub is a modern AI SaaS-style platform that brings together AI assistants, automation tools, productivity bots, developer tools, business utilities, security checks, and entertainment bots in one dashboard.

This project is designed to be open source, easy to self-host, and ready for deployment on a public cloud platform.

Features
- AI chat bots and productivity tools
- Telegram and website automation bots
- Developer utilities for HTML, CSS, JS, Python, and more
- Business, social, security, and document automation tools
- Admin dashboard and user dashboard
- SQLite-backed local storage
- Python Flask backend
- Responsive dark futuristic interface

Live demo
- Public GitHub repo: https://github.com/efebunmi7-create/timi-ai-hub-platform
- Deploy this app to a public hosting service for a live website

Project status
- Frontend prototype and interactive dashboard included
- Backend APIs for auth, bots, dashboard stats, and chat flow included
- Ready for extension with OpenAI/Gemini integrations and real production database

Tech stack
- Python / Flask
- SQLite
- HTML / CSS / JavaScript
- Gunicorn for production deployment

Repository structure
- app.py: Flask application and API routes
- static/: frontend assets
- templates/: HTML templates
- requirements.txt: Python dependencies
- .env.example: sample environment variables
- LICENSE: MIT license

Quick start

1. Clone the repo

```bash
git clone https://github.com/efebunmi7-create/timi-ai-hub-platform.git
cd timi-ai-hub-platform
```

2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
py -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure environment

```bash
cp .env.example .env
```

Edit `.env` and set values like:

```env
SECRET_KEY=your-secret-key
DATABASE_PATH=timi_ai_hub.db
OPENAI_API_KEY=
GEMINI_API_KEY=
MODEL_PROVIDER=local
PORT=5000
```

5. Run the app locally

```bash
python app.py
```

Then open:

```text
http://localhost:5000
```

Deployment options

Option A: Render (recommended for simple public deployment)
1. Push this repo to GitHub.
2. Create a new Web Service on Render.
3. Connect the repository.
4. Set the build command:

```bash
pip install -r requirements.txt
```

5. Set the start command:

```bash
gunicorn app:app
```

6. Add environment variables in Render dashboard.
7. Deploy.

Option B: Railway
1. Import the repo into Railway.
2. Configure Python environment.
3. Set port to 5000 or your chosen port.
4. Add required env vars.
5. Deploy.

Option C: GitHub Pages
- GitHub Pages is only for static front-end hosting.
- It cannot run a Python Flask backend or SQLite database directly.
- Use GitHub Pages only for a landing page or documentation site.
- For the actual app, use Render/Railway/Heroku/VPS.

Open source guidance
- This repository is open source.
- Keep the code public if you want community access.
- Add issues, pull requests, and discussion features in GitHub for contributions.
- Keep secret keys on the server and never expose them in frontend JavaScript.
- Make sure any third-party API integrations are documented.

License
This project is open source under the MIT License. See `LICENSE` for details.

Contributing
Contributions are welcome.

Please:
- create a branch for your change
- add tests where possible
- keep code clean and documented
- avoid exposing private keys or secrets

Security notice
This project includes defensive security tools only. It does not support unauthorized access, credential attacks, spam, malware, or service disruption.

Support
If you want help:
- open an issue in GitHub
- describe the problem clearly
- include steps to reproduce
- mention your environment

