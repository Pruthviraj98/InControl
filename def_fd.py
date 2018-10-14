import face_recognition
import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def face_detect():
    fromaddr = "kunal.kc.chandiramani@gmail.com"
    toaddr = "kdilip.chandiramani2016@vitstudent.ac.in"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "CAR ALERT"
 
    body = "A stranger has entered your car!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "7666561900")
    text = msg.as_string()
 
    #msg = "A stranger has entered your car!"
 
    video_capture = cv2.VideoCapture(0)
    #dhruv_image = face_recognition.load_image_file("dhruv.jpg")
    #dhruv_face_encoding = face_recognition.face_encodings(dhruv_image)[0]

    # Load a second sample picture and learn how to recognize it.
    kunal_image = face_recognition.load_image_file("kunal.jpg")
    kunal_face_encoding = face_recognition.face_encodings(kunal_image)[0]

    arush_image= face_recognition.load_image_file("arush3.jpg")
    arush_face_encoding = face_recognition.face_encodings(arush_image)[0]

    pruthviraj_image = face_recognition.load_image_file("pruthviraj.jpg")
    pruthviraj_face_encoding = face_recognition.face_encodings(pruthviraj_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [kunal_face_encoding, arush_face_encoding, pruthviraj_face_encoding]


    known_face_names = [
        "Kunal",
        "Arush",
        "Pruthviraj"
    ]

    flag=0
    name1=""
    j=0
    k=0

    while True:
        global name
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face enqcodings in the frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.4)

            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                name1=name
                j=j+1
            else:
                k+=1
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            #if(name=="Arush" or name=="Dhruv" or name=="Pruthviraj" or name=="Kunal"):
                #break

        # Display the resulting image
        cv2.imshow('Video', frame)
        #time.sleep(2)
        #if(name1=="Arush" or name1=="Dhruv" or name1=="Pruthviraj" or name1=="Kunal"):
                #break
        if(j>3):
            break
        elif(k>15):
            #text=msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            flag=1
            break
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
    server.quit()
    return name1,flag
