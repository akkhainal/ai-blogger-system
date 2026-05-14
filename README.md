# AI Auto Blogger System (Free Version)

This system:
- Generates SEO blog posts using a free AI API
- Adds JSON-LD schema
- Publishes automatically to Blogger
- Runs daily using GitHub Actions

---

# STEP 1 — Install Python

Download:
https://www.python.org/downloads/

During install:
✔ Add Python to PATH

---

# STEP 2 — Create GitHub Account

https://github.com

Create a new repository:
Example:
ai-blogger-system

---

# STEP 3 — Enable Blogger API

Open:
https://console.cloud.google.com/

Then:

1. Create Project
2. APIs & Services
3. Enable APIs
4. Search:
   Blogger API v3
5. Enable it

---

# STEP 4 — Create OAuth Credentials

Inside Google Cloud:

APIs & Services
→ Credentials
→ Create Credentials
→ OAuth Client ID

Choose:
Desktop App

Download the credentials JSON.

Rename it:
client_secret.json

Place inside project folder.

---

# STEP 5 — Install Dependencies

Open terminal in project folder:

pip install -r requirements.txt

---

# STEP 6 — Run Authentication Once

Run:

python auth.py

Browser open hoga.
Google login karo.

Ye file create karega:
token.json

IMPORTANT:
token.json ko safe rakho.

---

# STEP 7 — Get Blogger ID

Open your Blogger dashboard.

URL example:
https://www.blogger.com/blog/posts/1234567890123456789

The long number = BLOG_ID

Open config.py
Paste your BLOG_ID.

---

# STEP 8 — Add Free AI API

Open:
https://openrouter.ai/

Create free account.

Get API key.

Open config.py
Paste API key.

---

# STEP 9 — Test Publishing

Run:

python main.py

Agar sab sahi hua:
automatic blog publish ho jayega.

---

# STEP 10 — Push To GitHub

Upload all files to GitHub repository.

---

# STEP 11 — Enable GitHub Actions

GitHub repo:
Settings
→ Actions
→ Enable

---

# STEP 12 — Add Secrets

GitHub:
Settings
→ Secrets and Variables
→ Actions

Add:

OPENROUTER_API_KEY

---

# STEP 13 — Automatic Daily Posting

GitHub Actions automatically daily post karega.

Schedule file:
.github/workflows/auto_post.yml

Current:
8 AM UTC

---

# CONTENT CUSTOMIZATION

Edit:
keywords.json

Add your own keywords.

---

# IMPORTANT

Avoid spam.

Focus on:
- emotional storytelling
- cinematic tone
- author branding
- semantic SEO

