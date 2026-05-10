from tkinter import *
def Createbtn(ch,r,c):
    if ch=="=":
        btn=Button(root,text=ch,height=2,width=10,command=btnEqual)
        btn.grid(row=r, column=c,columnspan=2)
    else:
        btn=Button(root,text=ch,height=2,width=5,command=lambda:btnClick(ch))
        btn.grid(row=r,column=c)

    def btnClick(ch):
        if ch=="C":
            txtbox.delete(1.0,END)
        elif ch=="+/-":
            ans=txtbox.get(1.0,END).strip()
            if ans[0:1]=="-":
                ans=ans[1:]
            else:
                ans="-"+ans
                txtbox.delete(1.0,END)
                txtbox.insert(END,ans,"right")
        elif ch=="1/x":
            if len(txtbox.get(1.0,END).strip())>0:
                ans=str(eval(txtbox.get(1.0,END)))
                ans="1/"+ans
                ans=eval(ans)
                txtbox.delete(1.0,END)
                txtbox.insert(END,ans,"right")
        else:
                txtbox.insert(END,ch,"right")
def btnEqual():
    ans=eval(txtbox.get(1.0,END))
    txtbox.delete(1.0,END)
    txtbox.insert(END,ans,"right")


root=Tk()
root.title("Cals")
root.geometry("200x270")

txtbox=Text(root,height=2,width=23)
txtbox.grid(row=0,columnspan=4,padx=5,pady=8)
txtbox.tag_config("right",justify="right")

lst=["7","8","9","/","4","5","6","*","1","2","3","-","+/-","0",".","+","1/x","C","="]
r=1
c=0
for ch in lst:
    Createbtn(ch,r,c)
    c+=1
    if c>3:
        c=0
        r+=1

root.mainloop()
