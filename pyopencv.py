import cv2

def show_image_and_gray_image():
    image = cv2.imread('path/to/your/image.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('path/to/save/gray_image.jpg', gray_image)
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def play_video_and_gray_video():
    cap = cv2.VideoCapture('path/to/your/video.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Original Frame', frame)
        cv2.imshow('Grayscale Frame', gray_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def detect_features():
    image = cv2.imread('path/to/your/image.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(gray_image, None)
    image_with_keypoints = cv2.drawKeypoints(gray_image, keypoints, None, color=(0, 255, 0))
    cv2.imshow('Original Image', gray_image)
    cv2.imshow('Image with Keypoints', image_with_keypoints)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_image_and_gray_image()
    play_video_and_gray_video()
    detect_features()
