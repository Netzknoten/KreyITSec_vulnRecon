import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
import socket

def resolve_domain_to_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def execute_nmap_command(ip_address, ports):
    if not ports:
        ports = "1-65535"  # Wenn keine Ports angegeben sind, alle Ports scannen

    command = f"nmap -sV -sA -p {ports} --script all {ip_address}"
    try:
        result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
        return True, result
    except subprocess.CalledProcessError as e:
        return False, e.output

def export_to_file(result_text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(result_text)
        messagebox.showinfo("Export abgeschlossen", f"Daten wurden in {file_path} gespeichert.")

def on_submit():
    domain = entry_domain.get()
    ports = entry_ports.get()

    if not domain:
        messagebox.showerror("Fehler", "Bitte geben Sie einen Domainnamen ein.")
        return

    # Domain in IP-Adresse auflösen
    ip_address = resolve_domain_to_ip(domain)

    if ip_address is None:
        messagebox.showerror("Fehler", "Die Domain konnte nicht aufgelöst werden.")
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

def create_gui():
    global entry_domain, entry_ports, submit_button, export_button, text_result, status_label, root
    root = tk.Tk()
    root.title("VulnRecon")
    root.configure(background="black")

    frame = tk.Frame(root, padx=20, pady=20, bg="black")
    frame.pack()

    label_title = tk.Label(frame, text="VulnRecon", font=("Courier", 26, "bold"), fg="lime green", bg="black")
    label_title.pack()

    label_domain = tk.Label(frame, text="Domain-Name:", font=("Courier", 12), fg="lime green", bg="black")
    label_domain.pack()

    entry_domain = tk.Entry(frame, width=20, font=("Courier", 12))
    entry_domain.pack()

    label_ports = tk.Label(frame, text="Ports (kommagetrennt, leer lassen für alle):", font=("Courier", 12), fg="lime green", bg="black")
    label_ports.pack()

    entry_ports = tk.Entry(frame, width=30, font=("Courier", 12))
    entry_ports.pack()

    submit_button = tk.Button(frame, text="Aufklärung", command=on_submit, font=("Courier", 12, "bold"), bg="#007bff", fg="white")
    submit_button.pack(pady=10)

    export_button = tk.Button(frame, text="Exportieren", command=lambda: export_to_file(text_result.get(1.0, tk.END)), font=("Courier", 12, "bold"), bg="#007bff", fg="white")
    export_button.pack(pady=10)

    status_label = tk.Label(frame, text="", font=("Courier", 12), fg="yellow", bg="black")
    status_label.pack()

    text_result = scrolledtext.ScrolledText(frame, height=15, width=80, state=tk.DISABLED, font=("Courier", 12), bg="black", fg="lime green")
    text_result.pack(fill=tk.BOTH, expand=True)

    # Definiere die Stile für den Text
    text_result.tag_configure("success", foreground="lime green")
    text_result.tag_configure("error", foreground="red")

    root.mainloop()

if __name__ == "__main__":
    create_gui()
