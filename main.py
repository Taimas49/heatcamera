import cv2 as cv
capture = cv.VideoCapture(0) #to open Camera
from database import Database
#Загружаем натренированную модель
pretrained_model = cv.CascadeClassifier("face.xml") 
temperature = 667
#Инициализируем класс для работы с БД
db = Database()
#Проверка работы методов
db.ConnectToDb()
db.InsertToDB(temperature)
db.CommitQuery()
db.CloseConnection()


while True:
    boolean, frame = capture.read()
    if boolean == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        coordinate_list = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) 
        
        # Отрисовка прямоугольника вокруг лица
        for (x,y,w,h) in coordinate_list:
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
  
        # Показ опознанного лица
        cv.imshow("Live Face Detection", frame)
        # Условие что бы выйти из цикла while:True
        if cv.waitKey(20) == ord('x'):
            break
capture.release()
cv.destroyAllWindows()