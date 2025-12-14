import random
from custom_csv.writer import CustomCsvWriter

def generate_data():
    rows = []
    for i in range(10000):
        rows.append([
            f"name {i}",
            f"value, {i}",
            f'quote "inside"',
            f"line1\nline2",
            random.randint(1, 1000)
        ])
    return rows

if __name__ == "__main__":
    writer = CustomCsvWriter("test.csv")
    writer.write_rows(generate_data())
    writer.close()
    print("test.csv generated")
