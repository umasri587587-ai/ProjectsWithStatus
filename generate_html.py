import requests
import json
from datetime import datetime

# Configuration
PORTAL_ID = "421253000000080067"
ACCESS_TOKEN = "1000.b1b9df9b57437c9b4386787f39e1d502.4ad77e21a08b9c0f94e5c09947e585a5"
GITHUB_TOKEN = "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"
REPO = "umasri587587-ai/ProjectsWithStatus"

# Fetch projects
url = f"https://projectsapi.zoho.in/restapi/portal/{PORTAL_ID}/projects/?range=1000"
headers = {"Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}"}
response = requests.get(url, headers=headers)
projects = response.json()

# Generate HTML (use your Deluge HTML template)
html = generate_html(projects)  # Your HTML generation logic
