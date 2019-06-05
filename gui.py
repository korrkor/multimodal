import tkinter as tk                    
from tkinter import ttk
from Profile import Profile
from tkinter import messagebox

logged_in = ""
def login():
  profile = Profile(name = name.get(), pin=pin.get())
  record = profile.log_in()
  if(record):
    tabControl.select(1)
    user = record[1]
    logged_in = user
    lblhide.configure(text=user)
    lblName.configure(text="Hello "  + user, padx =20,pady=20,font=("Gudea", 15), anchor="w",justify="left")
  else:
    messagebox.showerror("Authentication Failed!", "Login Failed. Try again")
    clear_text([name, pin])

def activate_profile_screen(event): 
  tabControl.select(2)
  
def create_profile():
  profile = Profile(pname.get(), pemail.get(), ppin.get())
  if profile.create_profile():
    messagebox.showinfo("Title","Profile succesfuly created. Log in with name and pin")
    show_tab(0)
    hide_tab(2)
    clear_text([pname,pemail,ppin])

def clear_text(element_list):
  for v in element_list:
    v.delete(0,"end") 

def hide_tab(index):
  tabControl.hide(index)

def show_tab(index):
  tabControl.select(index)

def activate_monitor():
  profile = Profile()
  if (profile.activate_monitor(lblhide.cget("text"))  ):
    messagebox.showinfo("Success", "Monitor activated")
    show_tab(0)
    clear_text([name, pin])
  else:
    messagebox.showerror("Oops", "Something went wrong. Contact the support center")

# ****************************************gui start******************************
win = tk.Tk()                           
win.title("Python GUI") 
win.geometry('400x300')

tabControl = ttk.Notebook(win)          
tab_intro = ttk.Frame(tabControl)   
tab_intro.grid(column=5, row=3)         
tab_home= ttk.Frame(tabControl) 
tab_create_profile = ttk.Frame(tabControl) 
 
tabControl.add(tab_intro, text='Getting Started') 
tabControl.add(tab_home, state="hidden",text='Home')  
tabControl.add(tab_create_profile, state="hidden",text='Add new profile')  

lbl = tk.Label(tab_intro, text="Welcome to the app.", padx =20,pady=20,font=("Gudea", 15), anchor="w",justify="left")
lbl.pack()

#******************* sign in *************
namelbl = tk.Label(tab_intro, text = "Username", font=("Gudea", 10),anchor="w", wraplength = 550,)
name = tk.Entry(tab_intro)
namelbl.pack()
name.pack()
name.focus_set()

pinlbl = tk.Label(tab_intro, text = "Pin", font=("Gudea", 10),anchor="w", wraplength = 550)
pinlbl.pack()
pin = tk.Entry(tab_intro)  
pin.pack()

buttonLogIn = tk.Button(tab_intro,text="Log in",font=("Gudea", 12), anchor="e",command=login)
buttonLogIn.pack()
#******************* end sign in *************



#******************* homepage *************
lblhide = tk.Label(tab_home, text="dsd" , font=("Gudea", 12), anchor="e", justify="left")

lblName = tk.Label(tab_home, text="Hello" , font=("Gudea", 12), anchor="e", justify="left")
lblName.pack()

buttonAcivate = tk.Button(tab_home,text="Activate Monitor",font=("Gudea", 12), anchor="e",command=activate_monitor)
buttonAcivate.pack()

buttonTrain = tk.Button(tab_home,text="Add new face",font=("Gudea", 12), anchor="e",command=login)
buttonTrain.pack()

#******************* end homepage *************

#**************************** new user creation **************************************************
intolbl = tk.Label(tab_create_profile, text="Here you can create a profile to access the application", padx =20,pady=20,font=("Gudea", 15), anchor="w",justify="left")
intolbl.pack()

lblNewUser= tk.Label(tab_intro,pady=20,text="New user? Create profile!",cursor="mouse",font=("Gudea", 10))
lblNewUser.pack()
lblNewUser.bind('<Button>',activate_profile_screen) 

#**************************** form user creation **************************************************
pnamelbl = tk.Label(tab_create_profile, text = "Name", font=("Gudea", 10),anchor="w", wraplength = 550)
pname = tk.Entry(tab_create_profile)
pnamelbl.pack()
pname.pack()

pemaillbl = tk.Label(tab_create_profile, text = "Email", font=("Gudea", 10),anchor="w", wraplength = 550)
pemail = tk.Entry(tab_create_profile)
pemaillbl.pack()
pemail.pack()

# ppasswordlbl = tk.Label(tab_create_profile, text = "Email password", font=("Gudea", 10),anchor="w", wraplength = 550)
# ppassword = tk.Entry(tab_create_profile)
# ppasswordlbl.pack()
# ppassword.pack()

ppinlbl = tk.Label(tab_create_profile, text = "Pin", font=("Gudea", 10),anchor="w", wraplength = 550)
ppin = tk.Entry(tab_create_profile)
ppinlbl.pack()
ppin.pack()

buttonCreateProfile = tk.Button(tab_create_profile,text="Create my profile",font=("Gudea", 10), anchor="e",command=create_profile) 
buttonCreateProfile.pack()

#**************************** end form  user creation **************************************************

#**************************** ENd new user creation **************************************************


tabControl.pack(expand=1, fill='both') 
win.mainloop() 