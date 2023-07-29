# DocFinder

This project is about creating a document search using keywords from a database, which involves processing a [dataset](https://www.boleary.com/blog/posts/202307-pmn/#download-the-data), populating it in a MySQL database, and searching the document from the database using a web application. Based on the keyword search, the webpage will return the submission_number, page_number, embedded_text, and OCR_text. Follow the steps below to set up and run the project.

## Step 1: Extracting and Preparing the Dataset

1. Clone this repository on your local machine.
2. Open a terminal and navigate to the project directory.
3. Execute the Python script `TextProcessing.py` to extract and convert the dataset into the proper format.

## Step 2: Download the Processed Dataset

1. Once the Python script has run successfully, you'll find the generated CSV file.
2. Download the CSV file and save it locally.

## Step 3: Setting up the MySQL Database

1. Connect to your MySQL server.
2. Create a new database using the schema given in `tables.sql`. You can execute the SQL commands through a MySQL client or interface.

## Step 4: Populating the MySQL Database

1. Use the Python script `insert_summary_data.py` to populate the MySQL database with the CSV dataset.
2. Before running the script, make sure to update the SQL parameters such as database name, host IP, password, and user. Your parameters are different than mine ;)

## Step 5: HTML Templates

1. The `templates` directory contains the HTML files required for a given task.

## Step 6: Running the Web Application

1. Make sure you have Flask installed (`pip install flask`).
2. Run the `app.py` script to start the web application.
3. Use the provided URL to access the web application on your local device and test its functionality.

## Step 7: Debugging

1. If you encounter any issues, set the `debug` mode to `True` in `app.py` to enable debugging and get detailed error messages.

For any queries or assistance, feel free to reach out to sumit.atlancey@gmail.com.

## Demo Video

[Demo Video]: (https://drive.google.com/file/d/1hyK2T9jdMKBjNfWTMNkhUddMUbd1ipf4/view?usp=sharing)https://drive.google.com/file/d/1hyK2T9jdMKBjNfWTMNkhUddMUbd1ipf4/view?usp=sharing)


