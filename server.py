from flask import Flask, render_template, request, url_for, redirect # This module helps us run our html,css and js files
app = Flask(__name__)
import csv

@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# # Now we are adding multiple routes
# @app.route('/works.html')
# def work():
#     return render_template('works.html')
# Above we are repeating code over and over for re routing. Is there a smarter way? Yes

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# csv stands for comma separated values
def write_to_csv(data):
    with open('database.csv', mode='a', newline= '') as database2:
       email = data["email"]                          
       subject = data["subject"]
       message =data["message"]
       csv_writer = csv.writer(database2, delimiter = ',',quotechar = '"', quoting = csv.QUOTE_MINIMAL) # delimiter is comma here which means each item in the row will be separated by comma
       csv_writer.writerow([email,subject,message])






def write_to_file(data):
    with open('database.txt', mode='a') as database:
       email = data["email"]                          # We can extract data from the dictionary we get in the terminal
       subject = data["subject"]
       message =data["message"]
       file = database.write(f'\n{email},{subject},{message}')   # Here we are writing the data in the txt file




# In methods = ['POST', 'GET'] codeline (expression or statement is it?) get means browser want us to send information and post means that the browser wants us to save information

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #return 'form submitted hoooorayyy!'
    if request.method == 'POST':
        try:
            data = request.form.to_dict()   # Here we can grab all the contact information provided by the user in our webpage in the form of a dictionary. This will appear on the terminal
            #print(data)
            #write_to_file(data)              # Instead of printing the data we are writing it
            write_to_csv(data)              # This time we are writing it to a csv file
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again'