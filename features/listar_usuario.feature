#language: pt
@03_listar_usuario

Funcionalidade: Listar usuario

Cenario: Listar usuario
    Dado que visito a url "https://front.serverest.dev/login"
    Quando insiro o email "automacao@teste.com"
    E insiro a senha "123456"
    E clico no botão Entrar
    E aciono o botao listar
    Entao o usuario "automacao@teste.com" e apresentado na lista
