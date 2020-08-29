//import * as tf from '@tensorflow/tfjs';

//const model = await tf.loadLayersModel('model.json');
import tensorflowjs as tfjs


json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
//load weights into new model
loaded_model.load_weights("model.h5")

