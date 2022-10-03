
from flask import Flask, jsonify, request
import json

from functions import allprod, limprod

app = Flask(__name__)

@app.route('/mercadoLibre', methods=["GET"])
def mercadoLibre():
    data = json.loads(request.data)
    if "limite" not in data:
        titulos, urls, precios = allprod(data["producto"])
    else:
        titulos, urls, precios = limprod(data["producto"], data["limite"])
    return jsonify({"datos":{"titulos":titulos, "urls": urls, "precios":precios}})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

