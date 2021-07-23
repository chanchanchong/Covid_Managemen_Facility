from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win

class CovidFacilityManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Covid Facility Management System")
        self.root.geometry("1550x800+-10+0")

    # ============1st img =======
        img1=Image.open(r"C:\Users\Tria\Documents\Covid_Managemen_Facility\img\hotel1.png")
        img1=img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg = Label(self.root, image = self.photoimg1, bd = 4, relief = RIDGE)
        lblimg.place(x = 0, y = 0, width = 1550, height = 140)

        # ========== logo =========
        img2 = Image.open(r"C:\Users\Tria\Documents\Covid_Managemen_Facility\img\logo.png")
        img2 = img2.resize((230, 230), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image = self.photoimg2, bd = 4, relief = RIDGE)
        lblimg.place(x = 0, y = -50, width = 230, height = 230)

        # ======== title ============
        lbl_title = Label(self.root, text = "Covid Facility Management System", font = ("Tokyo", 25, ), bg = "gray", fg = "white", bd = 4, relief = RIDGE)
        lbl_title.place(x = 230, y = 140, width = 1310, height = 50)

        # ======== main frame ===========
        main_frame = Frame(self.root, bd = 4, relief = RIDGE)
        main_frame.place(x = 0, y = 190, width = 1550, height = 620)

        # ======== menu =====================
        lbl_title = Label(main_frame, text = "MENU", font = ("Times New Roman", 20, "bold"), bg = "black", fg = "gold", bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y = 0, width = 230)

         # ======== btn frame ===========
        btn_frame = Frame(main_frame, bd = 4, relief = RIDGE)
        btn_frame.place(x = 0, y = 35, width = 228, height = 190)

        cust_btn = Button(btn_frame, text = "CUSTOMER", command = self.cust_details, width = 22, font = ("Times New Roman", 14, "bold"), bg = "black", fg = "gold", bd = 0)
        cust_btn.grid(row = 0, column = 0, pady = 1)

        room_btn = Button(btn_frame, text = "ROOM",width = 22, font = ("Times New Roman", 14, "bold"), bg = "black", fg = "gold", bd = 0)
        room_btn.grid(row = 1, column = 0, pady = 1)

        details_btn = Button(btn_frame, text = "DETAILS",width = 22, font = ("Times New Roman", 14, "bold"), bg = "black", fg = "gold", bd = 0)
        details_btn.grid(row = 2, column = 0, pady = 1)

        report_btn = Button(btn_frame, text = "REPORT",width = 22, font = ("Times New Roman", 14, "bold"), bg = "black", fg = "gold", bd = 0)
        report_btn.grid(row = 3, column = 0, pady = 1)

        logout_btn = Button(btn_frame, text = "LOG OUT",width = 22, font = ("Times New Roman", 14, "bold"), bg = "black", fg = "gold", bd = 0)
        logout_btn.grid(row = 4, column = 0, pady = 1)

        # ================ right side image =========
        img3 = Image.open(r"C:\Users\Tria\Documents\Covid_Managemen_Facility\img\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(main_frame, image = self.photoimg3, bd = 4, relief = RIDGE)
        lblimg.place(x = 225, y = 0, width = 1310, height = 590)


        # ============= down images ===============
        img4 = Image.open(r"C:\Users\Tria\Documents\Covid_Managemen_Facility\img\slide3.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg = Label(main_frame, image = self.photoimg4, bd = 4, relief = RIDGE)
        lblimg.place(x = 0, y = 225, width = 230, height = 210)

        img5 = Image.open(r"C:\Users\Tria\Documents\Covid_Managemen_Facility\img\slide3.jpg")
        img5 = img3.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg = Label(main_frame, image = self.photoimg5, bd = 4, relief = RIDGE)
        lblimg.place(x = 0, y = 420, width = 230, height = 190)



    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=CovidFacilityManagementSystem(root)
    root.mainloop()  