import csv
import timeit
from custom_csv.reader import CustomCsvReader
from custom_csv.writer import CustomCsvWriter

FILE = "test.csv"

def read_with_csv():
    with open(FILE, newline="", encoding="utf-8") as f:
        list(csv.reader(f))

def read_with_custom():
    reader = CustomCsvReader(FILE)
    list(reader)

def write_with_csv():
    with open("out_csv.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["a", "b", "c", "d", "e"])

def write_with_custom():
    writer = CustomCsvWriter("out_custom.csv")
    writer.write_row(["a", "b", "c", "d", "e"])
    writer.close()

if __name__ == "__main__":
    print("Read Benchmark:")
    print("csv.reader:", timeit.timeit(read_with_csv, number=5))
    print("custom reader:", timeit.timeit(read_with_custom, number=5))

    print("\nWrite Benchmark:")
    print("csv.writer:", timeit.timeit(write_with_csv, number=1000))
    print("custom writer:", timeit.timeit(write_with_custom, number=1000))
