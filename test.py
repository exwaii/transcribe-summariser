import requests

import re

full_html = requests.get("YOUR YOUTUBE LINK HERE").text
y = re.search(r'shortDescription":"', full_html)
desc = ""
count = y.start() + 19  # adding the length of the 'shortDescription":"
while True:
    # get the letter at current index in text
    letter = full_html[count]
    if letter == "\"":
        if full_html[count - 1] == "\\":
            # this is case where the letter before is a backslash, meaning it is not real end of description
            desc += letter
            count += 1
        else:
            break
    else:
        desc += letter
        count += 1

print(f'description: {desc}')