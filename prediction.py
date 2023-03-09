from sigmoid import *
from data_funcs import load_data


def predict(x, idk=False):
    data = load_data("output.json")
    W1 = np.array(data["w1"])
    W2 = np.array(data["w2"])

    h1 = sigmoid(np.dot(x, W1))
    h2 = sigmoid(np.dot(h1, W2))

    react = [("green", "SMILE :)"), ("green", "SAD :(")]

    if idk:
        for i in range(len(h2)):
            if round(h2[i]) == 1:
                return react[i]
        else:
            return ["red", "I DON'T KNOW"]
    else:
        m = max(h2)
        for i in range(len(h2)):
            if h2[i] == m:
                return react[i]

