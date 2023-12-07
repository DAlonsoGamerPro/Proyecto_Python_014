from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()
root.title("Banderas de países")
root.geometry("600x400")
root.configure(background="lightblue")

get_input = Entry(root)
show_label = Label(root)

india_map = ImageTk.PhotoImage(Image.open ("India.jpg"))
america_map = ImageTk.PhotoImage(Image.open ("America.jpg"))
australia_map = ImageTk.PhotoImage(Image.open ("Australia.png"))
philippines_map = ImageTk.PhotoImage(Image.open ("Filipinas.png"))
japan_map = ImageTk.PhotoImage(Image.open ("Japon.jpg"))

maps_dictionary = { "Índia" : india_map , 
                    "América" : america_map ,
                    "Australia" : australia_map ,
                    "Filipinas" : philippines_map,
                    "Japón" : japan_map,}

def showMaps():
    try:
        map_name = get_input.get()
        show_label['image'] = maps_dictionary[map_name]
    except:
        messagebox.showinfo("Upps...", "Lo sentimos, ese nombre no nos suena D:")

btn = Button(root , text="Mostrar mapa", bg="green", command=showMaps)
get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
show_label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()