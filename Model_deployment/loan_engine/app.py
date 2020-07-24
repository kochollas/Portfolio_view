import os, math
import pandas as pd 
from flask import Flask, request, render_template, flash, url_for, send_from_directory, redirect,abort
from werkzeug.utils import secure_filename
import requests
import pickle 
UPLOAD_FOLDER = '/home/mikes/Documents/jobs2020/portfolio/Model_deployment/loan_engine/uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
model = pickle.load(open('model.pkl','rb'))

#@app.route('/')
#def home():
#    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Handling the password for the pdf doc
        form_req = request.form 
        password = form_req.get('pass')
        
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('predict',
                                 filename=filename, pwd=password))
   
   
   
    return render_template('index.html')


@app.route('/sendfile/<filename>',methods=['GET', 'POST'])
def send_pdf(filename):
    try:
        return send_from_directory(
            app.config['UPLOAD_FOLDER'],filename=filename, as_attachment = True
        )
    except FileNotFoundError:
        abort(404)

@app.route('/predict/<filename>',methods=['GET', 'POST'])
def predict(filename):
    '''
    For rendering results on HTML GUI
    '''
   
    args = request.args
    if 'pwd' in args:
        nid = args["pwd"]
        url = 'http://127.0.0.1:8000/load_mpesa'
        r = requests.post(url,json={'nid':nid, 'filename':filename})
        X = r.json()
        # transform any NaN from APIs output list
        for i in range(6):
            if X[i]== 'NaN':
                X[i]=0
        print(X)
        output = model.predict([X])
        msg ='something wrong'
        if output ==[]:
            return render_template('predicted.html', prediction_text='Ksh. {}'.format(msg))
        else:
            return render_template('predicted.html', prediction_text= 'Ksh. {}'.format(output[0]))


    else:
        return "No query string received", 200 



if __name__ =="__main__":
    app.run(debug=True)
