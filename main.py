import tika
import numpy as np
import string
from tika import parser
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# start virtual machine to run TIKA
tika.initVM()
parsed = parser.from_file('data\\test3.pdf')
content = parsed["content"]

# Create ignore list
katakana_chart = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポ" \
                 "マミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾー"
hiragana_chart = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼ" \
                 "ぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
punctuation = '、。「」…―！？』『※【】≪≫・｜“”Оγω☆♯★≠А《》♪βα×ΩΣθ■〜▼�△'
latin = str([chr(65280 + x) for x in range(0, 91)])

# filter and sort
words = content.split()
stop_words = katakana_chart + hiragana_chart + punctuation + string.ascii_letters + latin
words = [w for w in words if (w not in stop_words) and (not w.isnumeric()) and (len(w) == 1)]
labels, counts = np.unique(words, return_counts=True)

indSort = np.argsort(counts)[::-1]
ordered_counts = counts[indSort]
ordered_labels = labels[indSort]

# Analysis and plots
print('There are {:d} unique Kanji'.format(len(counts)))
percentages = ordered_counts/np.sum(counts)*100
cum_percent = np.cumsum(percentages)
print('The first {:d} kanji make up 50% of total uses.\n'
      'The first {:d} kanji make up 90% of total uses\n'
      '{:d} appear only one time'.format(np.argwhere(cum_percent > 50)[0, 0],
                                         np.argwhere(cum_percent > 90)[0, 0],
                                         np.sum([1 for i in ordered_counts if i == 1])))
i = 0
plt.figure(i)
plt.plot(cum_percent)
plt.grid()
i += 1
plt.figure(i)
plt.plot(percentages)
plt.grid()

i += 1
plt.figure(i)
index_max = 50
print('These {} Kanji represent {:.1f}% of the total occurrences'.format(index_max, cum_percent[index_max]))
indexes = np.arange(len(ordered_labels[:index_max]))
plt.bar(indexes, ordered_counts[:index_max])

# add labels
bar_width = 0.35
ChineseFont1 = FontProperties(fname='C:\\Windows\\Fonts\\simsun.ttc', size=16)
plt.xticks(indexes, ordered_labels[:index_max], fontproperties=ChineseFont1)
plt.show()
