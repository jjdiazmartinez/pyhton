import json
import src.io.ManagerFile as managerfile

#Implemenacion de un patron singleton
class SharedTemplate(object):
    class _SharedTemplate:
        def __init__(self):
            managerFile = managerfile.ManagerFile()
            self.templatedto = None
            self.listletras = ["A", "B", "C","D"]
            self.type_structure = managerFile.load("D:/Areas/tool-python/estructura-py/src/source/type.json")
            self.templatedto = managerFile.load("D:/Areas/tool-python/estructura-py/src/template/dto.template")
            self.types = json.loads(self.type_structure)
            #Creo un diccionario
            self.types_own = dict()

        def getTempleteDto(self):
            return self.templatedto

        def getTypeStructure(self):
            return self.types
        def setType(self,name,type):
            self.types_own[name]=type
        def setStructure(self,structure):
            self.structure=structure;
        def getStructure(self):
            return self.structure
        def getTypeOun(self):
            return self.types_own
        def getLetras(self,idx):
            return self.listletras[idx]

    instance = None

    def __new__(cls):
        if not SharedTemplate.instance:
            SharedTemplate.instance = SharedTemplate._SharedTemplate()
        return SharedTemplate.instance






