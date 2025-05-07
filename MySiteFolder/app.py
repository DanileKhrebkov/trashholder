from flask import Flask, jsonify, render_template
class MyApp(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_routes()

    def setup_routes(self):
        @self.route('/')
        def home():
            return render_template("index.html")
        
        @self.route('/api/data')
        def get_data():
            return jsonify({"status":"ok", "data":[1,2,3]})
app = MyApp(__name__)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()





# from flask import Flask, render_template, request
# app = Flask(__name__, static_folder="static")
# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method =="POST":
#         username = request.form['username']
#         password = request.form['password']
#         return f"Вы вошли в систему, {username}"
#     else:
#         return render_template("login.html")
# if __name__ == "__main__":
#     app.run(debug=True)