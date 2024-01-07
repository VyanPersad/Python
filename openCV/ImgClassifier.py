import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential

train_path
test_path

x_train=ImageDataGenerator(rescale=1./255).flow_from_directory(train_path,batch_size=32,classes=['female','male'], class_mode='categorical', target_size=(220,220), shuffle=True)
x_test=ImageDataGenerator(rescale=1./255).flow_from_directory(train_path,batch_size=32,classes=['female','male'], class_mode='categorical', target_size=(220,220), shuffle=True)

from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.models import Sequential
model = Sequential()

model.add(Conv2D(32,(3,3), activation='relu', padding='same',input_shape=(220,220,3)))
model.add(Conv2D(32,(3,3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(Conv2D(64,(3,3), activation='relu', padding='same'))
model.add(Conv2D(64,(3,3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Dense(100, activation='softmax'))

model.compile(optimizer='adam', loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),metrics=['accuracy'])
#history = model.fit_generator(x_train, epochs=10, steps_per_epoch=(200/5), verbose=1, validation_data=x_test,validation_steps=(80/5))

#model.save()
#plt.plot(history.history['accuracy'])
#plt.plot(history.history['val_accuracy'])
#plt.xlabel('epoch')
#plt.ylabel('accuracy')
#plt.legend(['train','test'],loc='best')

face_class=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def predict(model,cap):
    prediction=model.predict(cap)
    return np.argmax(prediction)
vid = cv2.VideoCapture(0)
if not vid.isOpened():
    print('Camera cannot be opened')
    exit()
while True:
    ret, cap = vid.read()
    if not ret:
        print('Cannot get frame')
        break
    gray = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
    face = face_class.detectMultiScale(gray,1.05,5)
    if face is():
        print('No face detected')


    for(x,y,a,b) in face:
        cv2.rectangle(cap,(x,y),(x+a,y+b), (127, 0, 255),2)
        roi_color = cap[y:y+b, x:x+a]
        img = cv2.resize(roi_color, (220,220), interpolation = cv2.INTER_CUBIC)
        img =img.astype('float16')
        img = np.expand_dims(img, axis=0)
        score = predict(model, img)
        if score == 1:
            cv2.putText(cap, 'Male',(x+a,y+b),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0),1, cv2.LINE_AA)
        if score == 0:
            cv2.putText(cap, 'Female', (x + a, y + b), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow('image', cap)
        cv2.waitKey(2)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()



