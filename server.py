from flask import Flask, jsonify, render_template
import os

PORT = 8000
MESSAGE = "Hello, world!\n"

app = Flask(__name__)

@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result

@app.route("/env/")
def hello():
    env = []
    for item, value in os.environ.items():
      if item.startswith("APP_CONFIG"):
        env.append('{}: {}'.format(item, value)) 

    return jsonify(env)
     
@app.route("/config/")
def config():
    try:
      with open("k8s-workshop-configmap/app.config", "r") as f:
        result = f.read()
    except:
      result = "File k8s-workshop-configmap/app.config not found."

    return render_template("template.html", content=result) 

@app.route("/jx")
def jx():
    result = "Welcome to Jenkins X. Hope you have fun".encode("utf-8")
    return result

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
