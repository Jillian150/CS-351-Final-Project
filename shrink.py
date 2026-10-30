import csv

# Settings: list your downloaded Goodreads CSV files here
FILES = ["book1-100k.csv", "book100k-200k.csv"]
SIZES = [1000, 10000, 100000, 1000000]

# 1. Read the titles from each file (no duplicates, no empty titles)
titles = []
seen = set()
for filename in FILES:
    with open(filename, encoding="utf-8", errors="ignore") as f:
        for row in csv.DictReader(f):
            name = (row.get("Name") or "").strip()
            if len(name) >= 2 and name.lower() not in seen:
                seen.add(name.lower())
                titles.append(name)
print("Clean books available:", len(titles))

# 2. Save the first N titles for each size (smaller sets sit inside bigger ones)
for n in SIZES:
    if len(titles) >= n:
        with open(f"books_{n}.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Name"])
            for title in titles[:n]:
                writer.writerow([title])
        print("Saved", n)
    else:
        print("Not enough books for", n)

# 3. Fixed search prefixes: first 3 letters of the first 1,000 titles, no repeats
prefixes = []
for title in titles[:1000]:
    p = title.lower()[:3]
    if p not in prefixes:
        prefixes.append(p)
with open("search_prefixes.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(prefixes[:200]))
print("Saved", len(prefixes[:200]), "prefixes")
