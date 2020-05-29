# Name Number Email City Comment

#=================================================================#
from Tkinter import *
from tkMessageBox import *
from random import *



window=Tk()
#code to add widgets goes here...
window.title("Contact Form")
window.geometry("500x600+100+50")
# geometry( " widthxheight + xoffset + yoffset " )
window.configure(bg="red")
window["bg"]="#bfd98b"#3#856ff2

labels=["Name","Email","City","Cell phone"]
# lbls=range(4)
# def helloCallBack():
# 	showinfo("Customer Information","Thank you for registering!")
# for i in range(4):
	# ct = [randrange(256) for x in range(3)]
 #   	brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
 #   	ct_hex = "%02x%02x%02x" % tuple(ct)
 #   	bg_colour = '#' + "".join(ct_hex)
 #   	l= Label(window,text=labels[i],fg='white' if brightness < 120 else 'Black')
 #   	l.place(x=20, y=30 +i*30,width=120, height=25)

#This creates the lable widget
L1=Label(window,text=labels[0],fg='blue',bg='white')
L2=Label(window,text=labels[1],fg='blue',bg='white')
L3=Label(window,text=labels[2],fg='blue',bg='white')
L4=Label(window,text=labels[3],fg='blue',bg='white')
#grid method is used to arrange labels in respective rows and columns as specified
L1.grid(row=0,column=1,sticky=W,padx=25,pady=2)
L2.grid(row=1,column=1,sticky=W,padx=25,pady=2)
L3.grid(row=2,column=1,sticky=W,padx=25,pady=2)
L4.grid(row=3,column=1,sticky=W,padx=25,pady=2)

#This creates the entry widgets for the user to input information
U1=Entry(window,bg="red")
U2=Entry(window,bg="red")
U3=Entry(window,bg="red")
U4=Entry(window,bg="red")
#This arranges the entry widgets
U1.grid(row=0,column=2,padx=5,pady=2)
U2.grid(row=1,column=2,pady=2)
U3.grid(row=2,column=2,pady=2)
U4.grid(row=3,column=2,pady=2)

# B1=Button(window,text="Submit",command=helloCallBack).pack(x=150,y=170,width=120,height=25)
window.mainloop()

print(dir(window))


# print("")
# print(Tk()) #Prints a dot .
######print(Tkinter)#This prints the directory where Tkinter is located in. 


#=================================================================#
