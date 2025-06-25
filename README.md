# analisador_lexico

## Descrição

Este sistema é um analisador léxico para códigos em Pascal. Ele permite ao usuário enviar um arquivo ou inserir um código de exemplo em Pascal e realiza a análise léxica, identificando e classificando tokens como identificadores, números, strings, operadores, delimitadores e palavras reservadas. O sistema possui interface web moderna e intuitiva.

## Como executar o sistema

Siga o passo a passo abaixo para rodar o analisador léxico em sua máquina:

1. **Clone o repositório ou copie os arquivos para sua máquina.**

2. **(Opcional, mas recomendado) Crie um ambiente virtual Python:**

   > O ambiente virtual é recomendado para isolar as dependências do projeto.  
   > Se você já possui um ambiente virtual criado, basta ativá-lo.  
   > Se for rodar em outra máquina, crie e ative um novo ambiente virtual.

   ```bash
   # Crie o ambiente virtual (apenas uma vez por máquina)
   python -m venv venv

   # Ative o ambiente virtual:
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o sistema:**

   ```bash
   # Normalmente o comando será:
   flask run
   # ou, se o arquivo principal for app.py:
   python app.py
   ```

5. **Acesse no navegador:**

   ```
   http://localhost:5000
   ```

---

**Dica:**  
Sempre ative o ambiente virtual antes de rodar o sistema, especialmente em outra máquina.  
Se for rodar em uma máquina nova, crie e ative o ambiente virtual, depois instale as dependências.

---

## Qualidade do Código

Este projeto segue boas práticas de código Python e é analisado com [pylint](https://pylint.pycqa.org/).

Pontuação atual do pylint:

```
app.py: Your code has been rated at 10/10
analisador.py: Your code has been rated at 9.70/10
```

Para rodar o pylint localmente:

```bash
pylint analisador.py app.py
```
