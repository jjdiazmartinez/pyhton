import os
class ManagerFile:



    def write(self,namefile,texto):
        with open(namefile, "a",encoding="utf-8") as file:
            token = []
            token.append(texto)
            token.append("\n")
            file.write(''.join(token))
            file.close()

    def load(self,namefile):
        with open(namefile, encoding="utf-8") as file:
            read_data = file.read()
            file.close()
            return read_data

    def createDirectory(self,path):
        if not os.path.exists(path):
            os.mkdir(path)

            
