# .github/scripts/update_readme.py
import json

# Load metadata.json
with open('metadata.json', 'r') as f:
    data = json.load(f)

# Construct the table for README.md
table = """
| Name | Source Name | Source URL |
|------|-------------|------------|
"""

for entry in data:
    table += f"| {entry['name']} | {entry['source']['name']} | [{entry['source']['url']}]({entry['source']['url']}) |\n"

# Update README.md
with open('README.md', 'w') as f:
    f.write(table)
