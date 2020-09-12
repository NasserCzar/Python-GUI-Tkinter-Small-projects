from tkinter import *

root = Tk()
root.title('Industrial Group Holding')
root.iconbitmap(r'C:/Users/COMPUTER 2000/Desktop/GUI Testing/logo.ico')
root.geometry("600x800")

# Welcome Text 
myLabel1 = Label(root, text="           <<<       ").grid(row=0 ,column=0)
myLabel2 = Label(root, text="Industrial Group Holding").grid(row=0 ,column=1)
myLabel3 = Label(root, text=" المجموعة الصناعية  القابضة   ").grid(row=0 ,column=2)
myLabel4 = Label(root, text="           >>>       ").grid(row=0 ,column=3)
myLabel5 = Label(root, text="           ").grid(row=1 ,column=0)
myLabel6 = Label(root, text="           ").grid(row=2 ,column=0)
myLabel7 = Label(root, text="           ").grid(row=3 ,column=0)
myLabel8 = Label(root, text="           ").grid(row=4 ,column=0)
myLabel9 = Label(root, text="           ").grid(row=5 ,column=0)
myLabel10 = Label(root, text="           ").grid(row=6 ,column=0)


# Login
myLabel2 = Label(root, text="USER").grid(row=5 ,column=1)
myLabel3 = Label(root, text="PASSWORD ").grid(row=6 ,column=1)

# Entry Login
USER1 = Entry(root, width=50 ,borderwidth=4)
USER1.grid(row=5 ,column=2)
PASSWORD1 = Entry(root, width=50 ,borderwidth=4)
PASSWORD1.grid(row=6 ,column=2)




root.mainloop()