# Gerador de Conselhos

## Descrição
Um site que gera conselhos aleatórios utilizando duas APIs:
1. **Advice Slip API**: Responsável por fornecer conselhos em inglês.
2. **MyMemory API**: Traduz conselhos de inglês para português.

Desenvolvido com **Python**, **Flask**, e **Bootstrap**, oferecendo uma interface simples e responsiva.

---

## Tecnologias Utilizadas
- **Python**: Linguagem principal para lógica do backend.
- **Flask**: Framework usado para gerenciamento de rotas e integração com as APIs.
- **Bootstrap**: Framework CSS para design responsivo e visual moderno.

---

## Funcionalidades
- **Geração de Conselhos**: Consome conselhos aleatórios da Advice Slip API.
- **Tradução**: Utiliza a MyMemory API para traduzir os conselhos para português.
- **Interface Responsiva**: Garantida com Bootstrap, adaptável para diferentes tamanhos de tela.

---

## Instalação e Configuração

### Pré-requisitos
- **Python 3.8+**
- **pip** para gerenciar dependências.
- **Virtualenv** (opcional): Para criar um ambiente virtual.

### Passo a Passo
1. Clone o repositório:
   ```bash
   git clone https://github.com/devMarlos/gerador-de--conselhos.git
   cd gerador-de--conselhos

   
2. Crie um Ambiente Virtual (opcional) Para garantir que as dependências sejam instaladas em um ambiente isolado:
  ```bash
   python -m venv venv
   source venv/bin/activate # Linux/macOS
   venv\Scripts\activate    # Windows
  ```

3. Instale as Dependências Instale as dependências listadas no arquivo :
  ```bash
   pip install -r requirements.txt
  ```

4. Execute o Servidor Flask Inicie o servidor local:
  ```bash
   python app.py
  ```

5. Acesse o Site Abra o navegador e acesse a URL (configurado na porta 8080):
  ```bash
  http://127.0.0.1:8080
  ```

---

## Conclusão

Este projeto demonstra como integrar diferentes APIs para criar uma aplicação web funcional e interativa. Ao utilizar tecnologias como **Python**, **Flask** e **Bootstrap**, foi possível construir um site moderno, responsivo e com funcionalidades práticas, como a geração de conselhos aleatórios e a tradução automática.

---



