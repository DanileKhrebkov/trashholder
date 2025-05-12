
from flask import Flask, request, render_template
app = Flask(__name__)

about_title = "Страница - биография"
admin = True
langs = ["Ruby", "LUA", "Python", "Crystal", "Julia"]

@app.route("/")
def main():
    return render_template('index2.html', admin = admin)

@app.route("/about")
def about():
    return render_template('about.html', title=about_title, langs=langs)

if __name__ == "__main__":
    app.run(debug=True)



# FOR GET_OPROS

# from flask import Flask, request, render_template, redirect, url_for
# app = Flask(__name__)

# @app.route("/")
# def opros():
#     return render_template("get_opros.html")

# @app.route("/search", methods=['GET'])
# def search():
#     query = request.args.get('q')
#     return f"Ничего не найдено по запросу: {query}"

# if __name__ == "__main__":
#     app.run(debug=True)