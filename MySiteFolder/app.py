from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def opros():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]
        source = request.form.get('source')
        comments = request.form.get('comments')        
        print(f"{name} ({age}) прошел опрос")
        print(source, comments)
        return redirect(url_for('thank'))
    return render_template("opros.html")

@app.route("/thank")
def thank(): return "Спасибо за участие в опросе"

if __name__ == "__main__":
    app.run(debug=True)