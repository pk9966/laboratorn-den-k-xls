# Vyhodnocení laboratorního deníku

Tato aplikace slouží k automatickému vyhodnocení zkoušek zhotovitele podle zadaného klíče. Pracuje výhradně s daty uloženými v Excelových souborech.

## 📦 Funkce
- Načtení vstupních dat z listu **Evidence zkoušek zhotovitele**
- Porovnání skutečně provedených zkoušek s požadovaným počtem podle klíče
- Vyhodnocení výsledků ve formátu "Vyhovující" nebo "Chybí X zk."
- Možnost stažení aktualizovaného souboru s výsledky

## 📂 Vstupní soubor
- **Klíč.xlsx** s listy:
  - `Evidence zkoušek zhotovitele` – výstupní list se záznamy provedených zkoušek
  - `seznam zkoušek PM+LM OP1` – klíč pro části OP1
  - `seznam zkoušek PM+LM OP2` – klíč pro části OP2
  - `seznam zkoušek Celý objekt` – klíč pro obecné vyhodnocení
  - cílové listy: `PM - OP1`, `LM - OP1`, `PM - OP2`, `LM - OP2`, `Celý objekt`

## 🚀 Spuštění

```bash
pip install -r requirements.txt
streamlit run app.py
