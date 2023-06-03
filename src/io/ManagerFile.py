class ManagerFile:

    def __init__(self,namefile):
        self.namefile = namefile

    def escribir(self,texto):
        with open(self.namefile, "a") as file:
            file.write(texto)
            file.write("I am adding in more lines\n")
            file.write("And more…")

    def load(self):
        with open(self.namefile, encoding="utf-8") as file:
            read_data = file.read()
            file.close()
            return read_data
