from flask import Flask

app = Flask("my app")

NETTOOLKIT_API_TOKEN = "test_8F6P51ZjL21CLncoXsJ6Yw1SvOCSe7igfxUaPK7C"
aws_access_key_id = AKIAYVP4CIPPERUVIFXG
aws_secret_access_key = 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

@app.route('/')
def hello():
    return "Hellooo"

if __name__ == "__main__":
    app.run(debug=True)
