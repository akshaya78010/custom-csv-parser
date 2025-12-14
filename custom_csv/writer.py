class CustomCsvWriter:
    """
    A custom CSV writer implemented from scratch.
    """

    def __init__(self, file_path):
        self.file = open(file_path, "w", encoding="utf-8")

    def _needs_quotes(self, value):
        return any(ch in value for ch in [",", '"', "\n"])

    def write_row(self, row):
        output = []

        for field in row:
            field = str(field)
            if self._needs_quotes(field):
                field = field.replace('"', '""')
                field = f'"{field}"'
            output.append(field)

        self.file.write(",".join(output) + "\n")

    def write_rows(self, rows):
        for row in rows:
            self.write_row(row)

    def close(self):
        self.file.close()
