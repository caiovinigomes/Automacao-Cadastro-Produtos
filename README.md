# 🤖 Automação de Cadastro de Produtos com Python
Este projeto automatiza o processo de cadastro de produtos em um sistema web usando Python. Através da biblioteca `pyautogui`, o script simula ações humanas como digitar, clicar e navegar pelo browser, tornando o processo repetitivo muito mais rápido e eficiente.

## 🧩 Funcionalidades
- Abertura automática do navegador
- Acesso ao site com login automático
- Leitura de dados de um arquivo `.csv`
- Preenchimento de formulário web com base nos dados da planilha
- Cadastro automático de diversos produtos

## 🛠️ Tecnologias utilizadas
* **Python 3:** Linguagem de programação principal.
* **PyAutoGUI:** Biblioteca para automação da interface gráfica (controle do mouse e teclado) - (https://pyautogui.readthedocs.io/).
* **Pandas:** Biblioteca para manipulação de dados (leitura do arquivo CSV).
* **Pygetwindow:** Biblioteca para interagir com janelas (maximizar o Chrome, por exemplo).

## 📂 Estrutura do Projeto
- `main.py`: Script principal
- `produtos.csv`: Planilha com os produtos a cadastrar

## ▶️ Como usar
1.  **Instale as dependências:**
    ```bash
    pip install pyautogui pandas pygetwindow
    ```
2.  **Organize os arquivos:** Certifique-se de que `main.py` e `produtos.csv` estejam no mesmo diretório.

3.  **Verifique a URL:** O script interage com uma página web que foi desenvolvida com fins didáticos pela instituição que ministrou o curso. **É importante ressaltar que o site pode não estar mais no ar.**

4.  **Execute o script:**
    ```bash
    python codigo.py
    ```
    **Atenção:** Mantenha o mouse e o teclado livres durante a execução, pois o PyAutoGUI simulará suas ações.

## ▶️ Demonstração
Para uma demonstração da execução do código, você pode assistir ao vídeo:

[Vídeo de Demonstração](https://youtu.be/bJz_GWDKvXg)

> ⚠️ Dica: Teste com poucas linhas na planilha antes de automatizar tudo.

## 📋 Exemplo de produtos.csv
| codigo | marca    | tipo   | categoria | preco_unitario | custo | obs          |
|--------|----------|--------|-----------|----------------|-------|--------------|
| 001    | Marca X  | Mouse  | Periférico| 79.90          | 50.00 | Produto novo |
| 002    | Marca Y  | Teclado| Periférico| 129.90         | 80.00 | Promoção     |

## 📘 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usar e adaptar.