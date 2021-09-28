from tkinter import *
from PIL import ImageTk, Image
import io
import cv2
from urllib.request import urlopen
import numpy as np
from collections import deque 
import pyautogui
from tkinter import filedialog

top = Tk()
w, h = top.winfo_screenwidth(), top.winfo_screenheight()
top.title("Paint")
top.geometry("%dx%d" %(w,h))
top.configure(bg='white')
myCanvas = Canvas(top,bg="white",height=h,width=w)

image_bytes = urlopen("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdKpYyyVMK1PO9GDA-1Qkxbx1IobGA_JNplA&usqp=CAU").read()
data_stream = io.BytesIO(image_bytes)
photo = ImageTk.PhotoImage(Image.open(data_stream).resize((100,100)))

image_byte = urlopen("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcM3lfwRZTL-0EvgXtNPZyVXExG85EGsLDlQ&usqp=CAU").read()
data_strea = io.BytesIO(image_byte)
phot = ImageTk.PhotoImage(Image.open(data_strea).resize((100,100)))

font_one = urlopen("https://cdn160.picsart.com/upscale-269953521003211.png").read()
font_1 = io.BytesIO(font_one)
font1= ImageTk.PhotoImage(Image.open(font_1).resize((10,10)))

font_two = urlopen("https://cdn160.picsart.com/upscale-269953521003211.png").read()
font_2 = io.BytesIO(font_two)
font2= ImageTk.PhotoImage(Image.open(font_2).resize((15,15)))

font_th = urlopen("https://cdn160.picsart.com/upscale-269953521003211.png").read()
font_3 = io.BytesIO(font_th)
font3= ImageTk.PhotoImage(Image.open(font_3).resize((20,20)))

font_fo = urlopen("https://cdn160.picsart.com/upscale-269953521003211.png").read()
font_4 = io.BytesIO(font_fo)
font4= ImageTk.PhotoImage(Image.open(font_4).resize((25,25)))

font_fi = urlopen("https://cdn160.picsart.com/upscale-269953521003211.png").read()
font_5 = io.BytesIO(font_fi)
font5= ImageTk.PhotoImage(Image.open(font_4).resize((30,30)))

pencil = Button(top,bg = "black",image=photo,width=90,height = 80,pady=30,padx=50,command= lambda: fontColor("#000000"))
pencil.pack(side = RIGHT) 
pencil.place(x=w-190,y=100)

eraser = Button(top,bg = "black",image=phot,width=90,height = 80,  pady=30,padx=50, command= lambda: fontColor("#ffffff"))
eraser.pack(side = RIGHT)
eraser.place(x=w-100,y=100)

clear = Button(top,bg="black",text=" CLEAR ALL",fg="white",font="Helvetica",width=20,height=1, justify=LEFT,padx=10,pady=10,command= lambda: clearAll())
clear.pack(side = RIGHT)
clear.place(x=w-190,y=190)

fontOne = Button(top,bg="white",image=font1,border="0",pady=30,padx=50,command= lambda: fontSize(2))
fontOne.pack(side=RIGHT)
fontOne.place(x=w-165,y=300)

fontTwo = Button(top,bg="white",image=font2,border="0",pady=30,padx=50,command= lambda: fontSize(5))
fontTwo.pack(side=RIGHT)
fontTwo.place(x=w-140,y=296)

fontTh = Button(top,bg="white",image=font3,border="0",pady=30,padx=50,command= lambda: fontSize(10))
fontTh.pack(side=RIGHT)
fontTh.place(x=w-115,y=292)

fontFo = Button(top,bg="white",image=font4,border="0",pady=30,padx=50,command= lambda: fontSize(14))
fontFo.pack(side=RIGHT)
fontFo.place(x=w-88,y=289)

fontFi = Button(top,bg="white",image=font5,border="0",pady=30,padx=50,command= lambda: fontSize(20))
fontFi.pack(side=RIGHT)
fontFi.place(x=w-55,y=286)

label = Label( top, bg="black",pady=30,padx=50,width=80,height=5)
label.pack(side=RIGHT)
label.place(x=w-190,y=350)


White = urlopen("http://clipart-library.com/img/936535.png").read()
wh = io.BytesIO(White)
W = ImageTk.PhotoImage(Image.open(wh).resize((32,32)))
white = Button(top,bg="black",image=W,border="0",pady=30,padx=50,command= lambda: fontColor("#e3de4b"))
white.pack(side=RIGHT)
white.place(x=w-172,y=367)

Red = urlopen("https://i.redd.it/axorctfsk4v01.jpg").read()
re = io.BytesIO(Red)
R = ImageTk.PhotoImage(Image.open(re).resize((32,32)))
red = Button(top,bg="black",image=R,border="0",pady=30,padx=50,command= lambda: fontColor("#fc0303"))
red.pack(side=RIGHT)
red.place(x=w-125,y=366)

Green = urlopen("https://i.stack.imgur.com/6x4wL.png").read()
Gr = io.BytesIO(Green)
G = ImageTk.PhotoImage(Image.open(Gr).resize((30,30)))
green= Button(top,bg="black",image=G,border="0",pady=30,padx=50,command= lambda: fontColor("#03fc24"))
green.pack(side=RIGHT)
green.place(x=w-75,y=366)


Pink = urlopen("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjOm0gJsFFH36ohbJmto9nxdfi1dO30b8kcg&usqp=CAU").read()
Pk = io.BytesIO(Pink)
pin = ImageTk.PhotoImage(Image.open(Pk).resize((30,30)))
pink= Button(top,bg="black",image=pin,border="0",pady=30,padx=50,command= lambda: fontColor("#fc03b1"))
pink.pack(side=RIGHT)
pink.place(x=w-172,y=415)

Blue = urlopen("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScjzKWk5BieA1uI08leUieHc1xS6PnDiPwrw&usqp=CAU").read()
Bl = io.BytesIO(Blue)
blu = ImageTk.PhotoImage(Image.open(Bl).resize((30,30)))
blue= Button(top,bg="black",image=blu,border="0",pady=30,padx=50,command= lambda: fontColor("#0367fc"))
blue.pack(side=RIGHT)
blue.place(x=w-125,y=415)


Purple = urlopen("https://i.pinimg.com/736x/1f/a5/cc/1fa5cc20dfb8f6604051f73195326ed9.jpg").read()
purp = io.BytesIO(Purple)
ple = ImageTk.PhotoImage(Image.open(purp).resize((50,50)))
purple= Button(top,bg="black",image=ple,border="0",pady=30,padx=50,command= lambda: fontColor("#650680"))
purple.pack(side=RIGHT)
purple.place(x=w-85,y=405)



Camera = urlopen("https://www.kindpng.com/picc/m/403-4037368_tools-icons-png-png-download-camera-flash-icon.png").read()
cam = io.BytesIO(Camera)
cr= ImageTk.PhotoImage(Image.open(cam).resize((190,100)))
camera = Button(top,bg = "white",image=cr,width=200,height = 100,pady=30,padx=50,command= lambda: takeScreenShot())
camera.pack(side = RIGHT) 
camera.place(x=w-190,y=490)

myCanvas.pack() 



def setValues(x): 
   print("") 
   

cv2.namedWindow("Color detectors") 
cv2.createTrackbar("Upper Hue", "Color detectors", 
                   131, 180, setValues) 
cv2.createTrackbar("Upper Saturation", "Color detectors", 
                   255, 255, setValues) 
cv2.createTrackbar("Upper Value", "Color detectors",  
                   125, 255, setValues) 
cv2.createTrackbar("Lower Hue", "Color detectors", 
                   108, 180, setValues) 
cv2.createTrackbar("Lower Saturation", "Color detectors",  
                   137, 255, setValues) 
cv2.createTrackbar("Lower Value", "Color detectors",  
                   49,255, setValues) 
  


# The kernel to be used for dilation purpose 
kernel = np.ones((5,5), np.uint8)
#uint8 => 8 bit unsigned integer => 0-255
#np.ones => returns an array filled with ones
#(5,5) size of array here 2d array of 5column 5row

top.update()
# Loading the default webcam of PC. 
cap = cv2.VideoCapture(0)


canvas = None
x1,y1=0,0
c = "#000000"
w = 2
# Keep looping 
while True:
    # Reading the frame from the camera
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.namedWindow("Tracking", cv2.WINDOW_NORMAL)
        # Flipping the frame to see same side of yours 

    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    if canvas is None:
       canvas = np.zeros_like(frame)

    # Getting the updated positions of the trackbar 
    # and setting the HSV values 
    u_hue = cv2.getTrackbarPos("Upper Hue", 
                               "Color detectors") 
    u_saturation = cv2.getTrackbarPos("Upper Saturation", 
                                      "Color detectors") 
    u_value = cv2.getTrackbarPos("Upper Value", 
                                 "Color detectors") 
    l_hue = cv2.getTrackbarPos("Lower Hue", 
                               "Color detectors") 
    l_saturation = cv2.getTrackbarPos("Lower Saturation", 
                                      "Color detectors") 
    l_value = cv2.getTrackbarPos("Lower Value", 
                                 "Color detectors") 
    Upper_hsv = np.array([u_hue, u_saturation, u_value]) 
    Lower_hsv = np.array([l_hue, l_saturation, l_value]) 
   
    # Identifying the pointer by making its  
    # mask 
    Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv) 
    Mask = cv2.erode(Mask, kernel, iterations = 2) 
    Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel) 
    Mask = cv2.dilate(Mask, kernel, iterations = 2) 
   
    # Find contours for the pointer after  
    # idetifying it
    #cnts => all the contours found
    #_ => hierarchy of the contours
    cnts, _ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)

    #three arguments 1.source image 2.contour retrieval mode 3.contour approximation method => cv2.CHAIN_APPROX_SIMPLE => instead of showing the full boundary shows only the end points to save 
    #cv2_RETR_EXTERNAL gives "outer" contours, so if you have (say) one contour enclosing another (like concentric circles), only the outermost is given.

    # Ifthe contours are formed 
    #drawing contours
    if len(cnts) > 0:
        def clearAll():
           myCanvas.delete("all")
        def fontColor(color):  
            global c
            c=color
        def fontSize(size):  
            global w
            w=size
        def takeScreenShot():
           myScreenshot = pyautogui.screenshot()
           file_path = filedialog.asksaveasfilename(defaultextension='.png')
    
           myScreenshot.save(file_path)
        # sorting the contours to find biggest area  
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        print("Color",c)
        # Get the radius of the enclosing circle 
        # around the found contour
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
          
        # Draw the circle around the contour
        cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 255), 2)
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        if(x1==0 and y1==0):
           x1,y1=cX,cY
        else:
           #canvas=cv2.line(canvas,(x1,y1),(cX,cY),[255,255,255],4)
           myCanvas.create_line(x1, y1, cX, cY,fill=c,width= w)
           
        x1,y1=cX,cY
        
    else:
       x1,y1=0,0
     
    frame=cv2.add(frame,canvas)
    top.update()     
        
        
        
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break  
   
    # Show all the windows 
    cv2.imshow("Tracking", frame) 
    cv2.imshow("mask", Mask) 
    # If the 'q' key is pressed then stop the application  
   

# Release the camera and all resources 
cap.release() 
cv2.destroyAllWindows() 

