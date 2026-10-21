
# Chat em Python

Projeto de chat desenvolvido em Python utilizando o modelo cliente-servidor e comunicação por sockets.

A proposta é explorar conceitos de redes de computadores e comunicação entre aplicações, permitindo que um cliente envie mensagens para um servidor.

# Recursos Utilizados:

- Python
- Sockets
- Comunicação cliente-servidor
- Git e GitHub

# Estrutura do projeto:

- `base.py` — código relacionado ao servidor.
- `cliente.py` — código do cliente que envia mensagens.
- `cliente.spec` — arquivo de configuração associado ao empacotamento do cliente.
- `.gitignore` — arquivos e pastas que não devem ser enviados ao Git.

# Como executar

# 1. Pré-requisitos

- Python instalado.
- 
# 2. Baixe o projeto

```bash
git clone https://github.com/miguelhora0/Chat-em-python.git
```

Entre na pasta do projeto:

```bash
cd Chat-em-python
```

# 3. Inicie o servidor

Abra um terminal e execute:

```bash
python base.py
```

Mantenha o servidor em execução.

### 4. Inicie o cliente

Abra outro terminal na pasta do projeto e execute:

```bash
python cliente.py
```

Se solicitado, informe o endereço IP do servidor. Para testar cliente e servidor no mesmo computador, utilize `127.0.0.1`, desde que o servidor esteja escutando nessa interface.
