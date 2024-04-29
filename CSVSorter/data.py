import os
import csv
import tkinter as tk
from tkinter import filedialog

def get_sort_options(csv_file):
    with open(csv_file, "r") as f:
        # Read the header line from the CSV file
        header = f.readline().strip().split(',')
        return header

def datasearch(data, data_output, sort_by):
    with open(data, "r") as f: 
        # Read the lines from the CSV file
        lines = f.readlines()

        # Extract the header line and remove it from the data
        header = lines[0]
        lines = lines[1:]

        # Determine the index of the column to sort by
        column_index = header.strip().split(',').index(sort_by)

        # Sort the lines based on the chosen column
        sorted_lines = sorted(lines, key=lambda line: line.strip().split(',')[column_index])

    # Write the sorted data to a new CSV file in the Downloads folder
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads', data_output)
    with open(download_path, "w", newline="") as csvfile: 
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header.strip().split(','))  # Write the header line
        for line in sorted_lines: 
            csv_writer.writerow(line.strip().split(','))

    print(f"Data sorted and saved to '{download_path}'.")

# Create a Tkinter window for file selection
root = tk.Tk()
root.withdraw()

# Ask the user to select a CSV file
file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])

# Check if a file was selected
if file_path:
    # Get the sorting options based on the CSV file header
    sort_options = get_sort_options(file_path)

    print("Available sorting options:")
    for index, option in enumerate(sort_options, start=1):
        print(f"{index}. {option}")

    # Get user input for sorting option
    choice = int(input("Enter the number corresponding to the option you want to sort by: "))
    selected_option = sort_options[choice - 1]

    output_file = "sorted_data.csv"
    datasearch(file_path, output_file, selected_option)

else:
    print("No file selected. Exiting...")
