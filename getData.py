# this program collects data from the camera and from the microphone
# saves the camera data in the DacaC folder
# saves the microphone data in the DataM folder
    # use of audio data still under consideration

#imports
import numpy as np
import cv2
import os
import time

class dataColector():

    #initialize the class
    def __init__(self):
        self.vidcap = cv2.VideoCapture(0)
        #create DataC and DataM folders if not existent
        if not os.path.exists("DataC"):
            os.makedirs("DataC")
        if not os.path.exists("DataM"):
            os.makedirs("DataM")

    #function to collect one instance of data from the camera
    def collectCameraData(self):
        if self.vidcap.isOpened():
            ret, frame = self.vidcap.read()
            if ret:
                cv2.imshow('Frame', frame)
            else:
                print("frame not captured")
        else:
            print("cannot open camera")

        #save the frame in the DataC folder
        #the filename is the following: day_month_year_hour_minute_second_millisecond.jpg
        filename = time.strftime("%d_%m_%Y_%H_%M_%S_%f") + ".jpg"
        cv2.imwrite(os.path.join("DataC", filename), frame)

    #function to collect one instance of data from the microphone
    def collectMicrophoneData(self):
        pass


if __name__ == "__main__":
    #initialize the class
    data = dataColector()
    #creates an infinite loop that runs every second
    #it collect the data from the camera
    #and can be interrupted by the user
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        data.collectCameraData()

    #release the camera
    data.vidcap.release()
    #destroy all windows
    cv2.destroyAllWindows()
    #print a message
    print("data collected")
    #exit the program
    exit()
