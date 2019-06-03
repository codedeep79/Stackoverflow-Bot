# -*- coding: utf-8 -*-
import os, json

template='''# All Stackoverflow Tag List

Ever wish there was a curated list for your curated lists, including other curated lists of curated lists that may or may not contain other curated lists?

``` python
print('A Stackoverflow Tag List ' + ('Stackoverflow Tag List of '*∞) + 'Stackoverflow Tag List.')
```

_Updated as often as I can. Want to contribute? Go ahead and make a pull request._

- [x] Index top 10000 Stackoverflow Tag List.
- [x] Make a bot do it for me
- [x] Automate the curation entirely
- [ ] Organize lists
- [ ] Create easy search for lists.

# Stackoverflow Tag List (Some data)

'''


with open('README.md','w') as tag_list_md:
    tag_list_md.write(template)
    with open('README.json','r') as tag_list_json:
        tag_lists = json.load(tag_list_json)
        count = 1
        for tag_list in tag_lists:
            tag_list_md.write('__{}. [{}]({})__: {}\n\n'.format(
                count,
                tag_list['tagName'],
                'https://stackoverflow.com/questions/tagged/' + tag_list['tagName'],
                tag_list['descriptionTag'].capitalize()
            ))
            count = count + 1
            if count == 11001:
				break;
