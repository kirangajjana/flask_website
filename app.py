from flask import Flask


app=Flask("___name__")


@app.route("/home")
@app.route("/")
def home():
    return "hello all welcome to the flask home page"

if __name__=="__main__":
    app.run(debug=True)
    