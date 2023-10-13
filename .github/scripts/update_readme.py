import json

# Read the metadata.json file
with open("metadata.json", "r") as f:
    data = json.load(f)

# Create a markdown table header
table = "| Name | Source Name | Source URL |\n"
table += "|------|-------------|------------|\n"

# Populate the table rows with the 'name' and 'source' information
for item in data:
    name = item["name"]
    source_name = item["source"]["name"]
    source_url = item["source"]["url"]
    table += f"| {name} | {source_name} | [Link]({source_url}) |\n"

# Update the README.md file
readme_path = "README.md"
with open(readme_path, "r") as file:
    readme_content = file.readlines()

insert_index = readme_content.index("# Models\n") + 1
readme_content = readme_content[:insert_index] + [table] + readme_content[insert_index:]

# Write the updated content back to README.md
with open(readme_path, "w") as file:
    file.writelines(readme_content)
