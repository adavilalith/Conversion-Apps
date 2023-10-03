import tkinter as tk

def conversion_func():
    temp_in_F=celsius_temp.get()*9/5+32
    label2.configure(text=str(temp_in_F)+" F")

window=tk.Tk()
window.title("Celsius To Fahrenheit converter")
window.geometry("200x100")

label1=tk.Label(text="Temperature in Celsius")
label1.pack()
celsius_temp=tk.DoubleVar()
celsius_entry=tk.Entry(textvariable=celsius_temp)
celsius_entry.pack()
convert_button=tk.Button(text="Convert",command=conversion_func)
convert_button.pack()
label2=tk.Label()
label2.pack()

window.mainloop()