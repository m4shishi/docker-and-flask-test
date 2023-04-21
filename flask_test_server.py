from flask import Flask

app = Flask("my app")

@app.route('/')
def hello():
    return "Hellooo"

if __name__ == "__main__":
    app.run(debug=True)