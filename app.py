from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__)

def get_process_on_port(port_number):
    f = open("tmp.txt", "w")
    subprocess.check_call('lsof -i:{}'.format(port_number), shell=True, stdout=f)
    f.close()

@app.route('/', methods=['GET', 'POST'])
def lsof_output():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        port = request.form.to_dict()
        port = port['port']
        get_process_on_port(port)
        op = open("tmp.txt", "r").read()
        return render_template('index.html', output=op)