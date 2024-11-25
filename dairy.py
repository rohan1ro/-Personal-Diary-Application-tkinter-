import tkinter as tk
from tkinter import filedialog, messagebox
import os
from datetime import datetime


# Save the diary entry to a file
def save_entry():
    entry_text = text_area.get("1.0", tk.END).strip()
    if not entry_text:
        messagebox.showwarning("Warning", "The diary entry is empty.")
        return

    # Generate filename based on the current date
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"Diary_{date_str}.txt"

    # Ask user for save location
    save_path = filedialog.asksaveasfilename(
        initialfile=filename,
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if save_path:
        try:
            with open(save_path, "w") as file:
                file.write(entry_text)
            messagebox.showinfo("Success", f"Entry saved as '{save_path}'.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save entry: {e}")


# Open and display a saved diary entry
def open_entry():
    file_path = filedialog.askopenfilename(
        title="Open Diary Entry",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "r") as file:
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open entry: {e}")


# Clear the text area
def clear_text():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear the entry?"):
        text_area.delete("1.0", tk.END)


# Create the main application window
root = tk.Tk()
root.title("Personal Diary")
root.geometry("600x400")

# Add text area for writing
text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12), undo=True)
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Add a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, padx=10, pady=5)

# Add buttons
save_button = tk.Button(button_frame, text="Save Entry", command=save_entry, bg="lightgreen", font=("Arial", 10))
save_button.pack(side=tk.LEFT, padx=5)

open_button = tk.Button(button_frame, text="Open Entry", command=open_entry, bg="lightblue", font=("Arial", 10))
open_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear Entry", command=clear_text, bg="lightcoral", font=("Arial", 10))
clear_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=root.quit, bg="gray", font=("Arial", 10))
exit_button.pack(side=tk.RIGHT, padx=5)

# Run the application
root.mainloop()
