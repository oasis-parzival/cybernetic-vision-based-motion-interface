import cv2
import mediapipe as mp
import pyvjoy

# virtual joystick
j = pyvjoy.VJoyDevice(1)  # vJoy device ID 1

# MediaPipe pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# webcam (0 for inbuilt and 1 for External)
cap = cv2.VideoCapture(0)

# Create a resizable window
cv2.namedWindow("Pose Control", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(img_rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        lm = results.pose_landmarks.landmark

        # Punch
        if (lm[mp_pose.PoseLandmark.RIGHT_WRIST].y < lm[mp_pose.PoseLandmark.RIGHT_SHOULDER].y or
            lm[mp_pose.PoseLandmark.LEFT_WRIST].y < lm[mp_pose.PoseLandmark.LEFT_SHOULDER].y):
            print("Punch!")
            j.set_button(1, 1)
        else:
            j.set_button(1, 0)

        # Kick
        if (lm[mp_pose.PoseLandmark.RIGHT_KNEE].y < lm[mp_pose.PoseLandmark.RIGHT_HIP].y or
            lm[mp_pose.PoseLandmark.LEFT_KNEE].y < lm[mp_pose.PoseLandmark.LEFT_HIP].y):
            print("Kick!")
            j.set_button(2, 1)
        else:
            j.set_button(2, 0)

        # Block
        if (lm[mp_pose.PoseLandmark.RIGHT_WRIST].y < lm[mp_pose.PoseLandmark.RIGHT_SHOULDER].y and
            lm[mp_pose.PoseLandmark.LEFT_WRIST].y < lm[mp_pose.PoseLandmark.LEFT_SHOULDER].y):
            print("Block!")
            j.set_button(3, 1)
        else:
            j.set_button(3, 0)

        # Jump
        if (lm[mp_pose.PoseLandmark.RIGHT_KNEE].y < lm[mp_pose.PoseLandmark.RIGHT_HIP].y and
            lm[mp_pose.PoseLandmark.LEFT_KNEE].y < lm[mp_pose.PoseLandmark.LEFT_HIP].y):
            print("Jump!")
            j.set_button(4, 1)
        else:
            j.set_button(4, 0)

    frame = cv2.flip(frame, 1)

    cv2.imshow("Pose Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
