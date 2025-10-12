import cv2 as cv
import argparse
from operations.erosion import apply_erosion
from operations.dilatation import apply_dilation

def main():
    parser = argparse.ArgumentParser(description='Operações morfológicas: Erosão e Dilatação')
    parser.add_argument('--input', help='Caminho da imagem de entrada', default='./images/LinuxLogo.jpg')
    args = parser.parse_args()

    # carrega a imagem (precisa ser binária)
    src = cv.imread(args.input, cv.IMREAD_GRAYSCALE)
    if src is None:
        print("Erro: não foi possível carregar a imagem.")
        return

    print("=== Operações Morfológicas com OpenCV ===")
    
    opcao = input("Escolha a operação (1-Erosão, 2-Dilatação): ")

    if opcao == '1':
        apply_erosion(src)
    elif opcao == '2':
        apply_dilation(src)
    else:
        print("Opção inválida.")

    cv.destroyAllWindows()

main()
