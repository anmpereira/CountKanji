import tika
import numpy as np
import string
from tika import parser
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# start virtual machine to run TIKA
tika.initVM()
parsed = parser.from_file('data\\test2.pdf')
content = parsed["content"]

# Create ignore list
katakana_chart = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポ" \
                 "マミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾー"
hiragana_chart = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼ" \
                 "ぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
punctuation = '、。「」…―！？』『※【】≪≫・'
numbers = '0123456789'
latin = str([chr(65280 + x) for x in range(0, 91)])

# filter and sort
words = content.split()
stop_words = katakana_chart + hiragana_chart + punctuation + string.ascii_letters + numbers + latin
words = [word for word in words if word not in stop_words]
labels, counts = np.unique(words, return_counts=True)

indSort = np.argsort(counts)[::-1]
ordered_counts = counts[indSort]
ordered_labels = labels[indSort]

# Analysis and plots
print('There are {:d} unique Kanji'.format(len(counts)))
percentages = ordered_counts/np.sum(counts)*100
cum_percent = np.cumsum(percentages)

index_max = 50
print('These {} Kanji represent {:.1f}% of the total occurrences'.format(index_max, cum_percent[index_max]))
indexes = np.arange(len(ordered_labels[:index_max]))
plt.bar(indexes, ordered_counts[:index_max])

# add labels
bar_width = 0.35
ChineseFont1 = FontProperties(fname='C:\\Windows\\Fonts\\simsun.ttc', size=16)
plt.xticks(indexes, ordered_labels[:index_max], fontproperties=ChineseFont1)
plt.show()
