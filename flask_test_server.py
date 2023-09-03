from flask import Flask

app = Flask("my app")

NETLIFY_API_TOKEN = "56464-67676-67699"

@app.route('/')
def hello():
    return "Hellooo"

if __name__ == "__main__":
    app.run(debug=True)
