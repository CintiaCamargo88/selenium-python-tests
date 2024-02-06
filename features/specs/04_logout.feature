#language: pt
@04_logout

Funcionalidade: Efetuar logout

Cenario: Efetuar logout
    Dado que entro na url "https://front.serverest.dev/login"
    Quando preencho o email
    E preencho a senha
    E pressiono Entrar
    E apresenta a pagina inicial
    Entao aciono logout