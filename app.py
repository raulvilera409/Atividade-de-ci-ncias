<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Atividade Discursiva</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script> <!-- Biblioteca Chart.js -->
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      background: linear-gradient(to bottom, #FFD580, #B2FF99);
      color: black;
    }
    h1 {
      text-align: center;
      font-weight: normal;
    }
    h3 {
      font-weight: normal;
      margin: 0;
    }
    label, button, textarea {
      font-weight: normal;
    }
    .header-inputs {
      margin-bottom: 10px;
    }
    input, textarea {
      width: 25%;
      padding: 10px;
      margin-bottom: 40px;
      font-size: 12px;
      color: black;
    }
    textarea {
      width: 100%;
      height: 250px;
      margin-top: 10px;
      font-size: 16px;
    }
    button {
      display: block;
      margin: 20px auto;
      padding: 10px 20px;
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
      font-size: 14px;
      font-weight: normal;
    }
    button:hover {
      background-color: #45a049;
    }
    /* Feedback visual de respostas */
    .correto {
      background-color: lightblue;
      color: blue;
    }
    .erro {
      background-color: lightcoral;
      color: red;
    }
    /* Posicionamento do relógio no topo direito */
    .question {
      position: relative;
      margin-bottom: 20px;
      padding-right: 60px; /* Espaço para o relógio */
    }
    .clock {
      position: absolute;
      right: 10px;
      top: 10px;
      font-size: 14px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <center><h1><b>AVALIAÇÃO DE CIÊNCIAS (3º BIMESTRE)</b></h1></center>
  <form id="discursive-form">
    <!-- Cabeçalho com nome, série e dados -->
    <div class="header-inputs">
      <label for="nome">Nome:</label>
      <input type="text" id="nome" name="nome" placeholder="Digite seu nome aqui..." required>
      <label for="serie">Série:</label>
      <input type="text" id="serie" name="serie" placeholder="Digite sua série..." required>
      <label for="data">Data:</label>
      <input type="date" id="data" name="data" required>
    </div>

    <!-- Questões Discursivas com Relógio -->
    <div class="question">
      <h3><b>1.</b> Mudanças climáticas são geradas globalmente uma alteração nos habitats de diversas espécies. Explique como o isolamento geográfico pode levar à especiação, considerando o impacto das mudanças climáticas nos ambientes naturais. 
        <span id="clock1" class="clock">00:00</span>
      </h3>
      <textarea id="resposta1" name="resposta1" placeholder="Digite sua resposta aqui..." required onfocus="startClock(1)" onblur="stopClock(1)"></textarea>
    </div>

    <div class="question">
      <h3><b>2.</b> Os fósseis indicam que as baleias modernas evoluíram de mamíferos terrestres há milhões de anos. Utilizando o conceito de órgãos homólogos, explique o processo evolutivo que pode ter levado à transformação dos membros anteriores de mamíferos terrestres nos membros atuais das baleias.
        <span id="clock2" class="clock">00:00</span>
      </h3>
      <textarea id="resposta2" name="resposta2" placeholder="Digite sua resposta aqui..." required onfocus="startClock(2)" onblur="stopClock(2)"></textarea>
    </div>

    <div class="question">
      <h3><b>3.</b> O uso estendido de antibióticos tem causado o surgimento de bactérias resistentes a medicamentos. Explique como a seleção natural pode levar ao desenvolvimento de populações bacterianas resistentes a antibióticos.
        <span id="clock3" class="clock">00:00</span>
      </h3>
      <textarea id="resposta3" name="resposta3" placeholder="Digite sua resposta aqui..." required onfocus="startClock(3)" onblur="stopClock(3)"></textarea>
    </div>

    <div class="question">
      <h3><b>4.</b> Tanto as aves quanto os insetos desenvolveram a capacidade de voar. Suas asas são exemplos de órgãos análogos. Explique como órgãos análogos estão relacionados à evolução convergente.
        <span id="clock4" class="clock">00:00</span>
      </h3>
      <textarea id="resposta4" name="resposta4" placeholder="Digite sua resposta aqui..." required onfocus="startClock(4)" onblur="stopClock(4)"></textarea>
    </div>

    <div class="question">
      <h3><b>5.</b> Estudos indicam que bebês com pesos intermediários têm maior chance de sobrevivência. Explique qual o tipo de seleção natural está envolvido nesse exemplo.
        <span id="clock5" class="clock">00:00</span>
      </h3>
      <textarea id="resposta5" name="resposta5" placeholder="Digite sua resposta aqui..." required onfocus="startClock(5)" onblur="stopClock(5)"></textarea>
    </div>

    <div class="question">
      <h3><b>6.</b> Indivíduos com plumagens muito claras ou muito escuras têm maior sobrevivência devido à camuflagem. Explique como a seleção disruptiva pode atuar sobre essa população.
        <span id="clock6" class="clock">00:00</span>
      </h3>
      <textarea id="resposta6" name="resposta6" placeholder="Digite sua resposta aqui..." required onfocus="startClock(6)" onblur="stopClock(6)"></textarea>
    </div>

    <div class="question">
      <h3><b>7.</b> Darwin observou a seleção artificial em pombos e utilizou esse conceito para formular a seleção natural. Explique a relação entre seleção artificial e seleção natural.
        <span id="clock7" class="clock">00:00</span>
      </h3>
      <textarea id="resposta7" name="resposta7" placeholder="Digite sua resposta aqui..." required onfocus="startClock(7)" onblur="stopClock(7)"></textarea>
    </div>

    <div class="question">
      <h3><b>8.</b> O Neodarwinismo integrou os conhecimentos de genética com a teoria de Darwin. Explique como a recombinação genética e as mutações contribuem para a variabilidade das populações.
        <span id="clock8" class="clock">00:00</span>
      </h3>
      <textarea id="resposta8" name="resposta8" placeholder="Digite sua resposta aqui..." required onfocus="startClock(8)" onblur="stopClock(8)"></textarea>
    </div>

    <div class="question">
      <h3><b>9.</b> Explique como a especiação simpátrica pode ocorrer devido a diferenças de hábitos alimentares, mesmo sem separação geográfica.
        <span id="clock9" class="clock">00:00</span>
      </h3>
      <textarea id="resposta9" name="resposta9" placeholder="Digite sua resposta aqui..." required onfocus="startClock(9)" onblur="stopClock(9)"></textarea>
    </div>

    <div class="question">
      <h3><b>10.</b> Durante a pandemia de COVID-19, alguns grupos foram mais resistentes ao vírus. Utilizando o conceito de seleção natural, explique como pandemias podem influenciar a composição genética de uma população.
        <span id="clock10" class="clock">00:00</span>
      </h3>
      <textarea id="resposta10" name="resposta10" placeholder="Digite sua resposta aqui..." required onfocus="startClock(10)" onblur="stopClock(10)"></textarea>
    </div>

    <button type="button" onclick="submitAnswers()">ENVIAR</button>
  </form>

  <script>
    var timers = [];
    var intervals = [];

    // Inicia o cronômetro para uma questão específica
    function startClock(questionNumber) {
      if (!timers[questionNumber]) {
        timers[questionNumber] = 0;
      }
      if (!intervals[questionNumber]) {
        intervals[questionNumber] = setInterval(function() {
          timers[questionNumber]++;
          var minutes = Math.floor(timers[questionNumber] / 60);
          var seconds = timers[questionNumber] % 60;
          document.getElementById('clock' + questionNumber).innerText = ('0' + minutes).slice(-2) + ':' + ('0' + seconds).slice(-2);
        }, 1000);
      }
    }

    // Para o cronômetro da questão
    function stopClock(questionNumber) {
      clearInterval(intervals[questionNumber]);
      intervals[questionNumber] = null;
    }

    // Função para enviar as respostas
    function submitAnswers() {
      var nome = document.getElementById('nome').value;
      var serie = document.getElementById('serie').value;
      var data = document.getElementById('data').value;

      if (!nome || !serie || !data) {
        alert("Por favor, preencha todos os campos obrigatórios.");
        return;
      }

      var respostas = {
        nome: nome,
        serie: serie,
        data: data,
        resposta1: document.getElementById('resposta1').value,
        resposta2: document.getElementById('resposta2').value,
        resposta3: document.getElementById('resposta3').value,
        resposta4: document.getElementById('resposta4').value,
        resposta5: document.getElementById('resposta5').value,
        resposta6: document.getElementById('resposta6').value,
        resposta7: document.getElementById('resposta7').value,
        resposta8: document.getElementById('resposta8').value,
        resposta9: document.getElementById('resposta9').value,
        resposta10: document.getElementById('resposta10').value,
        tempos: timers
      };

      var url = 'https://script.google.com/macros/s/AKfycbzuvA9UgCFYyMJzkkj7tE6fzQ79JzbHvnqeYnHPd2Wubz1q357_j8K8MDybhAZgfNc/exec';
      
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(respostas)
      }).then(function(response) {
        if (!response.ok) {
          throw new Error('Erro ao enviar respostas.');
        }
        return response.json();
      }).then(function(data) {
        var feedback = data.feedback;
        for (var i = 1; i <= feedback.length; i++) {
          var respostaElement = document.getElementById('resposta' + i);
          respostaElement.className = feedback[i - 1];
        }
        alert('Respostas enviadas com sucesso!');
      }).catch(function(error) {
        console.error('Erro:', error);
      });
    }
  </script>
</body>
</html>
