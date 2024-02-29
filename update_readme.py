import os

markdown_files = [file for file in os.listdir('.') if file.endswith('.md')]

print('Skipping README.md')  # Added print statement for clarity

for file_name in markdown_files:
    if file_name == 'README.md':
        continue
    with open(file_name, 'r') as md_file:
        content = md_file.read()
    with open('README.md', 'a') as readme:
        readme.write(f"## {file_name}\n\n")
        readme.write(content)
        readme.write('\n\n---\n\n')  # Separation between files
