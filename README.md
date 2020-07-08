# Connecting Parts
Projeto desenvolvido em Python para a disciplina de Tópicos Especiais em Informática da Fatec Ribeirão Preto

## O que é o Connecting Parts?
É um projeto, que foi desenvolvido em python para a conclusão da disciplina de Tópicos Especiais em Informática, da Fatec de Ribeirão Preto, do curso de Análise e Desenvolvimento de Sistemas.

O software tem como objetivo permitir que os usuários façam cadastrados de livros.
Esses cadastros servirão, posteriormente, para que livros possam ser trocados e emprestados entre os próprios usuários.
A motivação inicial para esse projeto foi, justamente, promover o intercâmbio cultural entre pessoas que se interessam por diferentes tipos de leitura.

## Como usar?
1. Clone ou faça o dowload do projeto para a sua máquina
2. Navegue para a raiz do diretório onde está o projeto
3. Instale e configure os seguintes comandos:
   * pipenv --three
   * pipenv shell
   * pipenv install requests
   * pipenv check
   * pipenv update
   
   * pipenv install flask_migrate
   * pipenv install flask_wtf
   
4. Navegue para a pasta project (se estiver em um ambiente Windows, recomento utilizar o PowerShell)
5. Execute o seguinte comando:
   * $env:FLASK_APP = "project"
   
6. Volte um diretório (cd ..)
7. Execute o seguinte comando:
   * python -m flask run
   
Pronto, seu projeto estará executando no endereço: <b>http://127.0.0.1:5000/</b>
   
Se você quiser também pode alterar a configuração de banco de dados

## Como logar?
Cadastre um novo usuário, ou utilize:
   * User: teste@connecting.com
   * Password: 123456

  

