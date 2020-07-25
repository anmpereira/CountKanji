import tika
import numpy as np
import string
from tika import parser
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

tika.initVM()

parsed = parser.from_file('data\\test.pdf')
content = parsed["content"]

katakana_chart = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポ" \
                 "マミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾー"
hiragana_chart = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼ" \
                 "ぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
punctuation = '、。「」…―！？』『※'

words = content.split()
stop_words = katakana_chart + hiragana_chart + punctuation + string.ascii_lowercase + string.ascii_uppercase
words = [word for word in words if word not in stop_words]
labels, counts = np.unique(words, return_counts=True)

ordered_counts = np.sort(counts)[::-1]
ordered_labels = labels[ordered_counts]

index_max = 30
indexes = np.arange(len(ordered_labels[:index_max]))
plt.bar(indexes, ordered_counts[:index_max])
# add labels
bar_width = 0.35

ChineseFont1 = FontProperties(fname='C:\\Windows\\Fonts\\simsun.ttc', size=16)
plt.xticks(indexes, ordered_labels[:index_max], fontproperties=ChineseFont1)
plt.show()
