#language: pt
@03_listar_usuario

Funcionalidade: Listar usuario

Cenario: Listar usuario
    Dado que visito a url "https://front.serverest.dev/login"
    Quando insiro o email
    E insiro a senha
    E clico no botão Entrar
    E aciono o botao listar
    Entao o usuario e apresentado na lista
