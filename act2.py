from tkinter import*
window=Tk()
window.geometry("400x300")
window.title("My First Tkinter grid")
for i in range(4):
   for j in range(5):
      frame=Frame(master=window,relief="ridge",borderwidth=10)
      frame.grid(row=i,column=j,padx=5,pady=5)
      label=Label(master=frame,text=f"row{i}\ncolmn{j}")
      label.pack()
window.mainloop()
