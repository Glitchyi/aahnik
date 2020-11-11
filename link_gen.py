import os
import yaml


with open('social_links.yml') as f:
    link_dict = yaml.full_load(f)


with open('social.md','w+') as f:
    for img_name,link in link_dict.items():
        img_url = f'https://github.com/aahnik/aahnik/blob/master/svg_assets/{img}.svg?raw=true'
        template = f'<a href = "{link}" > <img src = "{img_url}" alt = "{img} width=50" > </a >'
        f.write(f'{template}\n\n')

