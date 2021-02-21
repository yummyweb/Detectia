from flask import Flask, render_template, request
import nn
app = Flask(__name__)


@app.route('/')
def home():
   return render_template("main.html")

@app.route('/detect', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        a = nn.searchnet('Truth.db')
        res = a.getresult(request.form['statement']) 
        
        if res[0] > res[1]:
            return "Lie Bitch"
        else:
            return "True Heavens"
    
    else:
        return render_template("detect.html")

if __name__ == '__main__':
    app.run()