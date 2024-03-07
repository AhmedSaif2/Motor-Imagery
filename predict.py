import pickle

model = pickle.load(open("model", 'rb'))
x_test = pickle.load(open("x_test", 'rb'))
y_test = pickle.load(open("y_test", 'rb'))
idx=0

def predict_movement():
    global idx
    sample=x_test[idx]
    sample=sample.reshape((1,-1))
    y_pred=model.predict(sample)
    print("prediction is: ",y_pred)
    print("test: ",y_test[idx])
    idx+=1
    return y_pred

