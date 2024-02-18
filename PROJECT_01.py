class Library:
    def __init__(self, book_name,book_writer, book_year,book_number):
       self.book_name = book_name
       self.book_writer = book_writer
       self.book_year = book_year
       self.book_number = book_number

    def add(self):
        self.book_name = input("Enter the book's name")
        self.book_writer = input("Enter the book's writer")
        self.book_year = input("Enter the book's year of publication")
        self.book_number = input("Enter the book's number of page ")
        with open("books.txt", "a+") as file:
            file.write("NAME: " + self.book_name + "\n")
            file.write("WRITER " + self.book_writer + "\n")
            file.write("YEAR OF PUBLİCATİON" + self.book_year + "\n")
            file.write("NUMBER OF PAGE: " + self.book_number+ "\n")
        print("SAVED THE İNFORMATİON.")
    def show(self):
        with open("books.txt", "r") as file:
            list = file.readlines()
            for line in list:
                print(line.strip())

    def remove(self):

        deleted = input()
        with open("books.txt", "r") as file:
            list = file.readlines()
        with open("books.txt", "w") as file:
            for line in list:
                if deleted not in line:
                    file.write(line)


if __name__ == "__main__":
    from tkinter import Tk, Canvas, Frame, Label
    from PIL import Image, ImageTk
    from tkcalendar import DateEntry

    master = Tk()
    canvas = Canvas(master, height=500, width=1000)
    canvas.pack()

    frame_ust = Frame(master, bg="#8B4513")
    frame_ust.place(relx=0, rely=0.0, relwidth=1, relheight=1.15)
    frame_sag = Frame(master, bg="#CD853F")
    frame_sag.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
    frame_sol = Frame(master, bg="#CD853F")
    frame_sol.place(relx=0.1, rely=0.21, relwidth=0.35, relheight=0.6)

    # Resmi yükleme işlemi
    image = ImageTk.PhotoImage(Image.open("C:/Users/pc/Desktop/kalender.jpg").resize((100, 100)))

    image_label = Label(frame_sag, image=image)
    image_label.pack(side="right", padx=1, pady=1)

    baslik_tipi = Label(frame_sag, bg="#8B4513", text="LİBRARY SYSTEM", font=("Arial", 20, "italic"))
    baslik_tipi.pack(padx=10, pady=10, side="bottom")
    yan_yazi1 = Label(frame_sol, bg="#8B4513", text="SHOW INFORMATION", font=("Arial", 12, "italic"))
    yan_yazi1.grid(row=0, column=0, padx=10, pady=10)

    yan_yazi2 = Label(frame_sol, bg="#8B4513", text="ADD NEW BOOK", font=("Arial", 12, "italic"))
    yan_yazi2.grid(row=1, column=0, padx=10, pady=10)

    yan_yazi3 = Label(frame_sol, bg="#8B4513", text="REMOVE BOOK", font=("Arial", 12, "italic"))
    yan_yazi3.grid(row=2, column=0, padx=10, pady=10)

    frame_sol.grid_columnconfigure(0, weight=1)
    tarih_tipi = Label(frame_sag, bg="#8B4513", text="calender", font=("Arial", 20, "italic"))
    tarih_tipi.pack(padx=10, pady=10, side="right")

    tarih_secici = DateEntry(frame_sag, width=12, font=("Arial"), background="white", fg="brown", locale="de_DE")

    tarih_secici.pack(padx=10, pady=10, side="right")
    master.mainloop()

    from colorama import Fore

    print(Fore.LIGHTCYAN_EX + "")
    lib = Library("", "", "", "")
    print("*******************************************************")
    print("*               WELCOME TO LİBRARY SYSTEM             *")
    print("*          PLEASED ENTER THE CHOİCE TO THE            *")
    print("*  1-SHOW INFORMATION                                 *")
    print("*  2-ADD NEW BOOK                                     *")
    print("*  2-REMOVE BOOK                                      *")
    print("*******************************************************")


    from colorama import Fore
    while True:
        choice = input("* ENTER YOUR CHOİCE                                   *")
        print(Fore.LIGHTWHITE_EX + "")
        if choice == "2":
            print("ADDİNG FROM LİBRARY.")
            lib.add()
        elif choice == "1":
            print("INFORMATION SHOW")
            lib.show()
        elif choice == "3":
            print("BOOK NAME TO BE DELETED ")
            lib.remove()
        elif choice == "q":
            break
        else:
            print("You made the wrong choice. Please do it right.")