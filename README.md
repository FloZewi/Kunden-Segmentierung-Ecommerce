# Kunden-Segmentierung-Ecommerce

## Projektbeschreibung

Verwenden Sie Kundendaten, um verschiedene Kundensegmente zu identifizieren. Diese Segmente können dann verwendet werden, um gezielte Marketingkampagnen zu entwickeln.

## Funktionen

- Generierung zufälliger Kundendaten
- Speicherung der Kundendaten in einer CSV-Datei
- Durchführung der Kundensegmentierung mit KMeans
- Visualisierung der Kundensegmente

## Installation

1. Klonen Sie das Repository:
    ```bash
    git clone https://github.com/FloZewi/Kundensegmentierung.git
    cd Kundensegmentierung
    ```

2. Erstellen Sie eine virtuelle Umgebung und aktivieren Sie sie:
    ```bash
    python -m venv env
    source env/bin/activate  # Auf Windows: env\Scripts\activate
    ```

3. Installieren Sie die benötigten Pakete:
    ```bash
    pip install pandas scikit-learn matplotlib seaborn
    ```

## Verwendung

1. Führen Sie das Skript zur Generierung der Kundendaten aus:
    ```bash
    python generate_customer_data.py
    ```

2. Das Skript erstellt eine CSV-Datei mit zufälligen Kundendaten im Verzeichnis `data`:
    - `data/customer_data.csv`

3. Führen Sie das Hauptprogramm zur Kundensegmentierung aus:
    ```bash
    python main.py
    ```

## Struktur

- `generate_customer_data.py`: Skript zur Generierung und Speicherung zufälliger Kundendaten.
- `main.py`: Hauptprogramm zur Durchführung der Kundensegmentierung.
- `.gitignore`: Datei zum Ausschließen unnötiger Dateien aus dem Git-Repository.
- `README.md`: Dokumentation des Projekts.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der [LICENSE](LICENSE) Datei.
