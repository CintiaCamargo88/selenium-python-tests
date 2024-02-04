#language: pt
@01_cadastro_usuario

Funcionalidade: Efetuar cadastro

Cenario: Testes de cadastro
    Dado que acesso a url "https://front.serverest.dev/login"
    Quando aciono o link de cadastro
    E informo o campo nome "Automação"
    E informo o campo email "automacao@teste.com"
    E informo o campo senha "123456"
    E seleciono o check Cadastrar como administrador
    E aciono o botão Cadastrar
    Entao o sistema apresenta as boas vindas para "Automação"

