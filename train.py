from distutils.version import LooseVersion
import gensim
from gensim.models import KeyedVectors
import os
from backend.NLP.main.text_classifier import TextClassifier

if __name__ == '__main__':
    root_dir = os.getcwd().replace('\\', '/')
    data_path = root_dir + '/backend/NLP/data/processed_data4.csv'

    if LooseVersion(gensim.__version__) >= LooseVersion("1.0.1"):
        from gensim.models import KeyedVectors
        word2vec_model = KeyedVectors.load_word2vec_format(
            root_dir + '/backend/NLP/models/w2v.bin', binary=True)
    else:
        from gensim.models import Word2Vec
        word2vec_model = Word2Vec.load(
            root_dir + '/backend/NLP/models/w2v.bin', binary=True)

    keras_text_classifier = TextClassifier(word2vec_dict=word2vec_model, model_path=root_dir + '/backend/NLP/models/sentiment_model7.weights.h5',
                                           max_length=50, n_epochs=1000)
    X, y = keras_text_classifier.load_data(data_path)
    keras_text_classifier.train(X, y)

    content = 'Võ Nguyên Giáp là ai vậy?'

    labels = keras_text_classifier.get_label(data_path)

    test = keras_text_classifier.classify([content], label_dict=labels)
    print(test)