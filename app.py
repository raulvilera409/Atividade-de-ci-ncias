<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Atividade Discursiva</title>
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
            height: 150px;
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

        .clock-container {
            font-size: 12px;
            font-weight: bold;
            color: black;
        }

        .question {
            margin-bottom: 20px;
        }

    </style>
</head>
<body>

    <center><h1><b>AVALIAÇÃO DE CIÊNCIAS (3º BIMESTRE)</b></h1></center>

    <form id="discursive-form">

        <!-- Cabeçalho com nome, série e data -->
        <div class="header-inputs">
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" placeholder="Digite seu nome aqui..." required>

            <label for="serie">Série:</label>
            <input type="text" id="serie" name="serie" placeholder="Digite sua série..." required>

            <label for="data">Data:</label>
            <input type="date" id="data" name="data" required>
        </div>

        <!-- Questões Discursivas com Relógio Circular -->
        <div class="question">
            <h3><b>1.</b> Mudanças climáticas globais têm gerado uma alteração nos habitats de diversas espécies. Explique como o isolamento geográfico pode levar à especiação, considerando o impacto das mudanças climáticas nos ambientes naturais.
                <div class="clock-container">
                    Tempo: <span id="clock1">00:00</span>
                </div>
            </h3>
            <textarea id="resposta1" name="resposta1" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>2.</b> Os fósseis indicam que as baleias modernas evoluíram de mamíferos terrestres há milhões de anos. Utilizando o conceito de órgãos homólogos, explique o processo evolutivo.
                <div class="clock-container">
                    Tempo: <span id="clock2">00:00</span>
                </div>
            </h3>
            <textarea id="resposta2" name="resposta2" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>3.</b> O uso indiscriminado de antibióticos tem causado o surgimento de bactérias resistentes. Explique como o processo de seleção natural pode levar ao desenvolvimento de populações bacterianas resistentes.
                <div class="clock-container">
                    Tempo: <span id="clock3">00:00</span>
                </div>
            </h3>
            <textarea id="resposta3" name="resposta3" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>4.</b> Tanto as aves quanto os insetos desenvolveram a capacidade de voar, apesar de não possuírem ancestrais comuns com essa característica. Suas asas são exemplos de órgãos análogos. Explique como eles se relacionam com a evolução convergente.
                <div class="clock-container">
                    Tempo: <span id="clock4">00:00</span>
                </div>
            </h3>
            <textarea id="resposta4" name="resposta4" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>5.</b> Estudos indicam que bebês com pesos muito baixos ou muito altos ao nascer têm menor chance de sobreviver. Explique como a seleção natural pode manter certas características em populações humanas.
                <div class="clock-container">
                    Tempo: <span id="clock5">00:00</span>
                </div>
            </h3>
            <textarea id="resposta5" name="resposta5" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>6.</b> Em uma população de pássaros, indivíduos com plumagens muito claras ou muito escuras têm maior sobrevivência. Explique como a seleção disruptiva pode promover a diversificação de características.
                <div class="clock-container">
                    Tempo: <span id="clock6">00:00</span>
                </div>
            </h3>
            <textarea id="resposta6" name="resposta6" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>7.</b> Charles Darwin observou que os criadores de pombos selecionavam animais com características desejáveis para reprodução. Explique como a seleção artificial observada por Darwin contribuiu para sua teoria da seleção natural.
                <div class="clock-container">
                    Tempo: <span id="clock7">00:00</span>
                </div>
            </h3>
            <textarea id="resposta7" name="resposta7" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>8.</b> A Teoria Sintética da Evolução integrou a teoria de Darwin com conhecimentos de genética. Explique o papel das mutações e da recombinação genética na variabilidade das populações.
                <div class="clock-container">
                    Tempo: <span id="clock8">00:00</span>
                </div>
            </h3>
            <textarea id="resposta8" name="resposta8" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>9.</b> Em um lago, uma população de peixes desenvolveu duas subpopulações com preferências alimentares distintas, levando a isolamento reprodutivo sem separação geográfica. Explique o conceito de especiação simpátrica.
                <div class="clock-container">
                    Tempo: <span id="clock9">00:00</span>
                </div>
            </h3>
            <textarea id="resposta9" name="resposta9" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>10.</b> Durante a pandemia de COVID-19, alguns grupos populacionais apresentaram maior resistência ao vírus. Explique como pandemias podem influenciar a composição genética de uma população.
                <div class="clock-container">
                    Tempo: <span id="clock10">00:00</span>
                </div>
            </h3>
            <textarea id="resposta10" name="resposta10" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <button type="button" onclick="submitAnswers()">ENVIAR</button>

    </form>

    <script>
    var startTimes = {};
    var endTimes = {};

    function startClock(i) {
        if (!startTimes[i]) {
            startTimes[i] = new Date();
        }
    }

    function stopClock(i) {
        if (!endTimes[i]) {
            endTimes[i] = new Date();
            var diff = (endTimes[i] - startTimes[i]) / 1000; // Diferença em segundos
            var minutes = Math.floor(diff / 60);
            var seconds = Math.floor(diff % 60);
            document.getElementById('clock' + i).innerText = ('0' + minutes).slice(-2) + ':' + ('0' + seconds).slice(-2);
        }
    }

    for (var i = 1; i <= 10; i++) {
        document.getElementById('resposta' + i).addEventListener('focus', (function(i) {
            return function() {
                startClock(i);
            };
        })(i));

        document.getElementById('resposta' + i).addEventListener('blur', (function(i) {
            return function() {
                stopClock(i);
            };
        })(i));
    }

    function submitAnswers() {
        var nome = document.getElementById('nome').value;
        var serie = document.getElementById('serie').value;
        var data = document.getElementById('data').value;

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
            tempos: {
                tempo1: document.getElementById('clock1').innerText,
                tempo2: document.getElementById('clock2').innerText,
                tempo3: document.getElementById('clock3').innerText,
                tempo4: document.getElementById('clock4').innerText,
                tempo5: document.getElementById('clock5').innerText,
                tempo6: document.getElementById('clock6').innerText,
                tempo7: document.getElementById('clock7').innerText,
                tempo8: document.getElementById('clock8').innerText,
                tempo9: document.getElementById('clock9').innerText,
                tempo10: document.getElementById('clock10').innerText
            }
        };

        var url = 'var url = 'https://script.google.com/macros/s/AKfycbxGUk3D53X1xWExbWqeenBeO8xFg-0259yjwYl5vQsgqO20xnB3tU_bNk7f2pCIl3c6/exec'; // Substitua pelo seu URL correto';

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(respostas)
        }).then(function(response) {
            return response.json();
        }).then(function(data) {
            var feedback = data.feedback;

            for (var i = 1; i <= feedback.length; i++) {
                var respostaElement = document.getElementById('resposta' + i);
                respostaElement.className = feedback[i - 1];
            }

            alert('Respostas enviadas com sucesso!');
        }).catch(function(error) {
            alert('Ocorreu um erro ao enviar as respostas.');
            console.error('Erro:', error);
        });
    }
    </script>

</body>
</html>
