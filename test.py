# import glob
# # for domain in glob.glob('/Users/naduong1001/Downloads/ecommerce/sample/*'):
# # 	for folder in glob.glob(domain+'/*'):
# # 		for file in glob.glob(folder+'/*.txt'):
# with open('/Users/naduong1001/Downloads/LC_lazada_output.txt') as f:
# 	sents = f.read().split('\n\n')
# 	with open('/Users/naduong1001/Downloads/new_lazada_predicted.txt', 'w') as w:
# 		for sent in sents:
# 			sent += ' .'
# 			for i, token in enumerate(sent.split()):
# 				if '.' in token and i == (len(sent.split())-1):
# 					break
# 				if '<' in token:
# 					continue
# 				if ('<' not in token) and ('<' in sent.split()[i+1]):
# 					tag = sent.split()[i+1].replace('<', '')
# 					tag = tag.replace('>', '')
# 					w.write(token+'\t'+tag+'\n')
# 				else:
# 					w.write(token+'\tO'+'\n')
# 			w.write('\n')
#
# # from flair.data import Sentence
# # from flair.models import SequenceTagger
# # import yaml
# #
# # if __name__ == '__main__':
# # 	model = SequenceTagger.load_from_file('/Users/naduong1001/Downloads/flair/resources/taggers/TMDT/best-model.pt')
# # 	result = {}
# # 	text = 'Máy Xay Thịt 2 Lưỡi Dao Kép Lock&Lock EJM171 (2L). Giày Thể Thao Nam Biti’s Hunter X – 2K18 – DSUH00100CAM - Sunrise Orange.'
# # 	text = str(text.encode('utf-8'))
# # 	sentences = text.split('. ')
# # 	result["input"] = text
# # 	result["result"] = []
# #
# # 	for j, sent in enumerate(sentences):
# # 		words_raw = Sentence(sent)
# # 		model.predict(words_raw)
# # 		preds = []
# # 		sequence_pred = words_raw.to_tagged_string()
# # 		sequence_pred += ' .'
# # 		for i, token in enumerate(sequence_pred.split()):
# # 			if '.' in token and i == (len(sequence_pred.split()) - 1):
# # 				break
# # 			if '<' in token:
# # 				continue
# # 			if ('<' not in token) and ('<' in sequence_pred.split()[i + 1]):
# # 				tag = sequence_pred.split()[i + 1].replace('<', '')
# # 				tag = tag.replace('>', '')
# # 			else:
# # 				tag = 'O'
# # 			preds += [tag]
# #
# # 		res = ""
# #
# # 		for i, token in enumerate(preds):
# # 			prefix = ''
# # 			suffix = ''
# # 			if token[0] == 'B':
# # 				prefix = '<' + token.replace('B-', '') + '>'
# # 				if (i < (len(preds) - 1) and preds[i + 1][0] != 'I') or i == (len(preds) - 1):
# # 					suffix = '</' + token.replace('B-', '') + '>'
# # 			elif token[0] == 'I':
# # 				if (i < (len(preds) - 1) and preds[i + 1][0] != 'I') or i == (len(preds) - 1):
# # 					suffix = '</' + token.replace('I-', '') + '>'
# #
# # 			if i < (len(sent) - 1):
# # 				res += (prefix + sent.split()[i] + suffix)
# #
# # 			if i < (len(preds) - 1):
# # 				res += ' '
# #
# # 		result["result"].append(res)
# # 	print (result)
#

def g():
	print(x)
	#x=1
def f():
	print(x)

x=3
g()