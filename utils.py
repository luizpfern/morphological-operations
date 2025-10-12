import cv2 as cv

# retorna o tipo de elemento estruturante
def morph_shape(val):
    if val == 0:
        return cv.MORPH_RECT ## retângulo
    elif val == 1:
        return cv.MORPH_CROSS ## cruz
    elif val == 2:
        return cv.MORPH_ELLIPSE ## elipse

# elemento estruturante kernel
def create_element(shape, size):
    return cv.getStructuringElement(shape, (2 * size + 1, 2 * size + 1), (size, size))
