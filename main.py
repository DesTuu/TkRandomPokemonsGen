import csv
import tkinter as tk
import random
from PIL import ImageTk

ran = random.choice(range(0, 100))

def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def fetch_db():
    c = 0
    id = []
    pokemon = []
    with open("pokemon.csv", "r") as data:
        reader = csv.reader(data)
        for row in reader:
            id.append(row[0])
            pokemon.append(str(row[1]).title())
            c += 1
            if c>=638:
                break
    pokemon = [random.choice(pokemon) for i in range(6)]
    return pokemon

def load_frame1():
    clear(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="assets/dess.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg='blue')
    logo_widget.image = logo_img #JEŚLI TEGO NIE ZROBIMY TO NIE WYŚWIETLI NAM OBRAZKA W FUNKCJI
    logo_widget.pack(pady=30, padx=30)
    tk.Label(frame1,
             text="TheLegend27",
             bg='blue',
             fg='gold',
             font=('Arial Black', 30)).pack(pady=30, padx=30)
    tk.Button(frame1,
              text="NEXT",
              font=('Arial Black', 30),
              bg="red",
              fg="white",
              cursor="hand2",
              activebackground="yellow",
              activeforeground="green",
              command=lambda: load_frame2()).pack(pady=30, padx=30)

def load_frame2():
    clear(frame1)
    frame2.tkraise()
    pokemon = fetch_db()
    logo_img = ImageTk.PhotoImage(file="assets/channel.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg='blue')
    logo_widget.image = logo_img  # JEŚLI TEGO NIE ZROBIMY TO NIE WYŚWIETLI NAM OBRAZKA W FUNKCJI
    logo_widget.pack(pady=10, padx=30)
    for i in pokemon:
        tk.Label(frame2,
                 text=i,
                 bg='dark blue',
                 fg='white',
                 font=('Arial', 18)).pack(pady=10, padx=30)
    tk.Button(frame2,
              text="BACK",
              font=('Arial Black', 30),
              bg="red",
              fg="white",
              # cursor="hand2",
              activebackground="yellow",
              activeforeground="green",
              command=lambda: load_frame1()).pack(pady=10, padx=30)

root = tk.Tk()
root.title("Random Pokemons")
# root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 3
y = int(root.winfo_screenheight() * 0.001)
root.geometry('500x600+' + str(x) + '+' + str(y))
frame1 = tk.Frame(root, width=500, height=600, bg='blue')
frame2 = tk.Frame(root, bg='blue')
for frame in (frame1, frame2):
    frame.grid(row=ran, column=ran, sticky="nesw")

load_frame1()

# root.attributes('-fullscreen', True)
root.mainloop()