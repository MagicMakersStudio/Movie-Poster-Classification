
#-=-=-=-=-=-=-=-=-=-=-#
#       IMPORT        #
#-=-=-=-=-=-=-=-=-=-=-#

import keras
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.optimizers import Adam
from PIL import Image
from glob import glob
import numpy as np
import h5py


#-=-=-=-=-=-=-=-=-=-=-#
#   CHARGER MODÈLE    #
#-=-=-=-=-=-=-=-=-=-=-#

model = load_model("model.h5")


#-=-=-=-=-=-=-=-=-=-=-#
#        DATA         #
#-=-=-=-=-=-=-=-=-=-=-#

toutesImages = glob("../Data/poster_test/*.jpg")
#print(toutesImages)


#-=-=-=-=-=-=-=-=-=-=-=-=-#
# PREDICTION SUR L'IMAGE  #
#-=-=-=-=-=-=-=-=-=-=-=-=-#


for img in toutesImages:
	poster_img = Image.open(img)
	#PREPARE DATA
	poster = np.array(poster_img)
	poster = poster.astype("float32")
	poster /= 255
	#PREDICT
	poster=np.expand_dims(poster,0)
	try :
		prediction = model.predict(poster)
		prediction = np.argmax(prediction)
		if prediction == 1:
			print(img)
			input("")
			poster_img.show()
	except:
		print("      ")
		print("Image erreur : " + img)
		print("      ")
