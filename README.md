# Traveling Salesman Problem – Genetski Algoritam

## 1. Opis problema
Problem trgovačkog putnika (TSP) traži najkraću moguću rutu koja posjećuje sve gradove jednom i vraća se na početni.  
Ovaj projekt koristi **genetski algoritam** za pronalazak približno optimalne rute.

## 2. Korišteni algoritmi
- **Tournament selection**: biranje roditelja kroz natjecanje manjih podskupova populacije
- **PMX crossover**: kombinacija roditeljskih rutu u djecu, zadržavajući jedinstvenost gradova
- **Inversion mutation**: mutacija dijela rute obrnutim redoslijedom

pip install -r requirements.txt
## 3. Upute za pokretanje
1. Instalirati Python 3.12+  

2. Kreirati i aktivirati virtualno okruženje te instalirati ovisnosti:

### Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

### Windows
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

> **Napomena:** Ako koristite PowerShell na Windowsu, aktivacija je `venv\Scripts\Activate.ps1`.

Projekt će raditi na oba operativna sustava ako su svi koraci ispravno izvedeni.
