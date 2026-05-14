import json
import random
import requests
import pickle
from googleapiclient.discovery import build

from config import BLOG_ID, OPENROUTER_API_KEY, AUTHOR_NAME

# LOAD KEYWORDS
with open("keywords.json", "r") as f:
    keywords = json.load(f)

keyword = random.choice(keywords)

# AI PROMPT
prompt = f"""
Write a cinematic SEO optimized blog article about:
{keyword}

Requirements:
- Emotional tone
- SEO headings
- Human sounding
- 800 words
- Mention author: {AUTHOR_NAME}
- Include FAQ section
- Add conclusion
"""

# CALL FREE AI
response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
)

data = response.json()

article = data["choices"][0]["message"]["content"]

# CREATE JSON-LD
schema = f"""
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"BlogPosting",
  "headline":"{keyword}",
  "author":{{
    "@type":"Person",
    "name":"{AUTHOR_NAME}"
  }}
}}
</script>
"""

html_content = f"""
<h1>{keyword}</h1>

{article}

{schema}
"""

# LOAD AUTH TOKEN
with open('token.pickle', 'rb') as token:
    creds = pickle.load(token)

service = build('blogger', 'v3', credentials=creds)

post = {
    "title": keyword,
    "content": html_content
}

result = service.posts().insert(
    blogId=BLOG_ID,
    body=post,
    isDraft=False
).execute()

print("POST PUBLISHED")
print(result["url"])
