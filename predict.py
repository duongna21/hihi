from flair.data import Sentence
from flair.models import SequenceTagger
from collections import defaultdict as ddict
import operator

model = SequenceTagger.load_from_file('/Users/naduong1001/Downloads/flair/resources/taggers/TMDT/best-model.pt')

#sentence= Sentence('Đừng Nhân Danh Tình Yêu')


sentences = open('/Users/naduong1001/Downloads/new_adayroi.txt').read().split('\n')

confidences = ddict(float)
for i, sent in enumerate(sentences[:50]):
    if sent:
        sentence = Sentence(sent)
        _, confidences[i] = model.predict(sentence)

sorted_x = sorted(confidences.items(), key=operator.itemgetter(1))

with open('data/LC_adayroi.txt', 'w') as w:
    for item in sorted_x:
        w.write(sentences[item[0]])
        w.write('\n')
# create example sentence

# predict tags and print
# model.predict(sentence)
#
# print(sentence.to_tagged_string())