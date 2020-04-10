from tkinter import *
from tkinter import messagebox
import math
from tkinter import simpledialog
class FaceDetectionSystem(object):
    def face_detector(self):
        from face_Detection import FaceDetection
        FaceDetection()
    def photo_scraper(self):
        from photo_scraper_from_facebook import PhotoScraper
        NAME=simpledialog.askstring(title="NAME", prompt="Enter the Name of the person:")
        FB_ID=simpledialog.askstring(title="FACEBOOK ID", prompt="Enter the FB_Id of the Person:")
        PhotoScraper(NAME,FB_ID)
    def sample(self):
        print("Have You Called Me")
    def finish(self):
        msg=messagebox.askquestion('CHECK','do you want to quit')
        if(msg=='yes'):
            self.root.destroy()

    def __init__(self):
        self.place_value=0
        self.root=Tk()
        self.root.title("Face Detecting System using Facebook")
        self.root.geometry("510x550")
        self.root['bg']='dark slate gray'
        l_0=Label(self.root,text="FACE DETECTION USING FACEBOOK",bg="red",fg="white",width=36)
        l_0.config(font=('courier',17,'bold'))
        l_0.place(x=0,y=0)
        photo=PhotoImage(file="image_lpu1.png")
        img=Label(self.root,image=photo,relief=RAISED)
        img.image=photo
        img.place(x=150,y=40)
        exitt=Button(self.root,text='EXIT',bg='gold',width=12,activebackground="red",relief=RIDGE,command=self.finish)
        exitt.config(font=('courier',10,'bold'))
        exitt.place(x=200,y=500)
        self.ButtonsFunction()
    def ButtonsFunction(self):
        self.photo_feeder=Button(self.root,text='Photo Feeder',bg='gold',fg='black',activebackground='green',relief=RIDGE,width=30,command=self.photo_scraper)
        self.photo_feeder.config(font=('times',10,'bold'))
        self.photo_feeder.place(x=150,y=300)
        self.face_detector=Button(self.root,text='Face Detector',bg='gold',fg='black',activebackground='green',relief=RIDGE,width=30,command=self.face_detector)
        self.face_detector.config(font=('times',10,'bold'))
        self.face_detector.place(x=150,y=360)
start=FaceDetectionSystem()
print(start)
