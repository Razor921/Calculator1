import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta


def calculate():
    try:
        current_bin_level = float(entry_b.get())
        current_hfr = float(entry_c.get())

        target_bin_level = 1020
        minutes = 60

        result = (target_bin_level - current_bin_level) / (current_hfr * minutes)

        total_minutes = int(result * 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60

        current_time = datetime.now()
        future_time = current_time + timedelta(hours=hours, minutes=minutes)

        formatted_time = future_time.strftime("%H:%M (%d %B %Y)")

        font_size = int(min(app.winfo_width(), app.winfo_height()) * 0.06)

        result_label.config(text="Estimate Changeout Time:\n" + formatted_time, font=("Arial", font_size),
                            justify="center")
        result_label.place(relx=0.5, rely=0.55, anchor="center")

    except Exception as e:
        messagebox.showerror("Error", "Invalid input: {}".format(e))


app = tk.Tk()
app.title("Harvest Changeout Calculator")

# Reduced header size and centered
header = tk.Label(app, text="Harvest Changeout Calculator", font=("Arial", 12, "bold"))
header.pack(pady=5)

frame = tk.Frame(app)
frame.place(relx=0.5, rely=0.3, anchor="center")

tk.Label(frame, text="Current Bin Level:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_b = tk.Entry(frame, width=20)
entry_b.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Current HFR:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_c = tk.Entry(frame, width=20)
entry_c.grid(row=1, column=1, padx=5, pady=5)

btn_calculate = tk.Button(frame, text="Calculate", command=calculate)
btn_calculate.grid(row=2, column=0, columnspan=2, pady=10)

# Result label - aligned and increased visibility
result_label = tk.Label(app, text="", font=("Arial", 24), fg="blue", pady=10)
result_label.place(relx=0.5, rely=0.55, anchor="center")


def resize_font(event):
    font_size = int(min(event.width, event.height) * 0.06)
    result_label.config(font=("Arial", font_size))


app.bind("<Configure>", resize_font)

app.minsize(350, 300)
app.geometry("400x350")

app.mainloop()
