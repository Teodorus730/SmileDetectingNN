from data.fake import make_fake
from data.dataset import DATASET
from config import OUT_DIM
from data_funcs import save_data


def make():
    real_inp = []
    real_out = []
    for i, o in zip(DATASET, range(OUT_DIM)):
        print(o)
        for j in DATASET[i]:
            real_inp.append(j)
            kek = [0]*OUT_DIM
            kek[o] = 1
            real_out.append(kek)

    fake_inp = []
    fake_out = []
    for i in make_fake(10000):
        fake_inp.append(i)
        fake_out.append([0]*OUT_DIM)

    return {"real": {"inp": real_inp, "out": real_out},
            "fake": {"inp": fake_inp, "out": fake_out}}


if __name__ == "__main__":
    save_data(make())
