import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog

def execute_nmap_command(ip_address, ports):
    command = f"nmap -sV -p {ports} --script all {ip_address}"
    try:
        result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
        return True, result
    except subprocess.CalledProcessError as e:
        return False, e.output

def on_submit():
    ip_address = entry_ip.get()
    ports = entry_ports.get()

    if not ip_address or not ports:
        messagebox.showerror("Fehler", "Bitte geben Sie eine IP-Adresse und mindestens einen Port ein.")
        return

    submit_button.config(state=tk.DISABLED)
    export_button.config(state=tk.DISABLED)
    status_label.config(text="Test läuft...", fg="yellow")
    root.update()

    success, result = execute_nmap_command(ip_address, ports)

    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, tk.END)

    if success:
        text_result.insert(tk.END, "Test erfolgreich:\n\n", "success")
        text_result.insert(tk.END, result, "success")
    else:
        text_result.insert(tk.END, "Fehler beim Test:\n\n", "error")
        text_result.insert(tk.END, result, "error")

    text_result.config(state=tk.DISABLED)
    submit_button.config(state=tk.NORMAL)
    export_button.config(state=tk.NORMAL)
    status_label.config(text="Test beendet", fg="lime green")

def export_result():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Datei", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            result_text = text_result.get(1.0, tk.END)
            file.write(result_text)
        messagebox.showinfo("Export Erfolgreich", "Die Ausgabe wurde erfolgreich exportiert.")

def create_gui():
    global entry_ip, entry_ports, submit_button, text_result, status_label, root, export_button
    root = tk.Tk()
    root.title("Krey-iTSec VulnRecon")
    root.configure(background="black")

    frame = tk.Frame(root, padx=20, pady=20, bg="black")
    frame.pack(fill=tk.BOTH, expand=True)  # Füllen Sie das Frame und erweitern Sie es

    label_title = tk.Label(frame, text="Krey-iTSec VulnRecon", font=("Courier", 26, "bold"), fg="lime green", bg="black")
    label_title.pack()

    label_ip = tk.Label(frame, text="IP-Adresse:", font=("Courier", 12), fg="lime green", bg="black")
    label_ip.pack()

    entry_ip = tk.Entry(frame, width=20, font=("Courier", 12))
    entry_ip.pack()

    label_ports = tk.Label(frame, text="Ports (kommagetrennt):", font=("Courier", 12), fg="lime green", bg="black")
    label_ports.pack()

    entry_ports = tk.Entry(frame, width=30, font=("Courier", 12))
    entry_ports.pack()

    submit_button = tk.Button(frame, text="Aufklärung", command=on_submit, font=("Courier", 12, "bold"), bg="#007bff", fg="white")
    submit_button.pack(pady=10)

    export_button = tk.Button(frame, text="Exportieren", command=export_result, font=("Courier", 12, "bold"), bg="#007bff", fg="white")
    export_button.pack(pady=10)
    export_button.config(state=tk.DISABLED)

    status_label = tk.Label(frame, text="", font=("Courier", 12), fg="yellow", bg="black")
    status_label.pack()

    text_result = scrolledtext.ScrolledText(frame, state=tk.DISABLED, font=("Courier", 12), bg="black", fg="lime green")
    text_result.pack(fill=tk.BOTH, expand=True)  # Füllen Sie das Textfeld und erweitern Sie es

    # Definiere die Stile für den Text
    text_result.tag_configure("success", foreground="lime green")
    text_result.tag_configure("error", foreground="red")

    root.mainloop()

if __name__ == "__main__":
    create_gui()
