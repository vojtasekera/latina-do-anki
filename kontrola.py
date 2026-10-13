import csv
from pathlib import Path

# najdi duplicity a zkontroluj tagy a počet sloupců

def main() -> None:
    csv_path = Path(__file__).resolve().with_name("slovicka.csv")
    rows: list[list[str]] = []

    with csv_path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter = "|")
        rows = list(reader)

    first = set()
    dupes = set()

    for row in rows:
        s = row[0].strip()
        if s in first:
            dupes.add(s)
        else:
            first.add(s)


    print(set(row[2] for row in rows))
    print(dupes)


if __name__ == "__main__":
    main()