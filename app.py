import os
from flask import Flask, jsonify, request, render_template
import subprocess
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # If a POST request is received, process the form data and display the output
    if request.method == 'POST':
        # Parse the form data
        text = request.form['text']
        timeout = 8
        size = request.form['size']

        # Call your C code
        cmd = f"make -j && ./main -m models/7B/ggml-model-q4_0.bin -p \"{text}\" -t {timeout} -n {size}"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()

        out_str = out.decode('utf-8')
        start_str = "1.300000\n\n\n"
        end_str = "\n\nmain:"
        start_index = out_str.find(start_str)
        end_index = out_str.find(end_str, start_index)
        
        if start_index != -1 and end_index != -1:
            predicted_text = out_str[start_index + len(start_str):end_index].strip()
        else:
            predicted_text = "Error: predicted text not found"
    
        # Render the output template with the result
        if proc.returncode != 0:
            return render_template('index.html', result=err.decode('utf-8'), error=True)
        else:
            return render_template('index.html', result=predicted_text, error=False)

    # If a GET request is received, render the input form
    else:
        return render_template('index.html', result='', error=False)

if __name__ == '__main__':
    app.run(debug=True)