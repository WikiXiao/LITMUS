from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import numpy as np
import os
from keras.layers import Dense, Input, Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model

MAX_SEQUENCE_LENGTH = 300
MAX_NB_WORDS = 20000
EMBEDDING_DIM = 100 
VALIDATION_SPLIT = 0.2 
NUM_OF_LABEL = 2

texts = []  # list of text samples
labels = []  # list of label ids
positive_data = open('positive.txt','r').readlines()
negative_data = open('negative.txt','r').readlines()

for line in positive_data:
	line = line.strip()
	texts.append(line)
	labels.append(1)

i = 0
negative_data_size = 3000
for line in negative_data:
  if i > negative_data_size:
    break
  i += 1
  line = line.strip()
  texts.append(line)
  labels.append(0)

tokens = Tokenizer(nb_words=MAX_NB_WORDS)
tokens.fit_on_texts(texts)
seqs = tokens.texts_to_sequences(texts)

word_idx = tokens.word_index

data = pad_sequences(seqs, maxlen=MAX_SEQUENCE_LENGTH)

labels = to_categorical(np.asarray(labels))

# split the data into a training set and a validation set
random_idx = np.arange(data.shape[0])
np.random.shuffle(random_idx)
data = data[random_idx]
labels = labels[random_idx]
val_samples = int(VALIDATION_SPLIT * data.shape[0])

x_train = data[:-val_samples]
y_train = labels[:-val_samples]
x_val = data[-val_samples:]
y_val = labels[-val_samples:]

embeddings_idx = {}
f = open('glove.6B.100d.txt',encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    vec = np.asarray(values[1:], dtype='float32')
    embeddings_idx[word] = vec
f.close()

embedding_matrix = np.zeros((len(word_idx) + 1, EMBEDDING_DIM))
for word, i in word_idx.items():
    embedding_vec = embeddings_idx.get(word)
    if embedding_vec is not None:
        embedding_matrix[i] = embedding_vec

embedding_layer = Embedding(len(word_idx) + 1,
                            EMBEDDING_DIM,
                            weights=[embedding_matrix],
                            input_length=MAX_SEQUENCE_LENGTH,
                            trainable=False)

seq_input = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
embedded_seqs = embedding_layer(seq_input)
x = Conv1D(128, 5, activation='relu')(embedded_seqs)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = MaxPooling1D(5)(x)  # global max pooling
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
preds = Dense(NUM_OF_LABEL, activation='softmax')(x)

model = Model(seq_input, preds)
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['acc'])


model.fit(x_train, y_train, validation_data=(x_val, y_val),
          nb_epoch=2, batch_size=128)

model.save('my_model.h5')
