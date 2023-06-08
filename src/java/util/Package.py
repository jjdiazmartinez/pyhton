import os
#Clase que se usa para trabajar solo el manejo de paquetes para Java

class Package:
    def create(self,path,package):
        values = package.split(".")
        token = [path]
        for item in values:
            token.append("\\" + item)
            if not os.path.exists("".join(token)):
                os.mkdir("".join(token))
        return  package.replace(".","/")
