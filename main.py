from flask import Flask, render_template

app = Flask(__name__,static_folder="static",template_folder="template",static_url_path='/')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/article')
def article():
    return render_template("article.html")

if __name__ == "__main__":
    app.run(debug=True)