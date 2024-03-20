from backend.NLP.main.preprocessor import Preprocessor as CustomPreprocessor  # NLP.main.
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras import backend as K
from sklearn.preprocessing import LabelEncoder
from keras.layers import LSTM, Dense, Bidirectional, Conv1D, MaxPooling1D
from keras.models import Sequential
import keras
import numpy as np
import pandas as pd
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


class TextClassifier:
    def __init__(self, word2vec_dict, model_path, max_length=10, n_epochs=20, batch_size=64, n_class=11):
        self.word2vec = word2vec_dict
        self.max_length = max_length
        self.word_dim = self.word2vec.vector_size
        self.n_epochs = n_epochs
        self.batch_size = batch_size
        self.model_path = model_path
        self.n_class = n_class
        self.model = None
        self.vocab = self.word2vec.key_to_index

    def build_model(self, input_dim):
        """
        Build model structure
        :param input_dim: input dimension max_length x word_dim
        :return: Keras model
        """
        model = Sequential()

        model.add(Conv1D(filters=128, kernel_size=3, padding='same',
                  activation='relu', input_shape=input_dim))
        model.add(Conv1D(filters=128, kernel_size=3,
                  padding='same', activation='relu'))
        model.add(Conv1D(filters=128, kernel_size=3,
                  padding='same', activation='relu'))
        model.add(Conv1D(filters=128, kernel_size=3,
                  padding='same', activation='relu'))
        model.add(Conv1D(filters=128, kernel_size=3,
                  padding='same', activation='relu'))
        model.add(Conv1D(filters=128, kernel_size=3,
                  padding='same', activation='relu'))
        model.add(MaxPooling1D(pool_size=(8)))
        model.add(Bidirectional(
            LSTM(128, dropout=0.1, activation='relu', return_sequences=True)))
        model.add(Bidirectional(LSTM(64, dropout=0.2, activation='relu')))
        model.add(Dense(self.n_class, activation="softmax"))

        # print(model.summary())

        model.compile(loss=keras.losses.binary_crossentropy,
                      optimizer=keras.optimizers.Adam(),
                      metrics=['accuracy'])
        K.clear_session()
        return model

    def train(self, X, y):
        """
        Training with data X, y
        :param X: 3D features array, number of samples x max length x word dimension
        :param y: 2D labels array, number of samples x number of class
        :return:
        """
        checkpoint = ModelCheckpoint(self.model_path, monitor='val_loss', verbose=1,
                                     save_best_only=True, mode='min', save_weights_only=True)
        early_stop = EarlyStopping(monitor='val_loss', patience=3)
        self.model = self.build_model((self.max_length, self.word_dim))
        self.model.fit(X, y, batch_size=self.batch_size, epochs=self.n_epochs,
                       validation_split=0.2, callbacks=[checkpoint, early_stop])
        self.model.save_weights(self.model_path)

    def predict(self, X):
        """
        Predict for 3D feature array
        :param X: 3D feature array, converted from string to matrix
        :return: label array y as 2D-array
        """
        if self.model is None:
            self.load_model()
        y = self.model.predict(X)
        K.clear_session()
        return y

    def classify(self, sentences, label_dict=None):
        """
        Classify sentences
        :param sentences: input sentences in format of list of strings
        :param label_dict: dictionary of label ids and names
        :return: label array
        """
        X = self.tokenize_sentences(sentences)
        X = self.word_embed_sentences(X, max_length=self.max_length)
        y = self.predict(np.array(X))
        y = np.argmax(y, axis=1)

        labels = []
        for lab_ in y:
            if label_dict is None:
                labels.append(lab_)
            else:
                labels.append(label_dict[lab_])
        X = None
        y = None
        return labels

    def load_model(self):
        """
        Load model from file
        :return: None
        """
        self.model = self.build_model((self.max_length, self.word_dim))
        self.model.load_weights(self.model_path)
        K.clear_session()

    def load_data(self, data_path):
        """
        Load data
        :param data_path: list of paths to files or directories
        :param load_method: method to load (from file or from directory)
        :return: 3D-array X and 2D-array y
        """
        df = pd.read_csv(data_path, encoding='utf-8', usecols=[1, 2])
        X = df.values[:, 0]
        y = df.values[:, 1]

        Encoder = LabelEncoder()
        y = Encoder.fit_transform(list(y))

        self.n_class = len(set(list(y)))

        y_train = np.zeros((len(y), self.n_class), dtype="float")
        for idx, val in enumerate(y):
            y_train[idx][val] = 1
        y = y_train
        X = self.tokenize_sentences(X)
        X = self.word_embed_sentences(X, max_length=self.max_length)

        K.clear_session()
        return np.array(X), np.array(y)

    # helper
    def word_embed_sentences(self, sentences, max_length=10):
        """
        Helper method to convert word to vector
        :param sentences: input sentences in list of strings format
        :param max_length: max length of sentence you want to keep, pad more or cut off
        :return: embedded sentences as a 3D-array
        """
        embed_sentences = []

        for sent in sentences:
            embed_sent = []
            for word in sent:
                if (word) in self.vocab:
                    embed_sent.append(self.word2vec[word])
            if len(embed_sent) > max_length:
                embed_sent = embed_sent[:max_length]
            elif len(embed_sent) < max_length:
                embed_sent = np.concatenate((embed_sent, np.zeros(
                    shape=(max_length - len(embed_sent), 150), dtype=float)), axis=0)
            embed_sentences.append(embed_sent)
        return embed_sentences

    def tokenize_sentences(self, sentences):
        p = CustomPreprocessor()
        return p.tokenize_list_sentences(sentences)

    def get_label(self, data_path):
        df = pd.read_csv(data_path, encoding='utf-8', usecols=[1, 2])
        X = df.values[:, 0]
        y = df.values[:, 1]
        labels = y
        Encoder = LabelEncoder()
        y = np.array(Encoder.fit_transform(y))
        y = np.concatenate((np.array(y).reshape(-1, 1),
                           np.array(labels).reshape(-1, 1)), axis=1)
        label_dict = {}
        for row in y:
            if row[0] in label_dict:
                pass
            else:
                label_dict[row[0]] = row[1]
        return label_dict




def classifier(keras_text_classifier, labels, content, is_general=True):
    print("Is generall: --->", is_general)

    results = keras_text_classifier.classify([content], label_dict=labels)
    return results[0]