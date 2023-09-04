import subprocess
import tkinter as tk
from tkinter import messagebox
import os
from tkinter import scrolledtext

def execute_nmap_command(target, ports):
    nmap_command = f"nmap -sV -p {ports} --script all {target} && nikto -h {target}"
    try:
        nmap_result = subprocess.check_output(nmap_command, shell=True, text=True, stderr=subprocess.STDOUT)
        return True, nmap_result
    except subprocess.CalledProcessError as e:
        return False, e.output

def on_submit():
    target = entry_target.get()
    ports = entry_ports.get()

    if not target:
        messagebox.showerror("Fehler", "Bitte geben Sie ein Ziel (Domain oder IP-Adresse) an.")
        return

    if not ports:
        ports = "1-65535"

    submit_button.config(state=tk.DISABLED)
    status_label.config(text="Test läuft...", fg="yellow")
    root.update()

    nmap_success, nmap_result = execute_nmap_command(target, ports)
    nikto_success, nikto_result = execute_nikto_command(target)

    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, tk.END)

    if nmap_success:
        text_result.insert(tk.END, "Nmap-Scan erfolgreich:\n\n", "success")
        text_result.insert(tk.END, nmap_result, "success")
    else:
        text_result.insert(tk.END, "Fehler beim Nmap-Scan:\n\n", "error")
        text_result.insert(tk.END, nmap_result, "error")

    text_result.insert(tk.END, "\n\n")

    if nikto_success:
        text_result.insert(tk.END, "Nikto-Scan erfolgreich:\n\n", "success")
        text_result.insert(tk.END, nikto_result, "success")
    else:
        text_result.insert(tk.END, "Fehler beim Nikto-Scan:\n\n", "error")
        text_result.insert(tk.END, nikto_result, "error")

    text_result.config(state=tk.DISABLED)
    submit_button.config(state=tk.NORMAL)
    status_label.config(text="Test beendet", fg="lime green")

def export_to_file():
    file_name = "scan_results.txt"
    with open(file_name, "w") as file:
        file.write(text_result.get(1.0, tk.END))
    messagebox.showinfo("Export abgeschlossen", f"Ergebnisse wurden in {file_name} exportiert.")

def create_gui():
    global entry_target, entry_ports, submit_button, text_result, status_label, root
    root = tk.Tk()
    root.title("Krey-iTSec VulnRecon")
    root.configure(background="black")

    frame = tk.Frame(root, padx=20, pady=20, bg="black")
    frame.pack()

    label_title = tk.Label(frame, text="Krey-iTSec VulnRecon", font=("Courier", 26, "bold"), fg="lime green", bg="black")
    label_title.pack()

    label_target = tk.Label(frame, text="Ziel (Domain oder IP-Adresse):", font=("Courier", 12), fg="lime green", bg="black")
    label_target.pack()

    entry_target = tk.Entry(frame, width=30, font=("Courier", 12))
    entry_target.pack()

    label_ports = tk.Label(frame, text="Ports (kommagetrennt, leer für alle):", font=("Courier", 12), fg="lime green", bg="black")
    label_ports.pack()

    entry_ports = tk.Entry(frame, width=30, font=("Courier", 12))
    entry_ports.pack()

    submit_button = tk.Button(frame, text="Aufklärung", command=on_submit, font=("Courier", 12, "bold"), bg="#007bff", fg="white")
    submit_button.pack(pady=10)

    export_button = tk.Button(frame, text="Exportieren", command=export_to_file, font=("Courier", 12, "bold"), bg="#007bff", fg="white")
    export_button.pack(pady=10)

    status_label = tk.Label(frame, text="", font=("Courier", 12), fg="yellow", bg="black")
    status_label.pack()

    text_result = scrolledtext.ScrolledText(frame, height=10, width=12, state=tk.DISABLED, font=("Courier", 80), bg="black", fg="lime green")
    text_result.pack(fill="both", expand=True)

    text_result.tag_configure("success", foreground="lime green")
    text_result.tag_configure("error", foreground="red")

    root.mainloop()

if __name__ == "__main__":
    create_gui()

