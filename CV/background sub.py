import cv2
def main():
    image_path = "C:/Users/gnana/Downloads/1231230.jpeg"
    image = cv2.imread(image_path)
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()
    fg_mask = bg_subtractor.apply(image)
    cv2.imshow('Original Image', image)
    cv2.imshow('Foreground Mask', fg_mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
