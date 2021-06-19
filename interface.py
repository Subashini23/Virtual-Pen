from tkinter import *
from PIL import ImageTk, Image
import io
import cv2
from urllib.request import urlopen
top = Tk()
w, h = top.winfo_screenwidth(), top.winfo_screenheight()
top.title("Paint")
top.geometry("%dx%d" %(w,h))
top.configure(bg='white')
myCanvas = Canvas(top,bg="white",height=h,width=w)
myCanvas.pack() 







