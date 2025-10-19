from tkinter import*
root=Tk()
root.title ("To Do List")
root.geometry("400x600")
root.config(bg="lightblue")
def add_task():
    task=entry.get()
    if task!="" :
        listbox.insert(END,task)
        entry_task.delete(0,END)
def delete_task():
    selected=listbox.curselection() 
    if selected:
       listbox.delete(selected)
Label(root,text="My To Do List",bg="#B88E23",font=("Airial",14,"bold")).pack(pady=10)
entry=Entry(root,width=25)
entry.pack()
user_input=entry.get()
btn=Button(root,text="add task", bg="green",fg="white",command=add_task).pack(padx=5)
btn=Button(root,text="delete task",bg="tomato",fg="white",command=delete_task).pack(pady=5)
listbox=Listbox(root,width=30,height=15)
listbox.pack(pady=10)
root.mainloop()
           
            


