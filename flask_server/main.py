from distutils.log import debug
from urllib import request
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/product/getBaseCategoryList")
def categoryList():
    print(request.url)
    return jsonify({"data": "test"})


if __name__ == "__main__":
    app.run(debug=True)
