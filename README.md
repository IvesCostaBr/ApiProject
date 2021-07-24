# ApiProject
Projeto de sstema de delivery



Para entrar no endpoint /user/ -> acesse localhost:8000/users(Todos os verbos HTTP Funcionais)


Sistema de Token 

a url localhost:8000/api/token/ -> gera um access que será o token vai no header da request.
a url localhost:8000/api/token/refresh/ -> você passa como form parameter o refresh token gerado na operação acima, assim você vai conseguir fazer o reset no token de acesso
