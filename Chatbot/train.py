import random
from tensorflow.keras.optimizers import SGD
from keras.layers import Dense, Dropout
from keras.models import load_model
from keras.models import Sequential
import numpy as np
import pickle
import json
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
nltk.download('omw-1.4')
nltk.download("punkt")
nltk.download("wordnet")


# 파일 load
words = []
classes = []
documents = []
ignore_words = ["?", "!"]
with open("intents.json", encoding="utf-8") as f:
    intents = json.load(f)

# 단어
for intent in intents["intents"]:
    for pattern in intent["patterns"]:

        # 각 단어 토큰화
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # documents 추가
        documents.append((w, intent["tag"]))

        # class list에 classes 추가
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

# lemmatizer
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

print(len(documents), "documents")

print(len(classes), "classes", classes)

print(len(words), "unique lemmatized words", words)


pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(classes, open("classes.pkl", "wb"))

# 학습 데이터 초기화
training = []
output_empty = [0] * len(classes)
for doc in documents:
    # 단어 초기화
    bag = []
    # 패턴에 대한 토큰화된 단어 리스트
    pattern_words = doc[0]
    # 기본 단어 만들기?
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # 패턴에서 일치하는 단어 있을 시 1로 단어 추가
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # 출력은 각 태그에 대해 0, 현재 태그에 대해서 1
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
# shuffle
random.shuffle(training)
training = np.array(training)
# 테스트 목록 생성
train_x = list(training[:, 0])
train_y = list(training[:, 1])
print("Training data created")

# 학습
# 모델 생성 - 3개 도면층. 첫 번째 층 128개, 두 번째 층 64개,
#             세 번째 출력 층은 뉴런 수를 포함

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))
model.summary()

# 모델 컴파일
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])


# 모델 저장, fitting
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save("chatbot_model.h5", hist)
print("model created")

