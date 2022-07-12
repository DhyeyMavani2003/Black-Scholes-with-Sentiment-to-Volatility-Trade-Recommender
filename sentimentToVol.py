# importing keras from TensorFlow
from tensorflow import keras

# Loading a trained model from Keras from previous sentiment to volatility data
model = keras.models.load_model('./sentiVol.h5')

'''
Converts sentiment values into a predicted volatility score
'''
def sentimentToVol(sentimentScore):
    ans = model.predict([sentimentScore])
    return ans[0]
