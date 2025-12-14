class CustomCsvReader:
    """
    Custom CSV reader implemented from scratch.
    Supports quoted fields, escaped quotes, commas, and embedded newlines.
    Designed for streaming large files.
    """

    def __init__(self, file_path):
        self.file = open(file_path, "r", encoding="utf-8", newline="")

    def __iter__(self):
        return self

    def __next__(self):
        row = []
        field = []
        in_quotes = False

        while True:
            ch = self.file.read(1)

            if ch == "":
                if field or row:
                    row.append("".join(field))
                    return row
                self.file.close()
                raise StopIteration

            if ch == '"':
                if in_quotes:
                    next_char = self.file.read(1)
                    if next_char == '"':
                        field.append('"')
                    else:
                        in_quotes = False
                        if next_char:
                            ch = next_char
                        else:
                            continue
                else:
                    in_quotes = True
                    continue

            if ch == "," and not in_quotes:
                row.append("".join(field))
                field = []

            elif ch == "\n" and not in_quotes:
                row.append("".join(field))
                return row

            else:
                field.append(ch)
