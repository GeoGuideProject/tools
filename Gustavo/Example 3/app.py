import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os, csv, re
from flask import Flask, render_template, request, send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_TMP = os.path.join(APP_ROOT, 'tmp')
app.config['UPLOAD_FOLDER'] = 'tmp/'
app.config['ALLOWED_EXTENSIONS'] = set(['csv', 'json'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def file_proc():
    number = []
    with open(os.path.join(APP_TMP, 'arquivo.csv')) as f:
        for row in csv.reader(iter(f.readline, '')):
            options = row
            break
    for x in options:
        print(re.search("[+-]?(([1-9][0-9]*)|(0))([.,][0-9]+)?", x) is True)
    print(number)
    return render_template('select.html', option_list=options)

@app.route('/')
def index():
    formatsmsg = 'Only accept: '
    for x in app.config['ALLOWED_EXTENSIONS']:
        formatsmsg += ' ' + x.upper()
    return render_template('index.html', formatsmsg=formatsmsg)

@app.route('/selectdata', methods=['POST'])
def selectdata():
    filter = [request.form.get('filter1'), request.form.get('filter2'),request.form.get('filter3'), request.form.get('filter4')]
    positions = [request.form.get('latitude1'),  request.form.get('longitude1'),  request.form.get('latitude2'),  request.form.get('longitude2')]
    print(positions[0], positions[1], positions[2], positions[3])
    return render_template('charts.html', csvfilename='arquivo.csv', filter=filter, positions=positions)

@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'arquivo.csv'))
        return file_proc()
    else:
        return render_template('index.html', formatsmsg='Format not suported! Try again!')

@app.route('/tmp/<path:filename>')
def sendcsv(filename):
    print("teste")
    return send_from_directory(APP_TMP, filename)

@app.route('/static/<path:filename>')
def sendstatic(filename):
    return send_from_directory('/static', filename)

app.run(use_reloader=True, port=8090)
