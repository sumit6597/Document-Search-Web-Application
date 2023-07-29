# Text Processing and MySQL Data Visualization

This project involves processing a dataset, storing it in a MySQL database, and searching the documnet from the database using a web application. Follow the steps below to set up and run the project.

## Step 1: Extracting and Preparing the Dataset

1. Clone this repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Execute the Python script `TextProcessing.py` to extract and convert the dataset into the proper format.

## Step 2: Download the Processed Dataset

1. Once the Python script has run successfully, you'll find the generated CSV file.
2. Download the CSV file and save it locally.

## Step 3: Setting up the MySQL Database

1. Connect to your MySQL server.
2. Create a new database using the schema given in `tables.sql`. You can execute the SQL commands in a MySQL client or interface.

## Step 4: Populating the MySQL Database

1. Use the Python script `insert_summary_data.py` to populate the MySQL database with the CSV dataset.
2. Before running the script, make sure to update the SQL parameters such as database name, host IP, password, and user.

## Step 5: HTML Templates

1. The `templates` directory contains the HTML files required for given task.

## Step 6: Running the Web Application

1. Make sure you have Flask installed (`pip install flask`).
2. Run the `app.py` script to start the web application.
3. Use the provided URL to access the web application on your local device and test its functionality.

## Step 7: Debugging

1. If you encounter any issues, set the `debug` mode to `True` in `app.py` to enable debugging and get detailed error messages.

For any queries or assistance, feel free to reach out to sumit.atlancey@gmail.com.

