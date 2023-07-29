import mysql.connector
from flask import Flask, render_template, request
from jinja2 import Environment, PackageLoader
import re

app = Flask(__name__)


# handle the conversion of both search_query and text to strings before performing the case-insensitive replacement with the re.sub function
def case_insensitive_replace(text, search_query):
    if not isinstance(search_query, str):
        search_query = str(search_query)
    if not isinstance(text, str):
        text = str(text)

    search_words = search_query.split()

    for word in search_words:
        text = re.sub(re.escape(word), lambda match: f'<span class="highlight">{match.group(0)}</span>', text, flags=re.IGNORECASE)

    return text

app.jinja_env.filters['case_insensitive_replace'] = case_insensitive_replace

# String Match function
def search_text(text_to_search):
    search_results = []
    search_query = text_to_search.lower()

    # Split the search query into individual words
    search_words = search_query.split()

    # Perform string matching search
    for submission in sample_data:

        text_embedded = submission["text_embedded"].lower() if submission["text_embedded"] else ""
        text_ocr = submission["text_ocr"].lower() if submission["text_ocr"] else ""

        # Check if all search words are present in either text_embedded or text_ocr
        if all(word in text_embedded or word in text_ocr for word in search_words):
            search_results.append(submission)

    return search_results

# route to the home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_query = request.form.get("search_query")
        if search_query is not None and search_query.strip():
            # Perform the search using the string matching function we implemented above
            search_results = search_text(search_query)
            return render_template("index.html", results=search_results, search_query=search_query)

    return render_template("index.html", results=[])

if __name__ == "__main__":
    # Database connection parameters
    db_user = ""    #user name
    db_password = ""     #password for database
    db_host = ""         #host ip, for example 127.0.0.1
    db_name = ""         #database name which you are currently using

    #establish the database connection
    try:
        cnx = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )

        # Create a cursor to execute queries
        cursor = cnx.cursor()

        sample_data = []
        query = "SELECT * FROM Summary"
        cursor.execute(query)
        for row in cursor:
            submission = {
                "submission_number": row[0],
                "date_obtained": row[1],
                "page_number": row[2],
                "text_embedded": row[3],
                "text_ocr": row[4]
            }
            sample_data.append(submission)

        cursor.close()
        cnx.close()

        app.run(debug=True)

    except mysql.connector.Error as err:
        print("Error connecting to the MySQL database:", err)