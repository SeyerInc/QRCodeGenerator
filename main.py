import tkinter as Lo
import pyqrcode # pip install pyqrcode
from PIL import Image # pip install Pillow

def showMyCode():
    """
        Create window instance and define name and window size
    """
    qrLo = Lo.Tk()
    qrLo.title("QR Generator")
    qrLo.geometry("400x150")
    qrLo.resizable(0,0)
    """
             Make globally accessible 
    """
    global qrUrl
    global qrImgName

    qrUrl = Lo.StringVar()
    qrImgName = Lo.StringVar()
    """
            Select calendar year and process "calendar()" method
            to retrive that years calendar
    """
    url_label = Lo.Label(qrLo, text="Enter url", font=("Verdana", 10, "bold"))
    url_entry = Lo.Entry(qrLo, text=qrUrl, font=("Verdana", 10, "bold"))
    image_label = Lo.Label(qrLo, text="Enter the image name", bg="white", font=("Times", 10, "bold"))
    image_entry = Lo.Entry(qrLo, textvariable=qrImgName, font=("Times", 10, "bold"))
    sub_btn = Lo.Button(qrLo, text="Submit", command=runCode)
    """
                Create grid system format and add values to your grid.
    """
    url_label.grid(row=0, column=0)
    url_entry.grid(row=0, column=1)
    image_label.grid(row=1, column=0)
    image_entry.grid(row=1, column=1)
    sub_btn.grid(row=2, column=1)
    """
                Run your application
    """
    qrLo.mainloop()

def runCode():
    qr_Url = qrUrl.get()
    qr_ImgName = qrImgName.get()

    qrCode = pyqrcode.create(qr_Url)
    
    qrCode.svg(qr_ImgName + ".svg", scale=8)
    qrCode.png(qr_ImgName + ".png", scale=6)

    image = Image.open(qr_ImgName + ".png")
    image.show()

showMyCode()


