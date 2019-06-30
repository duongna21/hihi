import sys

sys.path.append(".")
from flask import Flask, jsonify, make_response
from flask_restful import Api
from flask import request
from flair.data import Sentence
from flair.models import SequenceTagger
import yaml

app = Flask(__name__)
api = Api(app)

model = ""


@app.route('/ner/ecommerce', methods=['GET', 'POST'])
def ner_analytic():
    global model
    result = {}

    if request.method == 'GET':
        text = request.args.get('text')
    elif request.method == 'POST':
        text = request.form["text"]
    else:
        result = {"Error": "Wrong method"}
        return jsonify(result)

    if text is None or text == '':
        result = {"Error": "Missing text parameter"}
        return jsonify(result)
    if text[-1] == '.':
        text = text[:-1]

    sentences = text.split('. ')
    result["input"] = text
    result["result"] = []

    for j, sent in enumerate(sentences):
        words_raw = Sentence(sent)
        model.predict(words_raw)
        preds = []
        sequence_pred = words_raw.to_tagged_string()
        sequence_pred += ' .'
        for i, token in enumerate(sequence_pred.split()):
            if '.' in token and i == (len(sequence_pred.split()) - 1):
                break
            if '<' in token:
                continue
            if ('<' not in token) and ('<' in sequence_pred.split()[i + 1]):
                tag = sequence_pred.split()[i + 1].replace('<', '')
                tag = tag.replace('>', '')
            else:
                tag = 'O'
            preds += [tag]

        res = ""

        for i, token in enumerate(preds):
            prefix = ''
            suffix = ''
            if token[0] == 'B':
                prefix = '<' + token.replace('B-', '') + '>'
                if (i < (len(preds) - 1) and preds[i + 1][0] != 'I') or i == (len(preds) - 1):
                    suffix = '</' + token.replace('B-', '') + '>'
            elif token[0] == 'I':
                if (i < (len(preds) - 1) and preds[i + 1][0] != 'I') or i == (len(preds) - 1):
                    suffix = '</' + token.replace('I-', '') + '>'

            if i < (len(sent) - 1):
                res += (prefix + sent.split()[i] + suffix)

            if i < (len(preds) - 1):
                res += ' '

        result["result"].append(res)
    return jsonify(result)

from flair.data import Sentence
from flair.models import SequenceTagger

if __name__ == '__main__':
    # load model
    model = SequenceTagger.load_from_file('/storage/duongna/flair/resources/taggers/TMDT/best-model.pt')

    # load config
    host = "0.0.0.0"
    port = 9090

    app.run(host=host, port=port, debug=True, threaded=True)

