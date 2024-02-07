import tkinter
import string
from tkinter import ttk,messagebox
import sqlite3
class Form(tkinter.Tk):
    def __init__(self , so_st , cy , tw_te , tw_es , tw_al , tw_fa):
        tkinter.Tk.__init__(self)
        self.title("Personal Informational")
        self.width_monitor = self.winfo_screenwidth()
        self.height_monitor = self.winfo_screenheight() 
        self.geometry(f"500x700+{int((self.width_monitor/2)-250)}+{int((self.height_monitor/2)-350)}")
        self.resizable(False,False)
        self.gender_value = tkinter.IntVar()
        self.soldier_value = tkinter.StringVar()
        self.soldier_status = so_st
        self.city_value = tkinter.StringVar()
        self.city = cy
        self.town_value = tkinter.StringVar()
        self.town_tehr = tw_te
        self.town_esf = tw_es
        self.town_alb = tw_al
        self.town_far = tw_fa
        self.phone_value = tkinter.IntVar()
        self.mobile_value = tkinter.IntVar()
        self.email_value = tkinter.IntVar()
        ##///////////////////##
        self.input = None
        self.gender_save = None
        self.status_save = None
        self.city_save = None
        self.town_save = None
        self.counter_connections = 0
        self.warning_message = []
        self.characters = string.ascii_letters + " "
        self.numbers = string.digits + "."
        self.email_characters = string.ascii_letters + string.digits + "@._-"

    def create_elements(self):
        self.label_id = tkinter.Label(self,text="ID:",font=("Arial",18))
        self.label_fname = tkinter.Label(self,text="First Name:",font=("Arial",18))
        self.label_lname = tkinter.Label(self,text="Last Name:",font=("Arial",18))
        self.label_age = tkinter.Label(self,text="Age:",font=("Arial",18))
        self.label_height = tkinter.Label(self,text="Height(m):",font=("Arial",18))
        self.label_weight = tkinter.Label(self,text="Weight(kg):",font=("Arial",18))
        self.label_BMI = tkinter.Label(self,text="BMI:",font=("Arial",18))
        self.label_gender = tkinter.Label(self,text="Gender:",font=("Arial",18))
        self.label_soldier = tkinter.Label(self,text="Soldier Status:",font=("Arial",18))
        self.label_city = tkinter.Label(self,text="City:",font=("Arial",18))
        self.label_town = tkinter.Label(self,text="Town:",font=("Arial",18))
        self.label_connections = tkinter.Label(self,text="Connections:",font=("Arial",18))
        self.label_phnumber = tkinter.Label(self,text="Phone Number:",font=("Arial",18))
        self.label_monumber = tkinter.Label(self,text="Mobile Number:",font=("Arial",18))
        self.label_email = tkinter.Label(self,text="Email Address:",font=("Arial",18))
        #################
        #1
        self.box_ID = tkinter.Entry(self,width=24,font=("Arial",18),bg="#e8ebe9")
        self.box_fname = tkinter.Entry(self,width=24,font=("Arial",18),bg="#e8ebe9")
        self.box_lname = tkinter.Entry(self,width=24,font=("Arial",18),bg="#e8ebe9")
        self.box_age = tkinter.Entry(self,width=24,font=("Arial",18),bg="#e8ebe9")
        self.box_height = tkinter.Entry(self,width=24,font=("Arial",18),bg="#e8ebe9")
        self.box_weight = tkinter.Entry(self,width=24,font=("Arial",18),bg="#e8ebe9")
        #2
        self.box_BMI = tkinter.Entry(self,width=24,font=("Arial",18),bg="#e8ebe9",state="disable")
        #
        self.rbgender1 = tkinter.Radiobutton(self,text="Male",font=("Arial",14), variable=self.gender_value , value=1, command=self.soldieropcl_saveitem) 
        self.rbgender2 = tkinter.Radiobutton(self,text="Female",font=("Arial",14), variable=self.gender_value , value=2, command=self.soldieropcl_saveitem) 
        self.rbgender3 = tkinter.Radiobutton(self,text="Other",font=("Arial",14), variable=self.gender_value , value=3, command=self.soldieropcl_saveitem) 
        #2
        self.dropdown_soldier = ttk.Combobox(self,width=27,font=("Arial",14),state="disable",textvariable=self.soldier_value , values=self.soldier_status)
        self.dropdown_soldier.bind("<<ComboboxSelected>>",self.soldier_save)
        #
        self.dropdown_city = ttk.Combobox(self,width=27,font=("Arial",14),state="readonly",textvariable=self.city_value , values=self.city)
        self.dropdown_city.bind("<<ComboboxSelected>>",self.save_determinationTown)
        #2
        self.dropdown_town = ttk.Combobox(self,width=27,font=("Arial",14),state="disable",textvariable=self.town_value , values=[])
        self.dropdown_town.bind("<<ComboboxSelected>>",self.towns_save)
        #
        self.phone_button = tkinter.Checkbutton(self,text="Phone",font=("Arial",14),variable=self.phone_value,offvalue=0,onvalue=1,command=self.open_box_text)
        self.mobile_button = tkinter.Checkbutton(self,text="Mobile",font=("Arial",14),variable=self.mobile_value,offvalue=0,onvalue=1,command=self.open_box_text)
        self.email_button = tkinter.Checkbutton(self,text="Email",font=("Arial",14),variable=self.email_value,offvalue=0,onvalue=1,command=self.open_box_text)
        #2
        self.box_phone = tkinter.Entry(self,width=24,font=("Arial",18),bg="#e8ebe9",state="disable")
        self.box_mobile = tkinter.Entry(self,width=24,font=("Arial",18),bg="#e8ebe9",state="disable")
        self.box_email = tkinter.Entry(self,width=24,font=("Arial",18),bg="#e8ebe9",state="disable")
        #
        self.authenticate_button = tkinter.Button(self,text="Authenticate",font=("Arial",11,"bold"),width=14,height=2,borderwidth=3,bg="#878584",activebackground="#e8ebe9",command=self.check_items)
        self.save_button = tkinter.Button(self,text="Save",font=("Arial",11,"bold"),width=14,height=2,borderwidth=3,bg="#878584",activebackground="#e8ebe9",state="disable",command=self.save_dataBase)
        self.clear_button = tkinter.Button(self,text="Clear",font=("Arial",11,"bold"),width=14,height=2,borderwidth=3,bg="#878584",activebackground="#e8ebe9", command=self.clear_item)
        self.elements_group1 = [self.box_ID,self.box_fname,self.box_lname,self.box_age,self.box_height,self.box_weight]
        self.elements_group2 = [self.box_BMI,self.dropdown_soldier,self.dropdown_town,self.box_phone,self.box_mobile,self.box_email]
    def locate_elements(self):
        self.label_id.grid(row=0,column=0,sticky="w",pady=5)
        self.label_fname.grid(row=1,column=0,sticky="w",pady=5)
        self.label_lname.grid(row=2,column=0,sticky="w",pady=5) 
        self.label_age.grid(row=3,column=0,sticky="w",pady=5)  
        self.label_height.grid(row=4,column=0,sticky="w",pady=5) 
        self.label_weight.grid(row=5,column=0,sticky="w",pady=5) 
        self.label_BMI.grid(row=6,column=0,sticky="w",pady=5)  
        self.label_gender.grid(row=7,column=0,sticky="w",pady=5)
        self.label_soldier.grid(row=8,column=0,sticky="w",pady=5)
        self.label_city.grid(row=9,column=0,sticky="w",pady=5)
        self.label_town.grid(row=10,column=0,sticky="w",pady=5)
        self.label_connections.grid(row=11,column=0,sticky="w",pady=5) 
        self.label_phnumber.grid(row=12,column=0,sticky="w",pady=5) 
        self.label_monumber.grid(row=13,column=0,sticky="w",pady=5)
        self.label_email.grid(row=14,column=0,sticky="w",pady=5)
        #############
        self.box_ID.grid(row=0,column=1)
        self.box_fname.grid(row=1,column=1)
        self.box_lname.grid(row=2,column=1) 
        self.box_age.grid(row=3,column=1) 
        self.box_height.grid(row=4,column=1) 
        self.box_weight.grid(row=5,column=1) 
        self.box_BMI.grid(row=6,column=1)
        self.rbgender1.place(x=180,y=304) 
        self.rbgender2.place(x=260,y=304)  
        self.rbgender3.place(x=360,y=304)
        self.dropdown_soldier.grid(row=8,column=1) 
        self.dropdown_city.grid(row=9,column=1) 
        self.dropdown_town.grid(row=10,column=1)
        self.phone_button.place(x=180,y=480) 
        self.mobile_button.place(x=280,y=480)
        self.email_button.place(x=380,y=480)
        self.box_phone.grid(row=12,column=1)
        self.box_mobile.grid(row=13,column=1)
        self.box_email.grid(row=14,column=1)
        self.authenticate_button.grid(row=15,column=0,padx=6)
        self.save_button.grid(row=15,column=1,padx=6,sticky="w")
        self.clear_button.place(x=350,y=645)
    #Authenticate command:
    def check_items(self):
        self.input = self.box_ID.get()
        if len(self.input) != 10 or not self.input.isnumeric():
            self.warning_message.append("The number of (ID) characters  is not allowed or the type of characters  is not allowed.\n")    
        ##
        self.input = self.box_fname.get()
        if len(self.input) < 3 or self.correct_alpha():
            self.warning_message.append("The number of (first name) characters is not allowed or the type of characters is not allowed.\n")
        ##
        self.input = self.box_lname.get()
        if len(self.input) < 3 or self.correct_alpha():
            self.warning_message.append("The number of (last name) characters is not allowed or the type of characters is not allowed.\n")
        ##
        self.input = self.box_age.get()
        if len(self.input) < 1  or not self.input.isnumeric():
            self.warning_message.append("The number of (age) characters  is not allowed or the type of characters  is not allowed.\n")
        elif int(self.input) < 1 or int(self.input) > 120:
            self.warning_message.append("(Age) range is not allowed.\n")
        ##
        self.input = self.box_height.get()
        self.dot_count = self.input.count(".")
        if len(self.input) < 1  or self.correct_number() or self.input.startswith(".") or self.input.endswith(".") or self.dot_count > 1:
            self.warning_message.append("The number of (height) characters is not allowed or the type of characters is not allowed.\n")
        elif float(self.input) < 0.4  or float(self.input) > 2.5:
            self.warning_message.append("(height) range is not allowed.\n")
        ##
        self.input = self.box_weight.get()
        self.dot_count = self.input.count(".")
        if len(self.input) < 1  or self.correct_number() or self.input.startswith(".") or self.input.endswith(".") or self.dot_count > 1:
            self.warning_message.append("The number of (weight) characters is not allowed or the type of characters is not allowed.\n")
        elif float(self.input) < 1  or float(self.input) > 220:
            self.warning_message.append("(weight) range is not allowed.\n")      
        ##  
        if self.gender_save == None:
            self.warning_message.append("Determine the amount of (gender).\n")
        ##
        if self.gender_save == "Male":
            if self.status_save == None:
                self.warning_message.append("Determine the (soldier status).\n") 
        ##
        if self.city_save == None:
            self.warning_message.append("Determine the name of the (city).\n")
        ##
        if self.city_save != None:
            if self.town_save == None:
                self.warning_message.append("Determine the name of the (town).\n")
        ##
        self.input = self.box_phone.get()
        self.counter_connections = 0
        if len(self.input) < 1:
            self.counter_connections += 1
        elif not self.input.startswith("0"):
            self.warning_message.append("The (phone) number must start with zero")
        elif len(self.input) != 11 or not self.input.isnumeric() or self.input.startswith("00"):
            self.warning_message.append("The number of (phone) characters  is not allowed or the type of characters  is not allowed.\n")
        ##
        self.input = self.box_mobile.get()
        if len(self.input) < 1:
            self.counter_connections += 1
        elif not self.input.startswith("0"):
            self.warning_message.append("The (mobile) number must start with zero\n")            
        elif len(self.input) != 11 or not self.input.isnumeric() or self.input.startswith("00"):
            self.warning_message.append("The number of (mobile) characters  is not allowed or the type of characters  is not allowed.\n")
        ##
        self.input = self.box_email.get()
        self.at_sign_count = self.input.count("@")
        self.dot_count = self.input.count(".")
        self.dot_count_inARow = self.input.count("..")
        self.underline_inARow = self.input.count("__")
        self.dash_inARow = self.input.count("--")
        if len(self.input) < 1:
            self.counter_connections += 1
        elif len(self.input) < 8 or self.correct_email() or self.at_sign_count != 1 or self.dot_count < 1 or self.dot_count_inARow > 0 or self.underline_inARow > 0 or self.dash_inARow > 0 or self.input.startswith("@") or self.input.startswith(".") or self.input.endswith("@") or self.input.endswith("."):
            self.warning_message.append("The number of (email) characters is not allowed or the type of characters is not allowed.\n")
        ##
        if self.counter_connections > 1:
            self.warning_message.append("Determine at least two (connections).\n")


        #show warning:
        self.warning = "\n".join(self.warning_message)
        self.warning_message = []
        if len(self.warning) > 0:
            messagebox.showwarning("warning!",self.warning)
        ##show BMI:
        else:
            self.box_BMI.config(state="normal")
            self.box_BMI.delete(0,tkinter.END)
            self.box_BMI.insert(tkinter.END , self.bmi_Computing())
            self.box_BMI.config(state="readonly") 
            
        ##active save button & disable other buttons:
            self.save_button.config(state="normal")   
            self.authenticate_button.config(state="disable")
            self.clear_button.config(state="disable")


    ##clear command:
    def clear_item(self):
        self.phone_button.deselect()
        self.mobile_button.deselect()
        self.email_button.deselect()
        self.dropdown_city.config(state="normal")
        self.dropdown_city.delete(0,tkinter.END)
        self.dropdown_city.config(state="readonly")
        self.gender_value.set(0) 


        for element in self.elements_group1:
            element.delete(0,tkinter.END)

        for element in self.elements_group2:
            element.config(state="normal")
            element.delete(0,tkinter.END)
            element.config(state="disable")
        
        self.gender_save = None
        self.status_save = None
        self.city_save = None  
        self.town_save = None 


    ##save command:
    def save_dataBase(self):
        self.my_connector = sqlite3.connect("Form.db")
        self.my_cursor = self.my_connector.cursor()
        try:
            self.my_cursor.execute("CREATE TABLE IF NOT EXISTS personal_information(ID TEXT UNIQUE,First_name TEXT,last_name TEXT,Age INTEGER,Height REAL,Weight REAL,BMI REAL,Gender TEXT,Soldier_status TEXT,City TEXT,Town TEXT,Phone_number TEXT,Mobile_number TEXT,Email_address TEXT)")
            self.my_cursor.execute(f"INSERT INTO personal_information VALUES('{self.box_ID.get()}','{self.box_fname.get()}','{self.box_lname.get()}',{int(self.box_age.get())},{float(self.box_height.get())},{float(self.box_weight.get())},{float(self.box_BMI.get())},'{self.gender_save}','{self.status_save}','{self.city_save}','{self.town_save}','{self.box_phone.get()}','{self.box_mobile.get()}','{self.box_email.get()}')")
        except sqlite3.IntegrityError:
            messagebox.showwarning("warning!","The ID value is duplicated.")
            self.box_ID.delete(0,tkinter.END)
            self.save_button.config(state="disable")   
            self.authenticate_button.config(state="normal")
            self.clear_button.config(state="normal")

        else:
            self.save_button.config(state="disable")
            self.authenticate_button.config(state="normal")
            self.clear_button.config(state="normal")
            self.clear_item()
            
        self.my_connector.commit()
        self.my_connector.close()


    ##save gender & op_cl dropdown status soldier
    def soldieropcl_saveitem(self):
        if self.gender_value.get() == 1:
            self.dropdown_soldier.config(state="readonly")
            self.gender_save = "Male"
        else:
            self.dropdown_soldier.config(state="normal")
            self.dropdown_soldier.delete(0,tkinter.END)
            self.dropdown_soldier.config(state="disable")
            self.status_save = None
            if self.gender_value.get() ==2:
                self.gender_save = "Female"
            else:
                self.gender_save = "Other" 
    #######
    def soldier_save(self,save):
        self.status_save = self.soldier_value.get()
    
    ##save city & Determine the town
    def save_determinationTown(self,save):
        self.city_save = self.city_value.get()
        self.dropdown_town.config(state="normal")

        if self.city_save == self.city[0]:
            self.dropdown_town.delete(0,tkinter.END)
            self.dropdown_town.config(values=self.town_tehr)
        elif self.city_save == self.city[1]:
            self.dropdown_town.delete(0,tkinter.END)
            self.dropdown_town.config(values=self.town_esf)
        elif self.city_save == self.city[2]:
            self.dropdown_town.delete(0,tkinter.END)
            self.dropdown_town.config(values=self.town_alb)
        else:
            self.dropdown_town.delete(0,tkinter.END)
            self.dropdown_town.config(values=self.town_far)

        self.dropdown_town.config(state="readonly")
        
    #####
    def towns_save(self,save):
        self.town_save = self.town_value.get()

    ##### op cl connections box:
    def open_box_text(self):
        if self.phone_value.get() == 1:
            self.box_phone.config(state="normal")
        else:
            self.box_phone.delete(0,tkinter.END)
            self.box_phone.config(state="readonly")
        if self.mobile_value.get() == 1:
            self.box_mobile.config(state="normal")
        else:
            self.box_mobile.delete(0,tkinter.END)
            self.box_mobile.config(state="readonly")
        if self.email_value.get() == 1:
            self.box_email.config(state="normal")
        else:
            self.box_email.delete(0,tkinter.END)
            self.box_email.config(state="readonly")        


#//////////////////////////////////////////#
    def correct_alpha(self):
        for character in self.input:
            if character not in self.characters:
                return True
    
    def correct_number(self):
        for character in self.input:
            if character not in self.numbers:
                return True

    def correct_email(self):
        for character in self.input:
            if character not in self.email_characters:
                return True

    def bmi_Computing(self):
        self.bmi =float( self.box_weight.get())/(float(self.box_height.get())**2)
        return round(self.bmi,2)
    




    

      
soldier_status = ["medical Exemption","Exemption from sponsorship","education pardon","Exemption of help seekers"]
city = ["Tehran","Esfahan","Alborz","Fars"]
town_tehr = ["Tehran","Pardis","Ray","Varamin"]
town_esf = ["Esfahan","Naiin","Natanz","Shahin shahr"]
town_alb = ["Karaj","Taleghan","Hashtgerd","Nazar abad"]
town_Far = ["Shiraz","Marvdasht","Firoz abad","Darab"]
main_form = Form(soldier_status, city ,town_tehr , town_esf , town_alb , town_Far)
main_form.create_elements()
main_form.locate_elements()
main_form.mainloop()


    