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
            color: black; /* Cor preta para o texto */
        }

        h1 {
            text-align: center;
            text-shadow: none; /* Remove sombra do título */
            font-weight: normal; /* Sem negrito */
        }

        h3 {
            text-shadow: none; /* Remove sombra dos subtítulos */
            font-weight: normal; /* Sem negrito */
        }

        label, button, textarea {
            text-shadow: none; /* Remove sombra do texto */
            font-weight: normal; /* Sem negrito */
        }

        .header-inputs {
            margin-bottom: 10px;
        }

        input, textarea {
            width: 25%;
            padding: 10px;
            margin-bottom: 40px;
            font-size: 12px;
            color: black; /* Cor preta para o texto */
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
            font-weight: normal; /* Sem negrito */
        }

        button:hover {
            background-color: #45a049;
        }

        .image-container, .chart-container {
            text-align: center;
            margin: 20px 0;
        }

        canvas {
            background-color: white;
            border-radius: 5px;
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
            <h3><b>1.</b> Mudanças climáticas globais têm gerado uma alteração nos habitats de diversas espécies. Como resultado, populações de uma mesma espécie, geograficamente isoladas, podem evoluir de forma diferenciada em resposta às condições ambientais locais. Explique como o isolamento geográfico pode levar à especiação, considerando o impacto das mudanças climáticas nos ambientes naturais.</h3>
            <textarea id="resposta1" name="resposta1" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>2.</b> Os fósseis indicam que as baleias modernas evoluíram de mamíferos terrestres há milhões de anos. Seus membros anteriores são considerados órgãos homólogos aos membros de outros mamíferos, como os braços humanos. Utilizando o conceito de órgãos homólogos, explique o processo evolutivo que pode ter levado à transformação dos membros anteriores de mamíferos terrestres nos atuais membros das baleias.</h3>
            <textarea id="resposta2" name="resposta2" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>3.</b> O uso indiscriminado de antibióticos tem causado o surgimento de bactérias resistentes a medicamentos, representando um grande desafio à saúde pública global. Esse fenômeno é explicado pela seleção natural. Explique como o processo de seleção natural pode levar ao desenvolvimento de populações bacterianas resistentes a antibióticos.</h3>
            <textarea id="resposta3" name="resposta3" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>4.</b> Tanto as aves quanto os insetos desenvolveram a capacidade de voar, apesar de não possuírem ancestrais comuns com essa característica. Suas asas são exemplos de órgãos análogos. Defina o conceito de órgãos análogos e explique como eles se relacionam com o processo de evolução convergente.</h3>
            <textarea id="resposta4" name="resposta4" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>5.</b> Estudos indicam que bebês com pesos muito baixos ou muito altos ao nascer têm menor chance de sobreviver em comparação com bebês de peso intermediário. Esse fato ilustra um tipo de seleção natural. Descreva o tipo de seleção natural envolvido nesse exemplo e explique seu papel na manutenção de certas características em populações humanas.</h3>
            <textarea id="resposta5" name="resposta5" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>6.</b> Em uma população de pássaros, indivíduos com plumagens muito claras ou muito escuras têm maior sobrevivência do que aqueles com plumagem intermediária, devido à sua melhor camuflagem em ambientes distintos. Explique como a seleção disruptiva pode atuar sobre as populações, promovendo a diversificação de características.</h3>
            <textarea id="resposta6" name="resposta6" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>7.</b> Charles Darwin observou que os criadores de pombos selecionavam ativamente os animais com características desejáveis para a reprodução. Ele usou essas observações para desenvolver sua teoria da seleção natural. Explique como a seleção artificial observada por Darwin em pombos contribuiu para sua formulação da teoria da seleção natural.</h3>
            <textarea id="resposta7" name="resposta7" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>8.</b> A Teoria Sintética da Evolução, ou Neodarwinismo, integrou a teoria de Darwin com os conhecimentos de genética, como a transmissão de características hereditárias e as mutações. Explique como o Neodarwinismo ampliou a teoria original de Darwin e inclua no seu argumento o papel das mutações e da recombinação genética na variabilidade das populações.</h3>
            <textarea id="resposta8" name="resposta8" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>9.</b> Em um lago, uma população de peixes que antes se alimentava de um único tipo de alimento desenvolveu duas subpopulações com preferências alimentares distintas, levando a um isolamento reprodutivo sem separação geográfica. Defina especiação simpátrica e explique como a diferenciação de hábitos alimentares pode levar à formação de novas espécies dentro de uma mesma área geográfica.</h3>
            <textarea id="resposta9" name="resposta9" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <h3><b>10.</b> Durante a pandemia de COVID-19, alguns grupos populacionais apresentaram maior resistência ao vírus devido a fatores genéticos, imunológicos ou comportamentais, enquanto outros foram mais suscetíveis. Utilizando o conceito de seleção natural, explique como pandemias podem influenciar a composição genética de uma população ao longo do tempo.</h3>
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

        // ID da planilha do Google
        var spreadsheetId = '16PQkpPICh5hwjIor9HeQ6LRHWiETfmOi_tJpiJ6EQyo';
        var url = `https://script.google.com/macros/s/AKfycbxEgBgzn6fSGP8C9ZVTdWhyXGqd66Kxl5L8bsX4lkEUGefpkmjTqyVgh70CltRM72I/exec`;

        fetch(url, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(respostas)
        }).then(function(response) {
            alert('Respostas enviadas com sucesso!');
        }).catch(function(error) {
            alert('Ocorreu um erro ao enviar as respostas.');
        });
    }
    </script>

</body>
</html>
