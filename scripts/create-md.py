pip install pyaml
import json
import yaml
import os

# Load the JSON file
with open('events.json') as f:
    data = json.load(f)

# Iterate through each object in the JSON array
for item in data:
    # Create an empty dictionary for the front matter
    front_matter = {}

    # Add the 'title' and 'prog_date' key-value pairs to the front matter
    front_matter['title'] = item['title']
    front_matter['prog_date'] = item['prog_date']

    # Add the 'category' key-value pair to the front matter
    front_matter['category'] = item['prog_type']

    # Iterate through the remaining key-value pairs in the JSON object and add them to the front matter
    for key, value in item.items():
        if key not in ['title', 'prog_date', 'prog_type']:
            front_matter[key] = value
    year = item['prog_date'].split('-')[0]
    year_folder = os.path.join('content', year)
    os.makedirs(year_folder, exist_ok=True)

    # Write the front matter and markdown content to a file inside the year folder
    with open(os.path.join(year_folder, item['id'] + '.md'), 'w') as f:
        # Write the front matter as YAML formatted text
        f.write('---\n')
        f.write('title: {}\n'.format(front_matter['title']))
        f.write('prog_date: {}\n'.format(front_matter['prog_date']))
        for key, value in front_matter.items():
            if key not in ['title', 'prog_date']:
                f.write('{}: {}\n'.format(key, value))
        f.write('---\n\n')

import shutil
shutil.make_archive("content-zipped", 'zip', "content")
