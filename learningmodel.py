import librosa
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import os
import numpy as np
import pandas as pd

dataset = []

for j in range(0, 3):
    dir = input("음원 파일이 있는 디렉토리: ")
    files = os.listdir(dir)
    for i in files:
        y, sr = librosa.load(dir+i, res_type='kaiser_fast')
        mf = librosa.feature.mfcc(y)
        data = np.mean(mf.T, axis=0)
        dataset.append([data, j])

features = pd.DataFrame(dataset, columns=['feature', 'class_label'])

x = np.array(features.feature.tolist())
y = np.array(features.class_label.tolist())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
#x_train = x_train.reshape(x_train.shape[0], 4, 5, num_channels)
#x_test = x_test.reshape(x_test.shape[0], 4, 5, num_channels)

#num_labels = other_y.shape[1]
#filter_size = 2

# Construct model
model = linear_model.LogisticRegression()
model.fit(x_train, y_train)
estimated = model.predict(x_test)
print("예상 값")
print(estimated)
print("정답")
print(y_test)

##model1 = Sequential()
##model1.add(Conv2D(4, (2,2), input_shape=(4, 5, num_channels), activation='relu', kernel_initializer="glorot_uniform"))
##model1.add(MaxPooling2D())
#model1.add(Flatten())
#model1.add(Dense(10, activation='softmax', kernel_initializer="glorot_uniform"))

#np.random.seed(0)
#model1.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=Adam())

#model1.summary()

#hist = model1.fit(x_train, y_train, epochs=10, batch_size=600, validation_data=(x_test, y_test), verbose=2)