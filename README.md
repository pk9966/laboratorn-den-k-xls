# Vyhodnocení laboratorního deníku

Tato aplikace slouží k vyhodnocení laboratorních zkoušek podle zadaného klíče v Excelovém souboru. Vstupními daty je soubor `Klíč.xlsx` obsahující požadovaný počet zkoušek a soubor `Laboratorní deník` s výsledky.

## 📦 Funkce
- Porovnání počtu zkoušek podle zadaného klíče.
- Vyhodnocení "Vyhovující" / "Chybí X zk."
- Možnost stažení aktualizovaného souboru s výsledky.

## 📂 Vstupní soubory
- **Klíč.xlsx** – obsahuje listy:
  - `seznam zkoušek PM+LM OP1`
  - `seznam zkoušek PM+LM OP2`
  - `seznam zkoušek Celý objekt`
  - cílové listy: `PM - OP1`, `LM - OP1`, `PM - OP2`, `LM - OP2`, `Celý objekt`
- **Laboratorní deník** – list s tímto názvem obsahuje výsledky zkoušek.

## 🚀 Spuštění aplikace

```bash
pip install -r requirements.txt
streamlit run app.py
