#!/usr/bin/python3.8

import os
import yaml


with open('social_links.yml') as f:
    link_dict = yaml.full_load(f)

with open('svg_assets/README.md') as f:
    readme = f.read()+'\n'

with open('social.md', 'w+') as f:
    f.write(readme)
    for img_name, link in link_dict.items():
        img_url = f'https://github.com/aahnik/aahnik/blob/master/svg_assets/{img_name}.svg?raw=true'
        template = f'<a href = "{link}" > <img src = "{img_url}" alt = "{img_name}" width=35> </a>'
        f.write(f'{template}\n')
