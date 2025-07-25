import pose_detection as pd
import cv2 as cv
import time

def main():
    cap = cv.VideoCapture(0)
    detector = pd.PoseDetector()
    ptime = 0

    while True:
        success, img = cap.read()
        if not success:
            break

        flipped_img = cv.flip(img, 1)  
        img = detector.findPose(img, flipped_img, draw=True)
        lmlist = detector.findPosition(img, draw=True)

        cTime = time.time()
        fps = 1 / (cTime - ptime) if cTime != ptime else 0
        ptime = cTime

        cv.putText(img, f'FPS: {int(fps)}', (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        cv.imshow("Partner Pose", img)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "_main_":
    main()