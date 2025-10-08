from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():    
    autor = "yo"
    arr = ["pepe","pica","papas","con","un","pico","pepe","pica","papas"]
    return render_template('index.html' , nombre = autor , nose = arr)
if __name__ == '__main__':    
    app.run(debug=True)

@app.route("/index1")
def index1():
    pepe = "papa"
    return render_template("index1.html" , nosabo = pepe)
