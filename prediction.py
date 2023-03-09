from sigmoid import *
from data_funcs import load_data


def predict(x, idk=False):
    data = load_data("output.json")
    W1 = np.array(data["w1"])
    W2 = np.array(data["w2"])

    h1 = sigmoid(np.dot(x, W1))
    h2 = sigmoid(np.dot(h1, W2))
    print(h2)

    if idk:
        if round(h2[0]) == 1:
            print("SMILE :)")
        elif round(h2[1]) == 1:
            print("SAD :(")
        else:
            print("I DON'T KNOW")
    else:
        m = max(h2)
        if h2[0] == m:
            print("SMILE :)")
        else:
            print("SAD :(")

