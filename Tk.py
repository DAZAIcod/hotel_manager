import tkinter as tk
from funks import *
from tkinter import messagebox, ttk, colorchooser


def center_window(width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')


class WelcomeWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Welcome")
        center_window(280, 150)

        login_button = tk.Button(self, text="Login", width=10,
                                 command=self.open_login_window)
        login_button.pack(padx=20, pady=(20, 10))

        register_button = tk.Button(self, text="Register", width=10,
                                    command=self.open_register_window)
        register_button.pack(pady=10)
        self.pack()

    def open_login_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        LoginWindow(self.master)

    def open_register_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        RegisterWindow(self.master)


class LoginWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Login")
        self.master.resizable(True, True)
        center_window(350, 150)

        tk.Label(self, text="Email:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        submit_button = tk.Button(self, text="Submit", width=8, command=self.submit)
        submit_button.grid(row=2, column=1, sticky="w", padx=10, pady=(10, 0))

        submit_button = tk.Button(self, text="Back", width=8, command=self.back)
        submit_button.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))
        self.pack()

    def submit(self):
        data = {}
        data["email"] = self.username_entry.get()
        data["password"] = self.password_entry.get()

        if login(data) == True:
            messagebox.showinfo(title='success' ,message='successful login')
            for widget in self.winfo_children():
                widget.destroy()
            self.destroy()
            MainWindow(self.master)
        elif login(data) == 'master':
            messagebox.showinfo(title='welcome', message='hy master')
            for widget in self.winfo_children():
                widget.destroy()
            self.destroy()
            MasterWindow(self.master)

    def back(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)


class RegisterWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Register")
        self.master.resizable(True, True)
        center_window(380, 350)

        tk.Label(self, text="First Name:").grid(row=0, column=0, sticky="w")
        self.first_name_entry = tk.Entry(self, width=26)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="Last Name:").grid(row=1, column=0, sticky="w")
        self.last_name_entry = tk.Entry(self, width=26)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="Email:").grid(row=2, column=0, sticky="w")
        self.email_entry = tk.Entry(self, width=26)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="Phone number:").grid(row=3, column=0, sticky="w")
        self.phone_entry = tk.Entry(self, width=26)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="Password :").grid(row=4, column=0, sticky="w")
        self.password1_entry = tk.Entry(self, show="*", width=26)
        self.password1_entry.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="sub Password :").grid(row=5, column=0, sticky="w")
        self.password2_entry = tk.Entry(self, show="*", width=26)
        self.password2_entry.grid(row=5, column=1, padx=10, pady=10, sticky="e")

        submit_button = tk.Button(self, text="Submit", width=8, command=self.submit)
        submit_button.grid(row=7, column=1, padx=10, pady=10, sticky="e")

        submit_button = tk.Button(self, text="Back", width=8, command=self.back)
        submit_button.grid(row=7, column=0, sticky="w", padx=10, pady=(10, 10))
        self.pack()

    def submit(self):
        data = {}
        data['fname'] = self.first_name_entry.get()
        data['lname'] = self.last_name_entry.get()
        data['email'] = self.email_entry.get()
        data['phone_number'] = self.phone_entry.get()
        if check_email_phone(data['email'], data['phone_number']):
            messagebox.showwarning(title='warning', message='this email or phone number is already exists')
            return self.open_register_window()
        password = self.password1_entry.get()
        password2 = self.password2_entry.get()
        if password2 != password :
            messagebox.showerror(title="error", message='passwords  not  matched!')
            return self.open_register_window()
        data['password'] = password
        add_new_guest(data)
        messagebox.showinfo(title='success', message='one guest created')
        self.back()

    def back(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)

    def open_register_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        RegisterWindow(self.master)


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        center_window(600, 400)
        self.pack()


class MasterWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        center_window(1000, 500)

        my_menu = tk.Menu(self.master)
        self.master.config(menu=my_menu)

        option_menu = tk.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Options", menu=option_menu)

        option_menu.add_command(label='primary color', command=self.primary_color_chooser)
        option_menu.add_command(label='secondary color', command=self.secondary_color_chooser)
        option_menu.add_command(label='highlite color', command=self.highlight_color_chooser)
        option_menu.add_separator()
        option_menu.add_command(label='reset', command=self.reset_colors)
        option_menu.add_separator()
        option_menu.add_command(label='exit', command=self.quit)



        self.pack()
        global style
        style = ttk.Style()
        style.theme_use('default')
        style.configure(style="Treeview",
                        background='#D3D3D3',
                        foreground='black',
                        rowheight=25,
                        fieldbackground='D3D3D3')
        #"#347083"
        style.map('Treeview',
                  background=[('selected', saved_highlight_color)])
        self.tree_frame = tk.Frame(self.master)
        self.tree_frame.pack(pady=10)
        self.tree_scroll = tk.Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side='right', fill='y')
        self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set, selectmode="extended")
        self.tree.pack()
        self.tree_scroll.config(command=self.tree.yview)
        self.tree['columns'] = ('ID', 'First Name', 'Last Name', 'Email', 'Phone Number', 'Password')
        self.tree.column("#0", width=0, stretch='NO')
        self.tree.column("ID", anchor='center', width=30)
        self.tree.column("First Name", anchor='w', width=140)
        self.tree.column("Last Name", anchor='w', width=140)
        self.tree.column("Email", anchor='center', width=140)
        self.tree.column("Phone Number", anchor='center', width=140)
        self.tree.column("Password", anchor='center', width=140)

        self.tree.heading("#0", text='', anchor='center')
        self.tree.heading("ID", text='ID', anchor='center')
        self.tree.heading("First Name", text='First Name', anchor='w')
        self.tree.heading("Last Name", text='Last Name', anchor='w')
        self.tree.heading("Email", text='Email', anchor='center')
        self.tree.heading('Phone Number', text='Phone Number', anchor='center')
        self.tree.heading("Password", text='Password', anchor='center')

        self.data_frame = tk.LabelFrame(master, text='Record')
        self.data_frame.pack(fill='x', expand="yes", padx=20)

        tk.Label(self.data_frame, text="First Name:").grid(row=0, column=0, padx=10, pady=10)
        self.first_name_entry = tk.Entry(self.data_frame)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.data_frame, text="Last Name:").grid(row=0, column=2, padx=10, pady=10)
        self.last_name_entry = tk.Entry(self.data_frame)
        self.last_name_entry.grid(row=0, column=3, padx=10, pady=10)

        tk.Label(self.data_frame, text="Email:").grid(row=0, column=4, padx=10, pady=10)
        self.email_entry = tk.Entry(self.data_frame)
        self.email_entry.grid(row=0, column=5, padx=10, pady=10)

        tk.Label(self.data_frame, text="Phone number:").grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(self.data_frame)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.data_frame, text="Password :").grid(row=1, column=2, padx=10, pady=10)
        self.password1_entry = tk.Entry(self.data_frame)
        self.password1_entry.grid(row=1, column=3, padx=10, pady=10)

        self.button_frame = tk.LabelFrame(master, text='Commands')
        self.button_frame.pack(fill='x', expand='yes', padx=20)

        submit_button = tk.Button(self.button_frame, text="Add Guest", width=8, command=self.add_guest)
        submit_button.grid(row=0, column=0, padx=10, pady=10)

        submit_button = tk.Button(self.button_frame, text="Clear", width=8, command=self.clear)
        submit_button.grid(row=0, column=1, padx=10, pady=10)

        submit_button = tk.Button(self.button_frame, text="Remove", width=8, command=self.remove_one)
        submit_button.grid(row=0, column=2, padx=10, pady=10)

        submit_button = tk.Button(self.button_frame, text="Remove many", width=10, command=self.remove_many)
        submit_button.grid(row=0, column=3, padx=10, pady=10)

        submit_button = tk.Button(self.button_frame, text="Update", width=10, command=self.update_button)
        submit_button.grid(row=0, column=4, padx=10, pady=10)

        submit_button = tk.Button(self.button_frame, text="search", width=10, command=self.search_guest_by_all)
        submit_button.grid(row=0, column=5, padx=10, pady=10)

        self.tree.bind("<ButtonRelease-1>", self.select)
        self.tree.tag_configure('oddrow', background=saved_primary_color)
        self.tree.tag_configure('evenrow', background=saved_secondary_color)
        self.insert_guest(all_guest())

    def primary_color_chooser(self):
        primary_color = colorchooser.askcolor()[1]
        if primary_color:
            self.tree.tag_configure('evenrow', background=primary_color)
            parser = ConfigParser()
            parser.read('treebase.ini')
            parser.set('colors', 'primary_color', primary_color)
            with open ('treebase.ini', 'w') as configfile:
                parser.write(configfile)

    def secondary_color_chooser(self):
        secondary_color = colorchooser.askcolor()[1]
        if secondary_color:
            self.tree.tag_configure('oddrow', background=secondary_color)
            parser = ConfigParser()
            parser.read('treebase.ini')
            parser.set('colors', 'secondary_color', secondary_color)
            with open ('treebase.ini', 'w') as configfile:
                parser.write(configfile)

    def highlight_color_chooser(self):
        highlight_color = colorchooser.askcolor()[1]
        if highlight_color:
            style.map('Treeview',
                       background=[('selected', highlight_color)])
            parser = ConfigParser()                                 
            parser.read('treebase.ini')
            parser.set('colors', 'highlight_color', highlight_color)
            with open ('treebase.ini', 'w') as configfile:
                parser.write(configfile)

    def reset_colors(self):
        parser = ConfigParser()
        parser.read('treebase.ini')
        parser.set('colors', 'primary_color', 'lightblue')
        parser.set('colors', 'secondary_color', 'white')
        parser.set('colors', 'highlight_color', '#347083')
        with open ('treebase.ini', 'w') as configfile:
            parser.write(configfile)
        self.tree.tag_configure('oddrow', background='lightblue')
        self.tree.tag_configure('evenrow', background='white')
        style.map('Treeview',
                   background=[('selected', '#347083')])
    def search_guest_by_all(self):
        if self.check_entry():
            data = self.gather()
            self.clear_tree()
            self.insert_guest(search_guest(data))
        else:
            self.clear_tree()
            self.insert_guest(all_guest())

    def insert_guest(self, records):
        global count
        count = 0
        for item in records:
            if count % 2 == 0:
                self.tree.insert(parent='', index='end', iid=count, text='',
                                 values=(item[0], item[1], item[2], item[3], item[4], item[5]), tags=('evenrow',))
            else:
                self.tree.insert(parent='', index='end', iid=count, text='',
                                 values=(item[0], item[1], item[2], item[3], item[4], item[5]), tags=('oddrow',))
            count += 1

    def update_button(self):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            data = self.gather()
            data['id'] = int(values[0])
            update_guest(data)
            self.clear_tree()
            self.insert_guest(all_guest())
            self.clear()

    def add_guest(self):
        if self.first_name_entry.get():
            data = self.gather()
            add_new_guest(data)
            self.clear_tree()
            self.insert_guest(all_guest())

            self.clear()

    def select(self, e):

        self.clear()

        selected = self.tree.focus()

        values = self.tree.item(selected, 'values')
        self.first_name_entry.insert(0, values[1])
        self.last_name_entry.insert(0, values[2])
        self.email_entry.insert(0, values[3])
        self.phone_entry.insert(0, values[4])
        self.password1_entry.insert(0, values[5])

    def clear(self):
        self.first_name_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.password1_entry.delete(0, 'end')

    def gather(self):
        data = {}
        data['fname'] = self.first_name_entry.get()
        data['lname'] = self.last_name_entry.get()
        data['email'] = self.email_entry.get()
        data['phone'] = self.phone_entry.get()
        data['password'] = self.password1_entry.get()
        data['id'] = None
        return data

    def check_entry(self):
        if self.first_name_entry.get() or self.last_name_entry.get() or self.email_entry.get() or self.phone_entry.get() or self.password1_entry.get():
            return True

    def remove_one(self):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            delete_guest(int(values[0]))
            self.clear_tree()
            self.insert_guest(all_guest())
            self.clear()

    def remove_many(self):
        items = self.tree.selection()
        for item in items:
            values = self.tree.item(item, 'values')
            delete_guest(int(values[0]))
        self.clear_tree()
        self.insert_guest(all_guest())
        self.clear()

    def clear_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


root = tk.Tk()
root.eval('tk::PlaceWindow . center')
WelcomeWindow(root)
root.mainloop()
