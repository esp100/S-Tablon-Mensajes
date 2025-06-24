
from flask import Flask, request, jsonify,  render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Datos de conexión del servidor REST
HOST = '127.0.0.1'
PORT = 5000

# Lista para almacenar los mensajes 
messages = [] 


@app.get('/')
def home():
   return render_template('cli_ccy.html')


@app.get('/publisher')
def home():
   return render_template('cli_ccy2.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    if not data or 'tittle' not in data or 'message' not in data:
        return jsonify({'error': 'Se requiere título y mensaje'}), 400

    tittle = data['tittle']
    message = data['message'] 
    messages.append({'sender': tittle, 'content': message})
    return jsonify({'status': 'Mensaje enviado y difundido'}), 200

@app.route('/receive', methods=['GET'])
def get_messages():
    return jsonify(messages), 200

if __name__ == '__main__':
    print(f'Servidor REST centralizado iniciado en http://{HOST}:{PORT}')
    app.run(host=HOST, port=PORT, debug=True)