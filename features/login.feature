#language: pt
@02_login

Funcionalidade: Efetuar login

Cenario: Efetuar login
    Dado que abro a url "https://front.serverest.dev/login"
    Quando preencho o campo email "automacao@teste.com"
    E preencho o campo senha "123456"
    E pressiono o botão Entrar
    Entao o sistema apresenta a pagina inicial

