'''
Projek Home Loan Calculator
Nama : Deric Ing Quan Chong (8)
Kelas : 3 RED
'''
from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from matplotlib import pyplot as plt
from time import*

# Fungsi info
def info():
    window.destroy()
    window2 = Tk()
    window2.title("User Manual of Home Loan Calculator")
    window2.geometry("890x630")
    window2.resizable(0, 0)
    
    canvas2 = Canvas(window2, width = 890, height = 630)
    canvas2.pack(fill = "both", expand=True)
    bg2 = PhotoImage(file='background_2.png')
    canvas2.create_image(0, 0, image=bg2, anchor = "nw")
    canvas2.create_text(440, 40, text="USER MANUAL OF HOME LOAN CALCULATOR",
                        font=("Algerian", 30, "bold"))
    canvas2.create_text(430, 110,
                        text="1. Enter your Property Asset Value in NUMBER or DECIMAL and "
                        "your loan \namount cannot be NEGATIVE value or ZERO !",
                        font=("Courier New", 15, "bold"), justify="left")   
    canvas2.create_text(415, 180, text="2. Enter your Down Payment value (Percentage) in NUMBER "
                        "or DECIMAL \nand it CANNOT LOWER THAN 0 !",
                        font=("Courier New", 15, "bold"), justify="left")
    canvas2.create_text(420, 250, text="3. Enter your Interest Rate (number / decimal) for this"
                       " loan and it \nCANNOT BE LOWER THAN 0 !",
                        font=("Courier New", 15, "bold"), justify="left")
    canvas2.create_text(330, 310, text="4. Enter your Period for this Loan in year (number) !",
                        font=("Courier New", 15, "bold"), justify="left")
    canvas2.create_text(373, 370, text="5. Statement of Monthly Instalment Payment is shown in"
                        " the \nScrolledtext .", font=("Courier New", 15, "bold"),
                        justify="left")
    canvas2.create_text(425, 440, text="6. Click the Pie Chart button and it will show you the "
                        "Percentage of \nTotal Principal & Total Interest of your loan .",
                        font=("Courier New", 15, "bold"), justify="left")
    canvas2.create_text(410, 510, text="7. Close the Pie Chart and click the Reset Button and "
                        "you can now \ncalculate your another loan .",
                        font=("Courier New", 15, "bold"), justify="left")
    canvas2.create_text(280, 570, text="8. Click Export button to export your text .",
                        font=("Courier New", 15, "bold"), justify="left")
    next_button = Button(window2, text="Proceed to Calculation", font=("Arial Black",13), fg='#FFCC00',
                           bg='#003399', width=20, command = start_2, justify='center')
    next_button_window = canvas2.create_window(720, 570, window = next_button)
    global w2
    w2 = window2
    window2.mainloop()

# Fungsi start_1
def start_1():
    window.destroy()
    start()

# Fungsi start_2
def start_2():
    w2.destroy()
    start()

# Fungsi start
def start():
    window3 = Tk()
    window3.title("Home Loan Calculator")
    window3.geometry("890x630")
    window3.resizable(0, 0)
    
    bg3 = PhotoImage(file='background2.png')
    canvas3 = Canvas(window3, width = 900, height = 630)
    canvas3.pack(fill = "both", expand=True)
    canvas3.create_image(0, 0, image=bg3, anchor = "nw")
    canvas3.create_text(720, 30, text="HOME LOAN", font=("Algerian", 38, "bold"),
                        fill="#285EC9")
    canvas3.create_text(130, 40, text="Loan Amount (RM)  : ", font=("Calibri", 18, "bold"),
                        fill="#0C6B6E")
    canvas3.create_text(130, 90, text="Down Payment (%)  : ", font=("Calibri", 18, "bold"),
                        fill="#0C6B6E")
    canvas3.create_text(130, 140, text="Interest Rate (%)      : ",
                        font=("Calibri", 18, "bold"), fill="#0C6B6E")
    canvas3.create_text(130, 190, text="Year                              : ",
                        font=("Calibri", 18, "bold"), fill="#0C6B6E")
    canvas3.create_text(163, 260, text="Monthly Repayment (RM) :",
                        font=("Calibri", 18, "bold"),fill="#0C6B6E")
    home = PhotoImage(file='home2.png')
    canvas3.create_image(725, 135, image = home)
        
    def variable_validation():
        loan_amount = l.get()
        try:
            float(loan_amount)
        except:
            messagebox.askretrycancel("Warning !",
                                      "Please Enter Your Property Asset value in number !")
            l_reset()
        else:
            if float(loan_amount) <= 0:
                messagebox.askretrycancel("Ivalid Input !",
                                          "Loan amount Cannot be NEGATIVE value or ZERO !")
                l_reset()

        dp = d.get()
        try:
            float(dp)
        except:
            messagebox.askretrycancel("Warning !",
                                      "Please Enter Your Down Payment in NUMBER or DECIMAL !")
            d_reset()
        else:
            if float(dp) < 0 or float(dp) >= 100:
                messagebox.askretrycancel("Invalid Input !",
                                          "Percentage of Down Payment have to MORE THAN 0 or"
                                          "NOT MORE THAN 99!")
                d_reset()

        int_rate = i.get()
        try:
            float(int_rate)
        except:
            messagebox.askretrycancel("Warning !",
                                      "Please Enter Your Interest Rate in NUMBER or DECIMAL !")
            i_reset()
        else:
            if float(int_rate) <= 0:
                messagebox.askretrycancel("Invalid Input !",
                                          "Percentage of Interest Rate have to MORE THAN 0 !")
                i_reset()

        year_time = y.get()
        try:
            int(year_time)
        except:
            messagebox.askretrycancel("Warning !", "Please Enter Period of Year in number !")
            y_reset()
        else:
            if int(year_time) <= 0:
                messagebox.askretrycancel("Invalid Input !",
                                          "Period of year have to MORE THAN 0 !")
                y_reset()
        repayment()
        
    l = StringVar()
    loan_entry = Entry(window3,font=("Arial", 20, "bold"), fg="#EAA51E", textvariable=l,
                       width=15, bd=3)
    loan_window = canvas3.create_window(250, 25, anchor="nw", window = loan_entry)

    d = StringVar()
    downpayment_entry = Entry(window3, font=("Arial", 20, "bold"), fg="#FD9D04",
                              textvariable=d, width=15, bd=3)
    downpayment_window = canvas3.create_window(250, 75, anchor="nw", window = downpayment_entry)

    i = StringVar()
    interest_entry = Entry(window3, font=("Arial", 20, "bold"), fg="#FD9D04", textvariable=i,
                           width=15, bd=3)
    interest_window = canvas3.create_window(250, 125, anchor="nw", window = interest_entry)

    y = StringVar()
    year_entry = Entry(window3, font=("Arial", 20, "bold"), fg="#FD9D04", textvariable=y,
                       width=15, bd=3)
    year_entry_window = canvas3.create_window(250, 175, anchor="nw", window = year_entry)

    text_area = scrolledtext.ScrolledText(window3, wrap=WORD, width=68, height=13,
                                      font=("Courier New", 13))
    textarea_window = canvas3.create_window(25, 310, anchor="nw", window = text_area)
    text_area.config(state='disabled')
    
    exit_pic = PhotoImage(file='exit2.png')
    exit_button = Button(window3, image = exit_pic, command = close, borderwidth=0)
    exit_button_window = canvas3.create_window(805, 355, window = exit_button)

    reset_pic = PhotoImage(file='reset2.png')
    reset_button = Button(window3, image = reset_pic, command = reset, borderwidth=0)
    reset_button_window = canvas3.create_window(765, 435, window = reset_button)

    cal_pic = PhotoImage(file='calculate2.png')
    cal_button = Button(window3, image=cal_pic, command = variable_validation, bd=0)
    cal_button_window = canvas3.create_window(842, 435, window = cal_button)

    pie_pic = PhotoImage(file='pie_chart2.png')
    pie_button = Button(window3, image = pie_pic, command = pie_chart, bd=0)
    pie_button_window = canvas3.create_window(802, 520, window = pie_button)
    pie_button.config(state='disabled')

    export_button = Button(window3, text="EXPORT", font=("Arial Black",13), fg='#FFCC00',
                           bg='#003399', width=7, command = export, justify='center')
    export_button_window = canvas3.create_window(71, 595, window = export_button)
    export_button.config(state='disabled')
    
    def time():
        time_string = strftime("%I : %M : %S %p")
        time_label.config(text = time_string, fg='white', bg='black')
    
        day_string = strftime("%a %e-%m-%Y")
        day_label.config(text = day_string)
    
        time_label.after(50,time)
    time_label = Label(window3, font=("Arial Black", 16, "bold"))
    time_label.place(x=625, y=215)

    day_label = Label(window3, font=("Arial Black", 16, "bold"))
    day_label.place(x=622, y=260)
    time()
    global l_v, d_v, i_v, y_v , text_a, calculate_b, reset_b, pie_b, ex_b, c3, w3
    l_v = l
    d_v = d
    i_v = i
    y_v =y
    text_a = text_area
    calculate_b = cal_button
    reset_b = reset_button
    pie_b = pie_button
    ex_b = export_button
    c3 = canvas3
    w3 = window3
    window3.mainloop()

# Fungsi repayment
def repayment():
    loan = float(l_v.get())
    down_payment = float(d_v.get())
    irate = float(i_v.get())
    year = int(y_v.get())
    month = year * 12
    interest = irate / 100 / 12
    m_r = 1 - ((interest + 1) ** -month)
    loan_ = loan * ((100 - down_payment) / 100)
    monthly_repayment = loan_ * interest / m_r
    
    monthr_window = c3.create_text(430, 263, text=format(monthly_repayment, ".2f"),
                                        font=("Arial", 20, "bold"), fill="#EAA51E")
    reset_b.config(state='disabled')
    A = "-------".ljust(8) + "-----------".rjust(17) + "---------------".rjust(22) +\
        "------------".rjust(18)
    B = "\nPERIOD".ljust(3) + "PRINCIPAL".rjust(17) + "INTEREST RATE".rjust(22) +\
        "BALANCE".rjust(16)
    C = "\n-------".ljust(8) + "-----------".rjust(17) + "---------------".rjust(22) +\
        "------------".rjust(18)
    text_a.config(state='normal')
    text_a.insert('insert', A)
    text_a.insert('insert', B)
    text_a.insert('insert', C)
    global lo, int_rate, m, monr, mlabel
    lo = loan_
    int_rate = interest
    m = month
    monr = monthly_repayment
    mlabel = monthr_window
    calculation()

# Fungsi calculation
def calculation():
    total_principal = 0.00
    total_interest = 0.00
    balance = lo
    total_period = 0
    while total_period < m:
        total_period = total_period + 1
        interest_rate = balance * int_rate
        principal = monr - interest_rate
        balance = balance - principal

        if balance < 0:
            balance = 0.00
        total_principal = total_principal + principal
        total_interest = total_interest + interest_rate
        D = "\n" + str(total_period).rjust(4) + str(format(principal, ".2f")).rjust(18) + str(
            format(interest_rate, ".2f")).rjust(20) + \
            str(format(balance, ".2f").rjust(20))
        text_a.insert('insert', D)
    E = "\n-------".ljust(10) + "-----------".rjust(15) + "---------------".rjust(22)
    F = "\nTOTAL".rjust(5) + str(format(total_principal, ".2f")).rjust(17) + \
        str(format(total_interest, ".2f")).rjust(20)
    text_a.insert('insert', E)
    text_a.insert('insert', F)
    text_a.insert('insert', E)
    calculate_b.config(state='disabled')
    text_a.config(state='disabled')
    ex_b.config(state='normal')
    data = [total_principal, total_interest]
    data_label = ["Principal", "Interest"]
    data_explode = [0.4, 0]
    colour = ['silver', '#E22222']
    plt.pie(data, labels=data_label, explode=data_explode, radius=1, autopct='%0.0f%%',
            shadow=True, colors=colour)
    plt.title("Percentage of Total Principal & Total Interest")
    plt.tight_layout()
    plt.legend(loc='lower right')
    pie_b.config(state='normal')
    global pl, pb
    pl = plt
    pb = pie_b

# Fungsi pie_chart
def pie_chart():
    pl.show()
    pb.config(state='disabled')
    reset_b.config(state='normal')

# Fungsi l_reset
def l_reset():
    l_v.set("")
# Fungsi d_reset
def d_reset():
    d_v.set("")
# Fungsi i_reset
def i_reset():
    i_v.set("")
# Fungsi y_reset
def y_reset():
    y_v.set("")

# Fungsi reset
def reset():
    l_v.set("")
    d_v.set("")
    i_v.set("")
    y_v.set("")
    c3.delete(mlabel)
    text_a.config(state='normal')
    text_a.delete('0.0', END)
    text_a.config(state='disabled')
    calculate_b.config(state='normal')
    ex_b.config(state='disabled')
    pb.config(state='disabled')
    data=[]

# Fungsi export
def export():
    filename = filedialog.asksaveasfilename(defaultextension = '.txt',
                                            filetypes = [("Text File", ".txt"),
                                                         ("HTML", ".html"),("All File", "*")])
    files = open(filename,"w")
    text = text_a.get('1.0', END)
    files.write(text)
    files.close
    
# Fungsi close
def close():
    w3.destroy()

window = Tk()
window.title("Main Menu of Home Loan Calculator")
window.geometry("890x630")
window.resizable(0, 0)
icon = PhotoImage(file='mortgage.png')
window.iconphoto(True,icon)

bg1 = PhotoImage(file='front_bg2.png')
canvas1 = Canvas(window, width = 900, height = 630)
canvas1.pack(fill = "both", expand=True)
canvas1.create_image(0, 0, image=bg1, anchor = "nw")

house_image = PhotoImage(file='house.png')
canvas1.create_image(220,165, image=house_image, anchor="nw")
canvas1.create_text(445, 110, text="HOME LOAN", font=("Algerian", 45, "bold"), fill="black")
canvas1.create_text(442, 170, text="CALCULATOR", font=("Algerian", 45, "bold"), fill="black")

info1 = Button(window, text = "Info", font=("Arial Black",15), fg='white', bg='#132A75',
                   width=7, command=info, justify='center')
canvas1.create_window(350, 510, window = info1)
start1 = Button(window, text = "Start", font=("Arial Black",15), fg='white', bg='#132A75',
                   width=7, command=start_1, justify='center')
canvas1.create_window(540, 510, window = start1)
data =[]

window.mainloop()