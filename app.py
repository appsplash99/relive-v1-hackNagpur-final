import random
from flask import Flask, render_template, request
from flask import jsonify
from data import generate_DATA
from string_data import generate_Data_to_HTML
import json

# flask app instance
app = Flask(__name__)

# creating a url route for home page
# @app.route('/', methods=['GET', 'POST'])
@app.route('/')
def home_page():
    return render_template('home.html')

# url route for contact page
@app.route('/aboutus')
def contact_page():
    return render_template('aboutus.html')

# shows data when button clicked
@app.route('/show_data', methods=['GET', 'POST'])
def show_data_page():

    # stores data into a long html string
    final_html_data = generate_Data_to_HTML()
    return final_html_data




# repl run
# # to run the app via terminal
# if __name__ == "__main__":
#     app.run(
#             host='0.0.0.0',
#             port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
#             debug=True
#         )

# to run the app via terminal
if __name__ == "__main__":
    app.run(debug=True)
