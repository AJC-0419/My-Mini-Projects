import qrcode as qr
import tkinter as tk

def qr_generator(url, image_name):
    qr_code = qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_code.add_data(url)
    qr_code.make(fit=True)

    img = qr_code.make_image(fill_color="black", back_color="white")
    img.save(f"{image_name}.png")



A = tk.Tk()
A.title("Qr Code Generator")
A.resizable(False, False)


frame = tk.Frame(A,width=200,height=50) 
frame.pack(padx=10,pady=10,fill=tk.X)

Name = tk.Label(frame, text="QR Code Generator", font=("Arial", 25))
Name.pack()

frame2 = tk.Frame(A,width=400,height=250)
frame2.pack(padx=10, fill=tk.X)
url_label = tk.Label(frame2, text="URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
url_entry = tk.Entry(frame2, width=30)
url_entry.grid(row=0, column=1,padx=10, pady=10)
image_name = tk.Label(frame2, text="Image Name:")
image_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
image_entry = tk.Entry(frame2, width=30)
image_entry.grid(row=1, column=1,padx=10, pady=10)

frame3 = tk.Frame(A,width=400,height=250)
frame3.pack(padx=10, fill=tk.X)
submit_button = tk.Button(frame3, text="Generate QR Code", command=lambda: qr_generator(url_entry.get(), image_entry.get()))
submit_button.pack(padx=10, pady=10, fill=tk.X)
reset_button = tk.Button(frame3, text="Reset", command=lambda: (url_entry.delete(0, tk.END), image_entry.delete(0, tk.END)))
reset_button.pack(padx=10, pady=10, fill=tk.X)


A.mainloop()
