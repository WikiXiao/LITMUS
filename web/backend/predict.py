from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

model = load_model('my_model.h5')
MAX_SEQUENCE_LENGTH = 300
MAX_NB_WORDS = 20000
EMBEDDING_DIM = 100 
VALIDATION_SPLIT = 0.2 
NUM_OF_LABEL = 2

positive_data = open('positive.txt','r').readlines()

def predict(text):
	predict_text = []
	predict_text.append(text)
	predict_tokenizer = Tokenizer(nb_words=MAX_NB_WORDS)
	predict_tokenizer.fit_on_texts(predict_text)
	predict_sequences = predict_tokenizer.texts_to_sequences(predict_text)
	predict_data = pad_sequences(predict_sequences, maxlen=MAX_SEQUENCE_LENGTH)
	y_pred = model.predict(predict_data,batch_size=1)
	if(y_pred[0][0]>y_pred[0][1]):
		return 0
	else:
		return 1
print (predict(positive_data[0]))
