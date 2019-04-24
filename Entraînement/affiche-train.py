
#-=-=-=-=-=-=-=-=-=-=-#
#       IMPORT        #
#-=-=-=-=-=-=-=-=-=-=-#

import numpy as np
from PIL import Image as img
from glob import glob
from tqdm import tqdm
from keras.utils import to_categorical
import keras
from keras.layers import*
from keras.optimizers import Adam
from keras.models import Sequential
import h5py
from sklearn.model_selection import train_test_split

np.set_printoptions(threshold=np.nan)


#-=-=-=-=-=-=-=-=-=-=-#
#        DATA         #
#-=-=-=-=-=-=-=-=-=-=-#

mes_images=[]
mes_labels=[]

img_train=[]
img_test=[]
label_train=[]
label_test=[]

imageslvl = glob("../Data/posters/*.jpg")

for img in tqdm(imageslvl):
	label=img.split("__")
	label=label[1]
	label=label.split(".")[0]
	label=label.split("|")
	#print(label)
	if "Action" in label:
		#print("ui")
		mes_labels.append(1)
	else :
		#print("no god pls no, NOOOO")
		mes_labels.append(0)
	poster=img.open(img)
	poster=poster.convert("RGB")
	poster=np.array(poster)
	poster=poster.astype("float32")
	poster/=255
	mes_images.append(poster)

mes_labels=np.array(mes_labels)
mes_images=np.array(mes_images)

mes_labels = to_categorical(mes_labels,2)
img_train,img_test,label_train,label_test=train_test_split(mes_images,mes_labels,test_size=0.9)

print(mes_images.shape)
#print(mes_labels)

#-=-=-=-=-=-=-=-=-=-=-#
#       MODÈLE        #
#-=-=-=-=-=-=-=-=-=-=-#

model = Sequential()
model.add(Conv2D(24, (3,3), strides = (2,2), activation = "relu", input_shape=(268,182,3)))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))

model.add(Conv2D(32, (3,3), strides = (2,2), activation = "relu"))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))

model.add(Conv2D(64, (3,3), strides = (2,2), activation = "relu"))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))

model.add(Flatten())

model.add(Dense(100,activation="relu"))

model.add(Dense(2,activation="softmax"))

model.summary()

model.compile(loss = "categorical_crossentropy",
				optimizer = Adam(),
				metrics = ["accuracy"])

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#       TRAIN - ENTRAÎNEMENT        #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

model.fit(img_train, label_train,
			epochs = 10,
			batch_size = 100,
			validation_data = (img_test, label_test))

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#       SAUVEGARDER MODÈLE        #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

model.save("model.h5")
