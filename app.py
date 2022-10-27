from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "ciaone"

#selecting a route for our app
@app.route("/hello") #/hello will represent the last part of our URL
def index(): #verrà eseguita quando verrà messo l'URL finale con /hello
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"]) #specifico i metodi che voglio perchè sto interagendo con il server
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)