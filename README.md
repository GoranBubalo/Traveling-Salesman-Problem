# Traveling Salesman Problem – Genetski Algoritam

## 1. Opis problema
Problem trgovačkog putnika (TSP) traži najkraću moguću rutu koja posjećuje sve gradove jednom i vraća se na početni.  
Ovaj projekt koristi **genetski algoritam** za pronalazak približno optimalne rute.

## 2. Korišteni algoritmi
- **Tournament selection**: biranje roditelja kroz natjecanje manjih podskupova populacije
- **PMX crossover**: kombinacija roditeljskih rutu u djecu, zadržavajući jedinstvenost gradova
- **Inversion mutation**: mutacija dijela rute obrnutim redoslijedom

## 3. Upute za pokretanje
1. Instalirati Python 3.12+  
2. Kreirati virtualno okruženje:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

    Instalirati potrebne biblioteke:

pip install matplotlib

    Pokrenuti projekt:

python3 main.py
