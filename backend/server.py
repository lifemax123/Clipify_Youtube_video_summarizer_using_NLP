from flask import Flask
import summerise as summerise
from flask import Flask, flash, redirect, render_template, request, session, abort, send_file
import os
 
app = Flask(__name__)
 
@app.route('/')
def parameterExtraction():
    if request.method == 'GET':
        parsed_url = request.args['link']
        result = summerise.final(parsed_url)
        folder_path = "C:/Users/lifemax/OneDrive/Desktop/clipfy/backend"
        files = os.listdir(folder_path)
        file=""
        for i in files:
            if "summarized" in i:
                file=i
                break
        return send_file(file, as_attachment=False)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)