# Selenium-Python-Tests

Estudos voltados para automação de teste Web com o uso do framework Selenium com linguagem Python. Os exemplos deste repositório são executados no ambiente voltado para testes chamado Severest.

Neste projeto é utilizado:

    Python;
    Selenium;
    Allure report;
    Behave;

Requisitos:

    Java 8
    VisualCode Studio (ou IDE de sua preferência)
    Python v3.12.1
    Node.Js v18.17.1
  
Steps:

    Clone o repositório:

    git clone https://github.com/CintiaCamargo88/selenium-python-tests.git

    Importe na sua IDE de preferência.

    Para instalar as dependências, execute os seguintes comandos no terminal:

    pip install behave
    pip install selenium
    pip install splinter
    pip install allure-behave 
    npm install -g allure-commandline --save-dev

    Para executar a automação, execute o seguinte comando no terminal:

    behave --format allure_behave.formatter:AllureFormatter -o ./allure-results

    Para gerar o relatório, execute o seguinte comando no terminal:

    allure serve allure-results
    
