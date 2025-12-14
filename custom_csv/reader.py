class CustomCsvReader:
    """
    A custom CSV reader implemented from scratch.
    Reads CSV files in a streaming manner.
    """

    def __init__(self, file_path):
        self.file = open(file_path, "r", encoding="utf-8")

    def __iter__(self):
        return self

    def __next__(self):
        row = []
        field = ""
        in_quotes = False

        while True:
            ch = self.file.read(1)

            # End of file
            if ch == "":
                if field or row:
                    row.append(field)
                    return row
                self.file.close()
                raise StopIteration

            if ch == '"':
                if in_quotes:
                    next_char = self.file.read(1)
                    if next_char == '"':
                        field += '"'
                    else:
                        in_quotes = False
                        if next_char:
                            self.file.seek(self.file.tell() - 1)
                else:
                    in_quotes = True

            elif ch == "," and not in_quotes:
                row.append(field)
                field = ""

            elif ch == "\n" and not in_quotes:
                row.append(field)
                return row

            else:
                field += ch
