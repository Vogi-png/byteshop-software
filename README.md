# Byteshop: Loja fictícia de peças eletrônicas

![Status do Projeto](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=for-the-badge)
###
![Tamanho do Repositório](https://img.shields.io/github/repo-size/Vogi-png/byteshop-software?style=for-the-badge)
![Linguagens Utilizadas](https://img.shields.io/github/languages/count/Vogi-png/byteshop-software?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/Vogi-png/byteshop-software?style=for-the-badge)
[![Versão](https://img.shields.io/badge/Versão-0.0-blue?style=for-the-badge)](https://github.com/Vogi-png/byteshop-software/releases)

<br/>

## 📸 Screenshots

<table align="center">
  <tr>
    <td align="center"><strong>Tela de Login</strong></td>
    <td align="center"><strong>Menu Principal</strong></td>
  </tr>
  <tr>
    <td><img src="imagens_exemplo/login.jpg" alt="Tela de Login do ByteShop" width="300"/></td>
    <td><img src="imagens_exemplo/adm_menu.jpg" alt="Menu Principal do Administrador" width="300"/></td>
  </tr>
  <tr>
    <td align="center"><strong>Tabela de Cliente</strong></td>
    <td align="center"><strong>Cadastro de Cliente</strong></td>
  </tr>
  <tr>
    <td><img src="imagens_exemplo/tabela_usuario.jpg" alt="Tabela de Usuário do ByteShop" width="300"/></td>
    <td><img src="imagens_exemplo/form_usuario.jpg" alt="Cadastro de Usuário" width="300"/></td>
  </tr>
</table>


> Este é o repositório do **ByteShop**, um software desenvolvido para uma loja fictícia com o objetivo de gerenciar sua produção e suas operações. O sistema foi criado em Python, com uma interface gráfica projetada no Qt Designer e conectada através da biblioteca PySide6 (ou PyQt).
---

## ✨ Funcionalidades Principais

* 🔐 **Autenticação Segura:** Tela de login para garantir que apenas usuários autorizados acessem o sistema.
* 💻 **Gerenciamento:** Cadastro, edição, exclusão e consulta.
* 🔍 **Busca Inteligente:** Ferramenta de pesquisa em todas as seções para encontrar registros rapidamente.

---

<br/>

## 👩‍💻 Tecnologias Utilizadas
* **Linguagem:** Python
* **IDE:** Visual Studio Code (VS Code)
* **Banco de Dados:** MySQL
* **UI/Layout:** Qt Designer com PySide6
---

<br/>

## 🛠️ Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas para as seguintes tarefas:
### Curto Prazo
- [ ] **Implementar Dashboard de Rendimentos:** Criar uma interface gráfica para que o administrador possa visualizar as métricas de vendas e o faturamento em diferentes períodos (diário, mensal, anual).
- [ ] **Melhorar a Gestão do Banco de Dados:** Implementar um sistema de *migrations* para automatizar e versionar as alterações no esquema do banco de dados, facilitando a instalação e atualização para novos colaboradores.
- [ ] **Refatoração do Código:** Otimizar a estrutura atual do código para melhorar a legibilidade, performance e facilitar a manutenção futura.

### Médio/Longo Prazo
- [ ] **Empacotamento da Aplicação:** Criar um instalador/executável (`.exe` para Windows) para que o sistema possa ser facilmente instalado e utilizado sem a necessidade de ter o Python e as bibliotecas instaladas.
- [ ] **Adicionar Testes Automatizados:** Desenvolver testes unitários e de integração para garantir a estabilidade do sistema e evitar regressões.
---

<br/>

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Python 3.8+

- MySQL Server (recomendado versão 8.x)

- Git

- Pip (gerenciador de pacotes do Python)

Bibliotecas Python necessárias:

- PySide6 (interface gráfica)

- mysql-connector-python (conexão com MySQL)
  
---

<br/>

## 🚀 Instalando Bytecode

Para instalar o Bytecode, siga estas etapas:

### 1. Clonar o Repositório
Abra seu terminal ou Git Bash e execute o seguinte comando para baixar o projeto:
```
git clone https://github.com/Vogi-png/byteshop-software.git
```

---

<br/>

## ☕ Usando Byteshop

Para usar o sitema da empresa fictícia, siga estas etapas:

- Passo 1: Modificando Senha.
###
Edite os arquivos ```conexoes.py``` e ```database_setup.py```, substituindo a senha do banco pela senha que você colocou no seu banco de dados na maquina local.
###
- Passo 2: Criando o Banco de dados.
```
python database_setup.py
```
###
- Passo 3: Iniciando o Sistema
```
python src/main.py
```
---

<br/>

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <img src="https://lh3.googleusercontent.com/pw/AP1GczNyv1lSHv3F74EtX416QlBrjy0E9uUw8SjxUmGRMmtR-VUsBoQ-tvUMSy8tK3nsLFWDzhNQWwxcVl-EKEb0-ouV9WtLDX-DYfh5ZxYKXzOa7AMrXimUhzkBqEYqNiXXjeFSnlXsFJdI1yrklS1K653qPg=w464-h420-s-no-gm?authuser=0" width="100px;" alt="Foto de Giovanna Leal de Araujo"/><br>
      <sub>
        <b>Giovanna Leal de Araujo</b>
      </sub>
    </td>
    <td align="center">
      <img src="https://lh3.googleusercontent.com/pw/AP1GczPcW_MdbOkn9YxciO7qsrlUDlsjPuh9uiH0KAKIkmUtFlIsFjdHqMpGPNkiV5ptpn2Sp4Qr2XbtRnOFrUYbWSyV7jANankmEfkEzCioEfg9CuwfCWT-ynaeRxUvnncLsgqnKfje3WxRV69DCR5OhDLsFQ=w464-h420-s-no-gm?authuser=0" width="100px;" alt="Foto de Guilherme Barreiros Pimentel"/><br>
      <sub>
        <b>Guilherme Barreiros Pimentel</b>
      </sub>
    </td>
    <td align="center">
      <img src="https://lh3.googleusercontent.com/pw/AP1GczMgBVbNuElgfbzLacUZcVlSkMIBaS9D0xYN83iDBkDWC8uPyLxvKq1sKJKSb25ijN2z3Cu9ilb17PBmHFUXVsXlDrZfzM9A5BwBGo54zTJci3pLWhZZvWiFDazsdznTmXQ_6NPK7KrgnMsItB5UcJxz7A=w464-h420-s-no-gm?authuser=0" width="100px;" alt="Foto de Lorenzo Braiener da Cunha"/><br>
      <sub>
        <b>Lorenzo Braiener da Cunha</b>
      </sub>
    </td>
  </tr>
</table>

</table>
