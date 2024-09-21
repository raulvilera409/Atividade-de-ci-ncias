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

        /* Feedback visual de respostas */
        .correto {
            background-color: lightblue;
            color: blue;
        }

        .incorreto {
            background-color: lightcoral;
            color: red;
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

        <!-- Questões Discursivas -->
        <div class="question">
            <h3><b>1.</b> Mudanças climáticas globais têm gerado uma alteração nos habitats de diversas espécies. Explique como o isolamento geográfico pode levar à especiação, considerando o impacto das mudanças climáticas nos ambientes naturais.</h3>
            <textarea id="resposta1" name="resposta1" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>2.</b> Os fósseis indicam que as baleias modernas evoluíram de mamíferos terrestres há milhões de anos. Seus membros anteriores são considerados órgãos homólogos aos membros de outros mamíferos, como os braços humanos. Explique o processo evolutivo que pode ter levado à transformação dos membros anteriores de mamíferos terrestres nos atuais membros das baleias.</h3>
            <textarea id="resposta2" name="resposta2" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>3.</b> O uso indiscriminado de antibióticos tem causado o surgimento de bactérias resistentes a medicamentos, representando um grande desafio à saúde pública global. Explique como o processo de seleção natural pode levar ao desenvolvimento de populações bacterianas resistentes a antibióticos.</h3>
            <textarea id="resposta3" name="resposta3" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>4.</b> Tanto as aves quanto os insetos desenvolveram a capacidade de voar, apesar de não possuírem ancestrais comuns com essa característica. Suas asas são exemplos de órgãos análogos. Defina o conceito de órgãos análogos e explique como eles se relacionam com o processo de evolução convergente.</h3>
            <textarea id="resposta4" name="resposta4" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>5.</b> Estudos indicam que bebês com pesos muito baixos ou muito altos ao nascer têm menor chance de sobreviver em comparação com bebês de peso intermediário. Descreva o tipo de seleção natural envolvido nesse exemplo e explique seu papel na manutenção de certas características em populações humanas.</h3>
            <textarea id="resposta5" name="resposta5" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>6.</b> Em uma população de pássaros, indivíduos com plumagens muito claras ou muito escuras têm maior sobrevivência do que aqueles com plumagem intermediária, devido à sua melhor camuflagem em ambientes distintos. Explique como a seleção disruptiva pode atuar sobre as populações, promovendo a diversificação de características.</h3>
            <textarea id="resposta6" name="resposta6" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>7.</b> Charles Darwin observou que os criadores de pombos selecionavam ativamente os animais com características desejáveis para a reprodução. Explique como a seleção artificial observada por Darwin contribuiu para sua formulação da teoria da seleção natural.</h3>
            <textarea id="resposta7" name="resposta7" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>8.</b> A Teoria Sintética da Evolução, ou Neodarwinismo, integrou a teoria de Darwin com os conhecimentos de genética, como a transmissão de características hereditárias e as mutações. Explique como o Neodarwinismo ampliou a teoria original de Darwin e inclua no seu argumento o papel das mutações e da recombinação genética na variabilidade das populações.</h3>
            <textarea id="resposta8" name="resposta8" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>9.</b> Em um lago, uma população de peixes desenvolveu duas subpopulações com preferências alimentares distintas, levando a um isolamento reprodutivo sem separação geográfica. Explique o conceito de especiação simpátrica.</h3>
            <textarea id="resposta9" name="resposta9" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>10.</b> Durante a pandemia de COVID-19, alguns grupos populacionais apresentaram maior resistência ao vírus. Explique como pandemias podem influenciar a composição genética de uma população.</h3>
            <textarea id="resposta10" name="resposta10" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <button type="button" onclick="submitAnswers()">ENVIAR</button>

    </form>

    <script>
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
            resposta10: document.getElementById('resposta10').value
        };

        var url = 'https://script.google.com/macros/s/AKfycbyylS4M-ckcpYks72HQmIJQrV8zAXej1tgp9vScqLrrMs5gW7S7JDE3ZbWpNtxdbw5E/exec';

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

            alert('Respostas corrigidas!');
        }).catch(function(error) {
            alert('Ocorreu um erro ao enviar as respostas.');
            console.error('Erro:', error);
        });
    }
    </script>

</body>
</html>
