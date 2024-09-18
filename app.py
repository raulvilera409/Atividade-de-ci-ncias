from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota principal para verificar se o servidor está funcionando
@app.route('/')
def home():
    return "Servidor Flask funcionando!"

# Rota para correção automática
@app.route('/corrigir', methods=['POST'])
def corrigir():
    respostas = request.json  # Recebe as respostas enviadas pelo formulário
    # Chama a função para calcular a nota com base nas respostas
    nota = calcular_nota(respostas)
    return jsonify({'nota': nota})  # Retorna a nota como resposta JSON

def calcular_nota(respostas):
    # Exemplo de lógica de correção para cada pergunta
    nota = 0
    
    # Corrigindo a questão 1
    if respostas.get('resposta1', '').strip().lower() == "a resposta correta para a questão 1":
        nota += 1  # Adiciona 1 ponto se a resposta estiver correta
    
    # Corrigindo a questão 2
    if respostas.get('resposta2', '').strip().lower() == "a resposta correta para a questão 2":
        nota += 1
    
    # Continue adicionando a lógica para as outras questões
    if respostas.get('resposta3', '').strip().lower() == "a resposta correta para a questão 3":
        nota += 1
    
    # ... faça o mesmo para todas as questões
    
    return nota  # Retorna a nota final

if __name__ == '__main__':
    # Rodar o aplicativo Flask
    app.run(host='0.0.0.0', port=5000, debug=True)

