from flask import Flask, request

import nltk
from mode.utils.text import title
from nltk import pos_tag
from nltk.corpus import wordnet
import nlp_util

app = Flask(__name__)


@app.route('/nlp/keywords', methods=['GET'])
def hello_world():
    complete_title = request.args.get("title")
    # lemmatizer = nltk.WordNetLemmatizer()
    #
    # sentence = complete_title
    # tokens = nltk.word_tokenize(sentence)
    # postag = nltk.pos_tag(tokens)
    #
    # grammar = r"""
    #     NBAR:
    #         {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
    #         {<RB.?>*<VB.?>*<JJ>*<VB.?>+<VB>?} # Verbs and Verb Phrases
    #
    #     NP:
    #         {<NBAR>}
    #         {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
    #
    # """
    #
    # cp = nltk.RegexpParser(grammar)
    # tree = cp.parse(postag)
    #
    # # print(tree)
    #
    # def leaves(tree):
    #     """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    #     for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
    #         yield subtree.leaves()
    #
    # def get_word_postag(word):
    #     if pos_tag([word])[0][1].startswith('J'):
    #         return wordnet.ADJ
    #     if pos_tag([word])[0][1].startswith('V'):
    #         return wordnet.VERB
    #     if pos_tag([word])[0][1].startswith('N'):
    #         return wordnet.NOUN
    #     else:
    #         return wordnet.NOUN
    #
    # def normalise(word):
    #     """Normalises words to lowercase and stems and lemmatizes it."""
    #     word = word.lower()
    #     postag = get_word_postag(word)
    #     word = lemmatizer.lemmatize(word, postag)
    #     return word
    #
    # def get_terms(tree):
    #     for leaf in leaves(tree):
    #         terms = [normalise(w) for w, t in leaf]
    #         yield terms
    #
    # terms = get_terms(tree)
    #
    # features = []
    # for term in terms:
    #     _term = ''
    #     for word in term:
    #         _term += ' ' + word
    #     features.append(_term.strip())
    # list_info = [title(t_word) for t_word in features]
    list_info = nlp_util.get_continuous_chunks(complete_title)

    return {"result": list_info}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
