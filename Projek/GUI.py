import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# Function to load a file and display its contents in the table
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:  # Check if a file was selected
        entry_file_path.delete(0, tk.END)  # Clear previous text
        entry_file_path.insert(0, file_path)  # Insert the selected file path
        
        try:
            # Read the CSV file
            data = pd.read_csv(file_path)

            # Clear previous results in the treeview
            for row in tree.get_children():
                tree.delete(row)

            # Insert new results into the treeview
            for index, row in data.iterrows():
                tree.insert("", "end", values=(row.get('STA', ''), 
                                                row.get('Gobs', ''), 
                                                row.get('derajat', ''), 
                                                row.get('menit', ''), 
                                                row.get('detik', ''), 
                                                row.get('Lintang', ''), 
                                                row.get('Easting', ''), 
                                                row.get('Northing', ''), 
                                                row.get('Elevation', '')))

        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("CSV File Loader with Table")

# Set the window to full screen
root.attributes('-fullscreen', False)

# Create and place the widgets
label_file_path = tk.Label(root, text="CSV File Path:")
label_file_path.pack(pady=5)

entry_file_path = tk.Entry(root, width=50)
entry_file_path.pack(pady=5)

button_browse = tk.Button(root, text="Browse", command=load_file)
button_browse.pack(pady=5)

# Create a treeview to display the CSV contents
columns = ('STA', 'Gobs', 'derajat', 'menit', 'detik', 'Lintang', 'Easting', 'Northing', 'Elevation')
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor='center')

# Set the column widths
tree.column('STA', width=100)
tree.column('Gobs', width=100)
tree.column('derajat', width=100)
tree.column('menit', width=100)
tree.column('detik', width=100)
tree.column('Lintang', width=100)
tree.column('Easting', width=100)
tree.column('Northing', width=100)
tree.column('Elevation', width=100)

tree['displaycolumns'] = columns

# Add a scrollbar
scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side='right', fill='y')

tree.pack(pady=10, fill='both', expand=True)

# Start the GUI event loop
root.mainloop()