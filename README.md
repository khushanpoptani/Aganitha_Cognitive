# 🧠 Aganitha-Cognitive

## 🚀 Fetch Research Papers from PubMed via Command-Line

**Aganitha-Cognitive** is a **CLI tool** that allows users to fetch research papers from **PubMed** and save them in a CSV file. It is built using **Poetry** for dependency management.

---

## 📌 Features

✔️ **Search for Research Papers** using PubMed API  
✔️ **Save results in CSV format** with detailed metadata  
✔️ **Command-line friendly** with multiple options  
✔️ **Poetry-powered** for easy dependency management  

---

## 📌 Prerequisites

Before installing, ensure that you have:

- **Python 3.9+** installed. Check version:
  ```sh
  python3 --version
  ```
- **Poetry** installed (for package management). Check version:
  ```sh
  poetry --version
  ```
  If Poetry is not installed, install it:
  ```sh
  curl -sSL https://install.python-poetry.org | python3 -
  ```

---

## 📌 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/aganitha-cognitive.git
cd aganitha-cognitive
```

### 2️⃣ Install Dependencies Using Poetry
```sh
poetry install
```

### 3️⃣ Activate Virtual Environment
```sh
poetry shell
```
If `poetry shell` does not work, manually activate the virtual environment:
```sh
source $(poetry env info --path)/bin/activate
```

---

## 📌 Usage

### 🔹 Basic Search & Save Results
```sh
get-papers-list "Cancer Research" -n 5 -f results.csv
```
This will fetch 5 papers related to "Cancer Research" and save them in `results.csv`.

### 🔹 Print Results Instead of Saving
```sh
get-papers-list "AI in Medicine" -n 3
```

### 🔹 Enable Debug Mode
To view detailed logs while fetching:
```sh
get-papers-list "Deep Learning in Healthcare" -d
```

### 🔹 Command-Line Options
| Option             | Short Form | Description                          |
|--------------------|------------|--------------------------------------|
| `--help`           | `-h`       | Show usage instructions              |
| `--file <filename>`| `-f`       | Save results to a CSV file           |
| `--num <count>`    | `-n`       | Number of results to fetch (default: 10) |
| `--debug`          | `-d`       | Enable debugging mode                |

---

## 📌 Troubleshooting

### 1️⃣ Poetry Shell Not Working
Try manually activating the virtual environment:
```sh
source $(poetry env info --path)/bin/activate
```

### 2️⃣ `ModuleNotFoundError: No module named 'fetch_pubmed'`
Ensure the correct project structure is maintained:
```
📂 aganitha_cognitive/
 ├── fetch_pubmed.py
 ├── __init__.py
```
Run:
```sh
poetry install
```

### 3️⃣ `numpy.dtype size changed, may indicate binary incompatibility`
Upgrade NumPy and Pandas:
```sh
poetry run pip install --upgrade numpy pandas
```
Then reinstall dependencies:
```sh
poetry lock clear
poetry install
```

---

## 📌 Uninstallation

If you no longer need the tool, you can remove it:
```sh
cd ..
rm -rf aganitha-cognitive
```
To remove the Poetry virtual environment:
```sh
poetry env remove python
```

---

## 📌 Contact

👨‍💻 **Khushan Poptani**  
📧 **Email**: poptanikhushan@gmail.com  
📍 **GitHub**: Khushan Poptani(https://github.com/khushanpoptani)
