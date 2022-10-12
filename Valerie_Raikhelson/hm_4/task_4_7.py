from collections import Counter
import re

text = 'one!'
reg = re.compile('[^a-zA-Z ]')

text_from_let = sorted(reg.sub('', text).replace(' ', '').lower())

el_count = Counter(list(text_from_let))
print(el_count)

for let, count in el_count.items():
    if count == max(el_count.values()):
        print(let)
        break
