WIDTH = 5
HEIGHT = 5

INP_DIM = WIDTH * HEIGHT
HID_DIM = 1000  # количество нейронов во внутреннем слое
OUT_DIM = 2

GENERATIONS = 100  # количество поколений

RANDOM_SIZE = 20  # количество изображений fake в батче
RANDOM_AMOUNT = 10000  # количество изображений группы fake

# название директории с json файлами (датасет и веса обученной сети)
JSON_DIR = "json_files"
