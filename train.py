import json
import numpy as np
import nltk
from nltk.stem import PorterStemmer
import tensorflow as tf
from tensorflow.keras import layers

# NLTK setup
nltk.download('punkt')
stemmer = PorterStemmer()

# Load intents
with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?', '!', '.', ',']
all_words = [stemmer.stem(w.lower()) for w in all_words if w not in ignore_words]
all_words = sorted(list(set(all_words)))
tags = sorted(list(set(tags)))

X_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = []
    pattern_words = [stemmer.stem(w.lower()) for w in pattern_sentence]
    for w in all_words:
        bag.append(1) if w in pattern_words else bag.append(0)
    
    X_train.append(bag)
    y_train.append(tags.index(tag))

X_train = np.array(X_train)
y_train = np.array(y_train)

# Neural Network Model
model = tf.keras.Sequential([
    layers.Dense(8, input_shape=(len(X_train[0]),), activation='relu'),
    layers.Dense(8, activation='relu'),
    layers.Dense(len(tags), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=200)

model.save('chatbot_model.h5')
import pickle


model.save('chatbot_model.h5')

pickle.dump(all_words, open('words.pkl', 'wb'))
pickle.dump(tags, open('classes.pkl', 'wb'))

print("Training complete! Model saved as chatbot_model.h5")
print("Training complete! Model saved as chatbot_model.h5")