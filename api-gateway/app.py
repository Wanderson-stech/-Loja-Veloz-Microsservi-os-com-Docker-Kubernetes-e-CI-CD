from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

PEDIDOS_URL = os.getenv('PEDIDOS_URL', 'http://pedido-service:5000')

@app.route('/')
def home():
    return jsonify({"message": "API Gateway Loja Veloz Online v1.0"})

@app.route('/comprar', methods=['POST'])
def comprar():
    try:
        response = requests.post(f"{PEDIDOS_URL}/criar_pedido")
        return jsonify(response.json()), response.status_code
    except:
        return jsonify({"error": "Servico de pedidos indisponivel"}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
