from Tkinter import *
import datetime
import calendar
import tkMessageBox

root = Tk()
root.wm_title("Follow Up period for a clinical trial") #title of program
root.geometry("420x150") #size of root (canvas)

#creating End date of RT entry box
end_date_rt = Entry(root)
end_date_rt.insert(0, "01-01-2018")
end_date_rt.grid(row=1, column=1, pady=4)

#creating End date of RT label
end_date_rt_lb = Label(root, text="End date of RT")
end_date_rt_lb.grid(row=1, column=0, pady=4)

#creating Year box
year = StringVar(root)
year.set("2")

#creating Year Options
year_options = OptionMenu(root, year , "2", "3", "4", "5", "6")
year_options.grid(row = 2, column = 1)

#creating Year label
year_label = Label(root, text = "Year")
year_label.grid(row = 2, column = 0)

#Creating output (beginning date) label
output = Label(root, text = 'Follow up Duration:')
output.grid(row=5, column=0, pady=4)

#Creating output (beginning date) textbox
output_entry = Entry(root)
output_entry.configure(state = "disabled")
output_entry.grid(row=5, column=1)

#Creating output (end date) label
output_1 = Label(root, text = 'to')
output_1.grid(row=5, column=2, pady=4)

#Creating output (end date) textbox
output_1_entry = Entry(root)
output_1_entry.configure(state = "disabled")
output_1_entry.grid(row=5, column=3)

#Create error label
error = Label(root, text = '', fg="red")
error.grid(row=6, column=1, pady=4)

#Create function to add month
#(From: https://stackoverflow.com/a/4131114)
def add_months(sourcedate,months):
    """
    Input: the end date of RT and months based on the "Year" Entry
    Output: return the date after the necessary month is added
    """
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return datetime.date(year,month,day)


#Create a function to define the month after the end date based on the year
def year_to_month(year):
    """
    Input: Entry from "Year" Entry
    Output: Month based on the "Year" Entry
    To convert into months based on the year
    - Year 2: 12 months
    - Year 3: 24 months
    - Year 4: 36 months
    - Year 5: 48 months
    - Year 6: 60 months
    """
    if year == "2":
        return 12
    elif year == "3":
        return 24
    elif year == "4":
        return 36
    elif year == "5":
        return 48
    elif year == "6":
        return 60
    else:
        return 0
    
#Create function to convert date
def date_conversion():
    """
    Output: the start date of the duration is "End Date of RT" + number of months based on "Year" Entry
    the end date of the duration is "End Date of RT" + number of months based on "Year" Entry + 2
    """
    error.config(text = "")
    output_entry.configure(state = "normal")
    output_entry.delete(0,END)
    output_1_entry.configure(state = "normal")
    output_1_entry.delete(0,END)
    try: 
        date = datetime.datetime.strptime(end_date_rt.get(), '%d-%m-%Y')
        start_date = add_months(date,year_to_month(year.get()))
        start_date_1 = str(start_date.day) + "-" + str(start_date.month) + "-" + str(start_date.year)
        output_entry.insert(END, start_date_1)
        output_entry.configure(state = "disabled")
        end_date = add_months(date,year_to_month(year.get()) + 2)
        end_date_1 = str(end_date .day) + "-" + str(end_date .month) + "-" + str(end_date .year)
        output_1_entry.insert(END, end_date_1)
        output_1_entry.configure(state = "disabled")
    except ValueError:
        output_entry.insert(END, "Undefined")
        output_1_entry.insert(END, "Undefined")
        output_entry.configure(state = "disabled")
        output_1_entry.configure(state = "disabled")
        error.config(text = "End Date not in" + "\n" + "dd-mm-yyyy format")
        
        
def show_error(self, *args):
    err = traceback.format_exception(*args)
    tkMessageBox.showerror('Exception',err)


#Creating buttons commanding printing output to output box    
b = Button(root, text="Print", command=date_conversion)
b.grid(row=1, column=4,sticky=W)


mainloop()
