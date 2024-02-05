#language: pt
@04_logout

Funcionalidade: Efetuar logout

Cenario: Efetuar logout
    Dado que entro na url "https://front.serverest.dev/login"
    Quando preencho o email "automacao@teste.com"
    E preencho a senha "123456"
    E pressiono Entrar
    E apresenta a pagina inicial
    Entao aciono logout