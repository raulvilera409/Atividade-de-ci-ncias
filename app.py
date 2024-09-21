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
            height: 150px;
            margin-top: 10px;
            font-size: 14px;
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

        .correto {
            background-color: lightblue;
            color: blue;
        }

        .incorreto {
            background-color: lightcoral;
            color: red;
        }

        .question {
            position: relative;
            margin-bottom: 30px;
        }

        .clock-box {
            position: absolute;
            top: 0;
            right: 0;
            font-size: 14px;
            font-weight: bold;
            background-color: lightgrey;
            border-radius: 5px;
            padding: 5px;
            width: 60px;
            text-align: center;
            margin-left: 10px;
        }

        .question-wrapper {
            display: flex;
            justify-content: space-between;
        }

        .question h3 {
            width: 80%;
        }
    </style>
</head>
<body>

   <center><h1><b>AVALIAÇÃO DE CIÊNCIAS (3º BIMESTRE)</b></h1></center>

    <form id="discursive-form" onsubmit="return verificarRespostas();">

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
            <div class="question-wrapper">
                <h3><b>1.</b> Mudanças climáticas globais têm gerado uma alteração nos habitats de diversas espécies. Explique como o isolamento geográfico pode levar à especiação, considerando o impacto das mudanças climáticas nos ambientes naturais.</h3>
                <div id="clock-box1" class="clock-box">00:00</div>
            </div>
            <textarea id="resposta1" name="resposta1" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <div class="question-wrapper">
                <h3><b>2.</b> Os fósseis indicam que as baleias modernas evoluíram de mamíferos terrestres há milhões de anos. Seus membros anteriores são considerados órgãos homólogos aos membros de outros mamíferos, como os braços humanos. Utilizando o conceito de órgãos homólogos, explique o processo evolutivo que pode ter levado à transformação dos membros anteriores de mamíferos terrestres nos atuais membros das baleias.</h3>
                <div id="clock-box2" class="clock-box">00:00</div>
            </div>
            <textarea id="resposta2" name="resposta2" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <div class="question-wrapper">
                <h3><b>3.</b> O uso indiscriminado de antibióticos tem causado o surgimento de bactérias resistentes a medicamentos, representando um grande desafio à saúde pública global. Esse fenômeno é explicado pela seleção natural. Explique como o processo de seleção natural pode levar ao desenvolvimento de populações bacterianas resistentes a antibióticos.</h3>
                <div id="clock-box3" class="clock-box">00:00</div>
            </div>
            <textarea id="resposta3" name="resposta3" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <div class="question-wrapper">
                <h3><b>4.</b> Tanto as aves quanto os insetos desenvolveram a capacidade de voar, apesar de não possuírem ancestrais comuns com essa característica. Suas asas são exemplos de órgãos análogos. Defina o conceito de órgãos análogos e explique como eles se relacionam com o processo de evolução convergente.</h3>
                <div id="clock-box4" class="clock-box">00:00</div>
            </div>
            <textarea id="resposta4" name="resposta4" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <div class="question-wrapper">
                <h3><b>5.</b> Estudos indicam que bebês com pesos muito baixos ou muito altos ao nascer têm menor chance de sobreviver em comparação com bebês de peso intermediário. Esse fato ilustra um tipo de seleção natural. Descreva o tipo de seleção natural envolvido nesse exemplo e explique seu papel na manutenção de certas características em populações humanas.</h3>
                <div id="clock-box5" class="clock-box">00:00</div>
            </div>
            <textarea id="resposta5" name="resposta5" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>
<div class="question">
            <div class="question-wrapper">
                <h3><b>6.</b> Em uma população de pássaros, indivíduos com plumagens muito claras ou muito escuras têm maior sobrevivência do que aqueles com plumagem intermediária, devido à sua melhor camuflagem em ambientes distintos. Explique como a seleção disruptiva pode atuar sobre as populações, promovendo a diversificação de características.</h3>
                <div id="clock-box6" class="clock-box">00:00</div>
            </div>
            <textarea id="resposta6" name="resposta6" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <div class="question-wrapper">
                <h3><b>7.</b> Charles Darwin observou que os criadores de pombos selecionavam ativamente os animais com características desejáveis para a reprodução. Ele usou essas observações para desenvolver sua teoria da seleção natural. Explique como a seleção artificial observada por Darwin em pombos contribuiu para sua formulação da teoria da seleção natural.</h3>
                <div id="clock-box7" class="clock-box">00:00</div>
            </div>
            <textarea id="resposta7" name="resposta7" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <div class="
        <div class="question-wrapper">
                <h3><b>8.</b> A Teoria Sintética da Evolução, ou Neodarwinismo, integrou a teoria de Darwin com os conhecimentos de genética, como a transmissão de características hereditárias e as mutações. Explique como o Neodarwinismo ampliou a teoria original de Darwin e inclua no seu argumento o papel das mutações e da recombinação genética na variabilidade das populações.</h3>
                <div id="clock-box8" class="clock-box">00:00</div>
            </div>
            <textarea id="resposta8" name="resposta8" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <div class="question-wrapper">
                <h3><b>9.</b> Em um lago, uma população de peixes que antes se alimentava de um único tipo de alimento desenvolveu duas subpopulações com preferências alimentares distintas, levando a um isolamento reprodutivo sem separação geográfica. Defina especiação simpátrica e explique como a diferenciação de hábitos alimentares pode levar à formação de novas espécies dentro de uma mesma área geográfica.</h3>
                <div id="clock-box9" class="clock-box">00:00</div>
            </div>
            <textarea id="resposta9" name="resposta9" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <div class="question">
            <div class="question-wrapper">
                <h3><b>10.</b> Durante a pandemia de COVID-19, alguns grupos populacionais apresentaram maior resistência ao vírus devido a fatores genéticos, imunológicos ou comportamentais, enquanto outros foram mais suscetíveis. Utilizando o conceito de seleção natural, explique como pandemias podem influenciar a composição genética de uma população ao longo do tempo.</h3>
                <div id="clock-box10" class="clock-box">00:00</div>
            </div>
            <textarea id="resposta10" name="resposta10" placeholder="Digite sua resposta aqui..." required></textarea>
        </div>

        <!-- Botão de envio -->
        <button type="submit">Enviar Respostas</button>
    </form>

    <script>
        // Respostas corretas retiradas do Gabarito
        const gabarito = [
            "Isolamento geográfico pode causar especiação pela seleção natural diferenciada.",
            "Órgãos homólogos surgem de um ancestral comum, adaptando-se para diferentes funções.",
            "Seleção natural favorece as bactérias resistentes que sobrevivem ao antibiótico.",
            "Órgãos análogos evoluem de forma independente por adaptação semelhante ao ambiente.",
            "Seleção estabilizadora favorece a sobrevivência de bebês de peso intermediário."
        ];

        function verificarRespostas() {
            const respostasUsuario = [
                document.getElementById('resposta1').value,
                document.getElementById('resposta2').value,
                document.getElementById('resposta3').value,
                document.getElementById('resposta4').value,
                document.getElementById('resposta5').value
            ];

            for (let i = 0; i < gabarito.length; i++) {
                if (respostasUsuario[i].toLowerCase().trim() === gabarito[i].toLowerCase().trim()) {
                    alert(`Questão ${i+1}: Correto!`);
                } else {
                    alert(`Questão ${i+1}: Incorreto. Resposta correta: ${gabarito[i]}`);
                }
            }

            return false; // Impede envio do formulário para permitir verificação
        }
    </script>

</body>
</html>
