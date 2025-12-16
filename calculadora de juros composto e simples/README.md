Calculadora de Juros (Simples e Compostos)

Uso rápido:

- Juros compostos (padrão):

```bash
python main.py -m composto -c 1000 -r 5 -t 2 -n 12
```

- Juros simples:

```bash
python main.py -m simples -c 1000 -r 5 -t 2
```

Parâmetros:
- `-m, --modo`: `simples` ou `composto` (padrão: composto)
- `-c, --capital`: capital inicial (float)
- `-r, --taxa`: taxa anual em porcentagem (ex: 5)
- `-t, --tempo`: tempo em anos (float)
- `-n, --periodos`: número de períodos por ano (apenas para composto, padrão 1)

Exemplo de saída:

```
Juros Compostos
Capital inicial: R$ 1.000,00
Taxa anual: 5%
Tempo: 2 anos
Compostos por ano: 12
Montante: R$ 1.104,71
Juros: R$ 104,71
```

Interface web
------------

Criei uma interface web simples para usar a calculadora no navegador: abra o arquivo `index.html` na pasta do projeto (ou use a extensão Live Server do VS Code). A interface usa `script.js` e `style.css` e permite alternar entre juros simples e compostos.

Abrir no PowerShell (na pasta do projeto):

```powershell
start index.html
```

Ou com Live Server abra o endereço mostrado (ex: `http://127.0.0.1:5500`).

Empacotamento (Windows .exe)
--------------------------------

Incluí um `gui.py` com interface `tkinter` e um `build.bat` que usa `PyInstaller` para gerar um executável:

1. Instale o PyInstaller:

```powershell
pip install pyinstaller
```

2. Execute o script de build (na pasta do projeto):

```powershell
build.bat
```

O executável ficará em `dist\calculadora_juros.exe`.

Observação: para criar um executável sem console (janela GUI) o `build.bat` usa a opção `--noconsole`.
