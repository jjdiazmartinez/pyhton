import json
import src.io.ManagerFile as managerfile

#Implemenacion de un patron singleton
class SharedTemplate(object):
    class _SharedTemplate:
        def __init__(self):
            self.templatedto = None
            managerTemplete = managerfile.ManagerFile("D:/Areas/tool-python/estructura-py/src/template/dto.template")
            managerType = managerfile.ManagerFile("D:/Areas/tool-python/estructura-py/src/source/type.json")
            self.type_structure = managerType.load()
            self.templatedto = managerTemplete.load()
            self.types = json.loads(self.type_structure)
            #Creo un diccionario
            self.types_own = dict()

        def getTempleteDto(self):
            return self.templatedto

        def getTypeStructure(self):
            return self.types
        def setType(self,name,type):
            self.types_own[name]=type

        def getTypeOun(self):
            return self.types_own

    instance = None

    def __new__(cls):
        if not SharedTemplate.instance:
            SharedTemplate.instance = SharedTemplate._SharedTemplate()
        return SharedTemplate.instance






