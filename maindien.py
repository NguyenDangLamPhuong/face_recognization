import face_recognition
import cv2
def is_match_person(source,unknown):
    known_image = face_recognition.load_image_file(source)


    unknown_image = face_recognition.load_image_file(unknown)

    if face_recognition.face_encodings(known_image) and face_recognition.face_encodings(unknown_image):
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
        return results
    else:
        return False



print(is_match_person("/Users/mac/Documents/GitHub/face-recognisation/dien2.jpeg", "/Users/mac/Documents/GitHub/face-recognisation/dien2.jpeg"))
#
cap = cv2.VideoCapture(0)
# Load the cascade
face_cascade = cv2.CascadeClassifier('/Users/mac/Documents/GitHub/face-recognisation/haarcascade_frontalface_default.xml')
#
# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input


while True:
    # Read the frame

    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face'


    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    org = (00, 185)

    # fontScale
    fontScale = 1

    # Red color in BGR
    color = (0, 0, 255)

    # Line thickness of 2 px
    thickness = 2

    # Using cv2.putText() method

    for (x, y, w, h) in faces:
        img_name = '/Users/mac/Documents/GitHub/face-recognisation/dien.jpeg'
        cv2.imwrite(img_name, img)
        ans = is_match_person("/Users/mac/Documents/GitHub/face-recognisation/dien2.jpeg", img_name)
        print(ans)
        if ans==[True]:
            text = "True"
        else:
            text = "False"

        (text_width, text_height) = cv2.getTextSize(text, font, font, thickness)[0]
        text_width *= len(text)
        # print(text_width,w)
        x2 = x + w // 2 - 50;
        y2 = y + h + 30
        org = (x2, y2)
        cv2.putText(img, text, org, font, fontScale,
                    color, thickness, cv2.LINE_AA, False)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the VideoCapture object
cap.release()
