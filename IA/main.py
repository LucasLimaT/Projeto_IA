import cv2


def main() -> None:
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        raise SystemExit("Não foi possível abrir a câmera.")

    try:
        while True:
            retorno, frame = capture.read()
            if not retorno:
                break

            cv2.imshow("Visão da câmera", frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC para sair
                break
    finally:
        capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
