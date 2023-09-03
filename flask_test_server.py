from flask import Flask

app = Flask("my app")

NETTOOLKIT_API_TOKEN = "test_8F6P51ZjL21CLncoXsJ6Yw1SvOCSe7igfxUaPK7C"


@app.route('/')
def hello():
    return "Hellooo"

if __name__ == "__main__":
    app.run(debug=True)
