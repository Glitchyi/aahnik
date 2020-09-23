import os
import yaml

images = [file[:-4] for file in os.listdir('social_media_logos') if file.endswith('.png') ]

with open('social_media_logos/links.yml') as f:
    link_dict = yaml.full_load(f)

with open('social.md','w+') as f:
    for img in images:
        link = link_dict[img]
        template = f'[![{img}](https://github.com/aahnik/aahnik/blob/master/social_media_logos/{img}.png?raw=true)]({link})\n'
        
        f.write('<center>')
        f.write(template)
        f.write('</center>')


