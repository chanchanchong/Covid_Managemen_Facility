from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Covid Facility Management System")
        self.root.geometry("1050x560+220+220")

 # ======== title ============
        lbl_title = Label(self.root, text = "ADD CUSTOMER DETAILS", font = ("Tokyo", 18, "bold"), bg = "gray", fg = "white", bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y = 0, width = 1050, height = 50)

# ============ Label Frame =============
        labelframeleft = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Customer Details", font = ("Recursive", 14, "bold"), padx = 2)
        labelframeleft.place(x = 5, y= 50, width = 425, height = 500)

# ===================== labels and entry ===========

#cust ref
        lbl_cust_ref = Label(labelframeleft, font = ("Recursive", 11, "bold"), text = "Customer Ref", padx = 2, pady = 6)
        lbl_cust_ref.grid(row = 0, column = 0, sticky = W)

        enty_ref = ttk.Entry(labelframeleft, font = ("Recursive", 11), width = 29)
        enty_ref.grid(row = 0, column = 1)

#cust name
        cname = Label(labelframeleft, font = ("Recursive", 11, "bold"), text = "Customer's Name: ", padx = 2, pady = 6)
        cname.grid(row = 1, column = 0, sticky = W)
        txtcname = ttk.Entry(labelframeleft, font = ("Recursive", 11), width = 29)
        txtcname.grid(row = 1, column = 1)

#mother name
        lblmname = Label(labelframeleft, font = ("Recursive", 11, "bold"), text = "Mother's Name: ", padx = 2, pady = 6)
        lblmname.grid(row = 2, column = 0, sticky = W)
        txtmname = ttk.Entry(labelframeleft, font = ("Recursive", 11), width = 29)
        txtmname.grid(row = 2, column = 1)

#gender combobox
        label_gender = Label(labelframeleft, font =  ("Recursive", 11, "bold"), text = "Gender: ", padx = 2, pady = 6)
        label_gender.grid(row = 3, column = 0, sticky = W)

        combo_gender = ttk.Combobox(labelframeleft, font =  ("Recursive", 11), width = 27, state = "readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row = 3, column = 1)        

#post code
        lblPostCode = Label(labelframeleft, font = ("Recursive", 11, "bold"), text = "Post Code: ", padx = 2, pady = 6)
        lblPostCode.grid(row = 4, column = 0, sticky = W)
        txtPostCode = ttk.Entry(labelframeleft, font = ("Recursive", 11), width = 29)
        txtPostCode.grid(row = 4, column = 1)

#mobile number
        lblMobile = Label(labelframeleft, font = ("Recursive", 11, "bold"), text = "Mobile Number: ", padx = 2, pady = 6)
        lblMobile.grid(row = 5, column = 0, sticky = W)
        txtMobile = ttk.Entry(labelframeleft, font = ("Recursive", 11), width = 29)
        txtMobile.grid(row = 5, column = 1)   

#email 
        lblemail = Label(labelframeleft, font = ("Recursive", 11, "bold"), text = "Email: ", padx = 2, pady = 6)
        lblemail.grid(row = 6, column = 0, sticky = W)
        txtemail = ttk.Entry(labelframeleft, font = ("Recursive", 11), width = 29)
        txtemail.grid(row = 6, column = 1)

#nationality
        lblemail = Label(labelframeleft, font = ("Recursive", 11, "bold"), text = "Nationality: ", padx = 2, pady = 6)
        lblemail.grid(row = 7, column = 0, sticky = W)

        combo_National = ttk.Combobox(labelframeleft, font = ("Recursive", 11), width = 27, state = "readonly")
        combo_National["value"] = ("Filipino", "American", "Japanese")
        combo_National.current(0)
        combo_National.grid(row = 7, column = 1)

#idproff tpye combobox 
        lbIdProof = Label(labelframeleft, font = ("Recursive", 11, "bold"), text = "ID: ", padx = 2, pady = 6)
        lbIdProof.grid(row = 8, column = 0, sticky = W)

        combo_National = ttk.Combobox(labelframeleft, font = ("Recursive", 11), width = 27, state = "readonly")
        combo_National["value"] = ("Driving", "Passport", "National")
        combo_National.current(0)
        combo_National.grid(row = 8, column = 1)

#id number   
        lblIdNumber = Label(labelframeleft, font = ("Recursive", 11, "bold"), text = "ID Number: ", padx = 2, pady = 6)
        lblIdNumber.grid(row = 9, column = 0, sticky = W)
        txtIdNumber = ttk.Entry(labelframeleft, font = ("Recursive", 11), width = 29)
        txtIdNumber.grid(row = 9, column = 1)

#address  
        lblAddress = Label(labelframeleft, font = ("Recursive", 11, "bold"), text = "Address: ", padx = 2, pady = 6)
        lblAddress.grid(row = 10, column = 0, sticky = W)
        txtAddress = ttk.Entry(labelframeleft, font = ("Recursive", 11), width = 29)
        txtAddress.grid(row = 10, column = 1)

#============ btn =============
        btn_frame = Frame(labelframeleft, bd = 2, relief = RIDGE)
        btn_frame.place(x = 0, y = 420, width = 412, height = 40)

        btnAdd = Button(btn_frame, text = "Add", font = ("Palatino Linotype", 13, "bold"), bg = "gray", fg = "white", width = 8)
        btnAdd.grid(row = 0, column = 0, padx = 1)

        btnUpdate = Button(btn_frame, text = "Update", font = ("Palatino Linotype", 13, "bold"), bg = "gray", fg = "white", width = 8)
        btnUpdate.grid(row = 0, column = 1, padx = 1)

        btnDelete = Button(btn_frame, text = "Delete", font = ("Palatino Linotype", 13, "bold"), bg = "gray", fg = "white", width = 8)
        btnDelete.grid(row = 0, column = 2, padx = 1)

        btnReset = Button(btn_frame, text = "Reset", font = ("Palatino Linotype", 13, "bold"), bg = "gray", fg = "white", width = 8)
        btnReset.grid(row = 0, column = 3, padx = 1)

# ============ Label Frame =============
        TableFrame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details and Search System", font = ("Recursive", 14, "bold"), padx = 2)
        TableFrame.place(x = 435, y= 50, width = 615, height = 500)        

        lblSearch = Label(TableFrame, font = ("Recursive", 11, "bold"), text = "Search: ")
        lblSearch.grid(row = 0, column = 0, sticky = W, padx = 2)

        comboSearch = ttk.Combobox(TableFrame, font = ("Recursive", 11), width = 10, state = "readonly")
        comboSearch["value"] = ("Driving", "Passport", "National")
        comboSearch.current(0)
        comboSearch.grid(row = 0, column = 1, padx = 2)

        txtSearch = ttk.Entry(TableFrame, font = ("Recursive", 11), width = 24)
        txtSearch.grid(row = 0, column = 2, padx = 2)

        btnSearch = Button(TableFrame, text = "Search", font = ("Palatino Linotype", 9, "bold"), bg = "gray", fg = "white", width = 8)
        btnSearch.grid(row = 0, column = 3, padx = 1)

        btnSearch = Button(TableFrame, text = "Show All", font = ("Palatino Linotype", 9, "bold"), bg = "gray", fg = "white", width = 8)
        btnSearch.grid(row = 0, column = 4, padx = 1)

        #================ data table ============
        detailsTable = Frame(TableFrame, bd = 2, relief = RIDGE)
        detailsTable.place(x = 0, y = 50, width = 860, height = 350)

        scroll_x = ttk.Scrollbar(detailsTable, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailsTable, orient = VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(detailsTable, column = ("ref","name", "mother", "gender", "post", "mobile"
                                                "email", "nationality", "id", "idnumber", "address"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X)                                        
        scroll_y.pack(side = RIGHT, fill = Y)

       


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()