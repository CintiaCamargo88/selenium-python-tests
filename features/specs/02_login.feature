#language: pt
@02_login

Funcionalidade: Efetuar login

Cenario: Efetuar login
    Dado que acesso a pagina de login "https://front.serverest.dev/login"
    Quando preencho o campo email
    E preencho o campo senha
    E pressiono o botao Entrar
    Entao o sistema apresenta a pagina inicial

