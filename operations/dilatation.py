import cv2 as cv
from utils import morph_shape, create_element

title_dilation_window = 'Dilatação'
trackbar_element = 'Elemento: 0-Retângulo | 1-Cruz | 2-Elipse'
trackbar_size = 'Tamanho do kernel: 2n + 1'

def apply_dilation(src):
    max_elem = 2
    max_kernel_size = 21

    # cria janelas e trackbars
    cv.namedWindow(title_dilation_window)
    cv.createTrackbar(trackbar_element, title_dilation_window, 0, max_elem, lambda x: None)
    cv.createTrackbar(trackbar_size, title_dilation_window, 0, max_kernel_size, lambda x: None)

    while True:
        # le valor da trackbars
        elem_type = cv.getTrackbarPos(trackbar_element, title_dilation_window)
        kernel_size = cv.getTrackbarPos(trackbar_size, title_dilation_window)

        # cria elemento estruturante
        element = create_element(morph_shape(elem_type), kernel_size)

        # aplicar dilatação
        dilation_result = cv.dilate(src, element)

        # mostrar resultado
        cv.imshow(title_dilation_window, dilation_result)

        # sair se o usuário apertar ESC
        key = cv.waitKey(30)
        if key == 27:
            break

    cv.destroyWindow(title_dilation_window)
