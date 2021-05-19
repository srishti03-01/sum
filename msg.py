import requests
import json
from tkinter.messagebox import showinfo,showerror
from tkinter import *

def  send_sms (number, message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    val={
        'authorization': '67D1oV3IOHUc9FkMTuCKxfJ2mEANiSWysQdlGB84rtXLYjZen5Io8d04DqjfFBKhUzMOplcxEYTQ1n9C',
        'sender_id': 'FASTSMS',
        'message':'message',
        'language': 'english',
        'route' : 'p',
        'number' : 'number',

    }
    response=requests.get("https://www.fast2sms.com/dev/bulkV2",params=val)
    dic=response.json();
    print(dic);

    return dic.get('return');


send_sms("9770236266","this is my msg");
def btn_clk():
    num=textNumber.get()
    msg=textMsg.get("%0",end)
    send_sms (num,msg)
    if r== true:
        showinfo("send secessful","sucessfully sent")
    else:
        showerror("error", "something went wrong")



root=Tk()
root.title("Message sender")
root.geometry("400x550")
fnt=("helvetia", "22", "bold")

textNumber = Entry(root, font=fnt)
textNumber.pack(fill=BOTH, pady=20)

#textMsg=text(root)
#textMsg.pack(fill=X)

sendBtn=Button(root,text ="send sms ", command=btn_click)
sendBtn.pack()

root.mainloop()
