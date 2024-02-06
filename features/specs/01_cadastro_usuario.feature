#language: pt
@01_cadastro_usuario

Funcionalidade: Efetuar cadastro

Cenario: Testes de cadastro
    Dado que acesso a url "https://front.serverest.dev/login"
    Quando aciono o link de cadastro
    E informo o campo nome
    E informo o campo email
    E informo o campo senha
    E seleciono o check Cadastrar como administrador
    E aciono o botao Cadastrar
    Entao o sistema apresenta as boas vindas para o usuario

