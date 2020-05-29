from keras import models
from keras.applications import VGG16

pre_model = VGG16(weights='imagenet', include_top=True)
pre_model.summary()