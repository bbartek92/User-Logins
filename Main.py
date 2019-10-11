import tkinter as tk
import json
import hashlib
import sqlite3

class MyApp():
    def __init__ (self):
        self.login_page = Loggin()


class Loggin():
    def __init__ (self):
        self.window = tk.Tk()
        self.window.title("System Log-in")
        self.window.geometry('300x150')
        #empty row
        tk.Label(self.window).grid(column=0, row=0)
        #set login part
        tk.Label(self.window, text="Login").grid(column=0, row=1, sticky='w')
        self.entry_login = tk.StringVar()
        tk.Entry(self.window, textvariable=self.entry_login).grid(column=1, row=1, sticky='w', columnspan=2)
        #set password part
        tk.Label(self.window, text="Password").grid(column=0, row=2, sticky='w')
        self.entry_password = tk.StringVar()
        tk.Entry(self.window, textvariable=self.entry_password).grid(column=1, row=2, sticky='w', columnspan=2)
        tk.Button(self.window, text="Log to the System", command = self.check_credential).grid(column=1, row=3, sticky='w')
        tk.Button(self.window, text="Create new account", command = self.new_account_req).grid(column=1, row=4, sticky='w')

    def check_credential(self):
        # window.delete(new_label)
        self.v=tk.StringVar()
        tk.Label(self.window, textvariable=self.v, fg='red').grid(column=1, row=6, sticky='w')
        #get hash
        log_hash = hashlib.sha256(self.entry_login.get().encode('utf-8')).hexdigest()
        pass_hash = hashlib.sha256(self.entry_password.get().encode('utf-8')).hexdigest()
        #connection to JSON data
        # log_check = self.json_check(log_hash, pass_hash)
        #connection to SQLite
        log_check = self.database_check(log_hash, pass_hash)
        if log_check==0:
            self.v.set('Connection problem')

        elif log_check==1:
            self.window.destroy()
            Online()
        else:
            self.v.set('Your Login or Password is not correct')

    def database_check(self, login, password):
        #connect to database
        data_path = 'database_hash.db'
        try:
            with open(data_path) as database:
                conn = sqlite3.connect(data_path)
        except IOError:
            return 0
        #check if login and passowrd are in the database
        c = conn.cursor()
        credencial1 = login
        credencial2 = password
        c.execute("select count(*) from users where username_hash=? and password_hash=?", (credencial1, credencial2))
        if c.fetchall()[0][0]==1:
            return 1
        else:
            return 2


    def json_check(self, login, password):
        #load data from file, create dictionary if there is no data
        json_path = 'data_hash.txt'
        try:
            with open(json_path) as json_cache:
                data = json.load(json_cache)
        except IOError:
                return 0
        #check if login and passowrd are in the data
        if login in data:
            if password == data[login]:
                return 1
            else:
                return 2
        else:
            return 2

    def new_account_req (self):
        NewAccount() 


class Online():
    def __init__ (self):
        self.online = tk.Tk()
        self.online.title("Super App")
        self.online.geometry('700x700')
        tk.Canvas(self.online, bg='black', height = 700, width = 700).pack()


class NewAccount():
    def __init__ (self):
        self.new_account_page = tk.Tk()
        self.new_account_page.title("New Account request")
        self.new_account_page.geometry('700x700')  
        self.frame1 = tk.Frame(self.new_account_page, height = 100, width=700, bg='azure3')
        self.frame1.pack(side='top')
        self.frame2 = tk.Frame(self.new_account_page, height = 700, width=100, bg='lime green')
        self.frame2.pack(side='left')
        self.frame3 = tk.Frame(self.new_account_page, height = 700, width=600, bg='SteelBlue1')
        self.frame3.pack(side='left')

if __name__ == "__main__":
    my_app = MyApp()
    my_app.login_page.window.mainloop()