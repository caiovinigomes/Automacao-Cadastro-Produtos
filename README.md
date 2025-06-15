
# 🤖 Automação de Cadastro de Produtos com Python

Este projeto automatiza o processo de cadastro de produtos em um sistema web utilizando Python. Por meio da biblioteca `PyAutoGUI`, o script simula ações humanas como digitação, cliques e navegação no browser, tornando tarefas repetitivas mais rápidas e eficientes — ideal para sistemas sem API.

## 🧩 Funcionalidades
- Abertura automática do navegador  
- Login automático no sistema  
- Leitura de dados de um arquivo `.csv`  
- Preenchimento automático de formulário web  
- Cadastro em massa de produtos  

## 🛠️ Tecnologias Utilizadas
- **Python 3** – Linguagem de programação principal  
- **PyAutoGUI** – Automação da interface gráfica (mouse e teclado)  
  🔗 [Documentação oficial](https://pyautogui.readthedocs.io/)
- **Pandas** – Manipulação de dados e leitura do CSV  
- **Pygetwindow** – Interação com janelas (ex: maximizar navegador)  

## 📂 Estrutura do Projeto
- `main.py` → Script principal de automação  
- `produtos.csv` → Planilha com os dados dos produtos a serem cadastrados  

## ▶️ Como Usar

1. **Instale as dependências:**
   ```bash
   pip install pyautogui pandas pygetwindow
   ```

2. **Organize os arquivos:**  
   Certifique-se de que `main.py` e `produtos.csv` estejam no mesmo diretório.

3. **Verifique a URL:**  
   O sistema utilizado é uma página web didática fornecida pela instituição do curso.  
   ⚠️ *Ela pode não estar mais disponível online.*

4. **Execute o script:**
   ```bash
   python main.py
   ```
   > ⚠️ **Importante:** Mantenha o mouse e teclado livres durante a execução, pois o PyAutoGUI tomará o controle.

## 🎥 Demonstração
Assista ao vídeo de demonstração para ver a automação funcionando na prática:

🔗 [Clique aqui para assistir](https://youtu.be/bJz_GWDKvXg)

> 💡 *Dica: teste com poucos produtos no início, até se familiarizar com o processo.*

## 📋 Exemplo de `produtos.csv`

| codigo | marca   | tipo     | categoria  | preco_unitario | custo | obs          |
|--------|---------|----------|------------|----------------|--------|--------------|
| 001    | Marca X | Mouse    | Periférico | 79.90          | 50.00  | Produto novo |
| 002    | Marca Y | Teclado  | Periférico | 129.90         | 80.00  | Promoção     |

## 📘 Licença
Este projeto está sob a Licença MIT.  
Sinta-se à vontade para usar, modificar e compartilhar!
