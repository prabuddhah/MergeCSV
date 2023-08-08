# Description:
This Python script is designed to efficiently merge data from multiple CSV log files into a single cohesive dataset. It utilizes the pandas library to manage and manipulate the CSV data.

# Usage:
1) Prerequisites. 
   - Ensure you have Python (version 3.6 or higher) installed on your system.
   - Install the pandas library if you haven't already:
        pip install pandas
2) Clone the Repository:
    - Clone this repository to your local machine using your preferred method (HTTPS, SSH, GitHub CLI, etc.)..
3) Navigate to the Script:
    - Open a terminal or command prompt and navigate to the directory containing the mergecsv.py.
4) Define Input and Output Paths:
    - In the script, modify the file paths to point to your source files to be merged.
5) Run the Script:
    - Execute the script by running the following command in the terminal:
        python mergecsv.py
    - This will initiate the process of reading the input CSV file, selecting the desired columns, and saving the updated data to the output CSV file.
6) Monitor Progress:
    - The script will display progress updates in the terminal as it performs each step of the data processing. This helps you keep track of the current execution status.
7) Review Output:
    - Once the script completes, navigate to the specified output_file path to find the new CSV file named Merged_Logs.csv.
8) Customization:
    - If needed, you can customize the filenames to include the specific files you want to merge.
