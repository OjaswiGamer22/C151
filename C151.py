from tkinter import *
import random
root=Tk()
root.title("Sales Application")
root.geometry("500x500")
label_month=Label(root)
label_month.place(relx=0.5,rely=0.1,anchor=CENTER)
label_profit=Label(root)
label_profit.place(relx=0.5,rely=0.2,anchor=CENTER)
month=("Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec")
profit=(10000,20000,50000,690000,560000,700000,60000,9600000,540000,89000,7900000,680000)
label_month["text"]="Months:  "+str(month)
label_profit["text"]="Profit:  "+str(profit)
def maxprofit():
    profit_max=max(profit)
    profit_max_index=profit.index(profit_max)
    profit_max_month=month[profit_max_index]
    label_maxp["text"]="The maximum profit of  "+str(profit_max)+" in the month of "+str(profit_max_month)
button_max=Button(root,text="Show Max Profitable Month ",bg="royalblue",command=maxprofit)
button_max.place(relx=0.5,rely=0.3,anchor=CENTER)
label_maxp=Label(root)
label_maxp.place(relx=0.5,rely=0.4,anchor=CENTER)
def minprofit():
    profit_min=min(profit)
    profit_min_index=profit.index(profit_min)
    profit_min_month=month[profit_min_index]
    label_minp["text"]="The minimum profit of  "+str(profit_min)+" in the month of "+str(profit_min_month)
button_min=Button(root,text="Show Min Profitable Month ",bg="royalblue",command=minprofit)
button_min.place(relx=0.5,rely=0.5,anchor=CENTER)
label_minp=Label(root)
label_minp.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()

