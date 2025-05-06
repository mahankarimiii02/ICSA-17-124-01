from tkinter import *
from tkinterweb import HtmlFrame



def start(ip) :
    snapshot_window = Toplevel()
    snapshot_frame = HtmlFrame(snapshot_window)  
    snapshot_frame.place(x=0, y=0, width=700, height=700)
    snapshot_frame.load_website("http://{}/onvif-http/snapshot?auth=YWRtaW46MTEK".format(ip))  
    snapshot_window.geometry('700x400')
    snapshot_window.mainloop()

