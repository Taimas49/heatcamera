import cv2 as cv
import psycopg2 
capture = cv.VideoCapture(0) #to open Camera

#accessing pretrained model
pretrained_model = cv.CascadeClassifier("face.xml") 
#rec = cv.rectangle()
# DBWork.ConnectToDb()

temperature = 999
connection = None
cursor = None

#connect to the db 
con = psycopg2.connect(
            host = "localhost",
            database="face_temperature",
            user = "postgres",
            password = "assasin007")

#cursor 
cur = con.cursor()

# cur.execute("insert into temp (temperature) values (5)"  )
        # if temperature > 36:
        #     cur.execute("insert into temp (temperature) values (%s)", [temperature] )
        #     con.commit()
            
        # else:
        #     continue   
# #execute query
# cur.execute("select temperature from temp")

# rows = cur.fetchall()

# # for r in rows:
# #     print (f"id {r[0]} name {r[1]}")

# #commit the transcation 
# con.commit()

# #close the cursor
# cur.close()

# #close the connection
# con.close()

while True:
    boolean, frame = capture.read()
    if boolean == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        coordinate_list = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) 
        
        # drawing rectangle in frame
        for (x,y,w,h) in coordinate_list:
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

  
        # Display detected face
        cv.imshow("Live Face Detection", frame)
        # condition to break out of while loop
        if cv.waitKey(20) == ord('x'):
            break
capture.release()
cv.destroyAllWindows()