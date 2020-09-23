import os
import yaml

images = [file[:-4] for file in os.listdir('social_media_logos') if file.endswith('.png') ]

with open('social_media_logos/links.yml') as f:
    link_dict = yaml.full_load(f)


with open('social.md','w+') as f:
    f.write('<center>\n\n')
    for img in images:
        link = link_dict[img]
        
        img_url = f'https://github.com/aahnik/aahnik/blob/master/social_media_logos/{img}.png?raw=true'
        template = f'<a href = "{link}" > <img src = "{img_url}" alt = "{img}" > </a >'
        f.write(f'{template}\n')

    f.write('\n\n</center>')





