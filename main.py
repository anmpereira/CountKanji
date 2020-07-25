import tika
import numpy as np
import string
from tika import parser

tika.initVM()

parsed = parser.from_file('data\\N2267BE.pdf')
content = parsed["content"]

katakana_chart = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポ"\
                "マミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾー"
hiragana_chart = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼ"\
                 "ぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
punctuation = '、。「」…―！？』『'

words = content.split()
stop_words = katakana_chart + hiragana_chart + punctuation + string.ascii_lowercase + string.ascii_uppercase
words = [word for word in words if word not in stop_words]
labels, counts = np.unique(words, return_counts=True)

print([x for _, x in sorted(zip(counts, labels))][::-1])
print(sorted(counts)[::-1])
