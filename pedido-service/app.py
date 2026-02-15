from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/criar_pedido', methods=['POST'])
def criar_pedido():
    return jsonify({
        "pedido_id": 12345,
        "status": "PROCESSADO",
        "mensagem": "Pedido criado com sucesso!"
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
