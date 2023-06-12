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
            self.templatemapper = managerFile.load("D:/Areas/tool-python/estructura-py/src/template/mapper.template")
            self.templatepersis = managerFile.load("D:/Areas/tool-python/estructura-py/src/template/datapersist.template")
            self.businesslogicexception = managerFile.load("D:/Areas/tool-python/estructura-py/src/template/businesslogicexception.template")
            self.dataccesexception = managerFile.load("D:/Areas/tool-python/estructura-py/src/template/dataccesexception.template")
            self.datamanagerexception = managerFile.load("D:/Areas/tool-python/estructura-py/src/template/datamanagerexception.template")
            self.datapersistinterfaz =managerFile.load("D:/Areas/tool-python/estructura-py/src/template/datapersistinterfaz.template")
            self.managerquery=managerFile.load("D:/Areas/tool-python/estructura-py/src/template/managerquery.template")
            self.responsemessage=managerFile.load("D:/Areas/tool-python/estructura-py/src/template/responsemessage.template")
            self.datamanager=managerFile.load("D:/Areas/tool-python/estructura-py/src/template/datamanager.template")
            self.datamanagerinterfaz = managerFile.load("D:/Areas/tool-python/estructura-py/src/template/datamanagerinterfaz.template")
            self.types = json.loads(self.type_structure)
            #Creo un diccionario
            self.types_own = dict()

        def getTemplateDatamanagerexception(self):
            return self.datamanagerexception
        def getTemplateDataccesexception(self):
            return self.dataccesexception
        def getTemplateBusinesslogicexception(self):
            return self.businesslogicexception
        def getTempleteDto(self):
            return self.templatedto
        def getTempleteMapper(self):
            return self.templatemapper
        def getTemplatePersist(self):
            return self.templatepersis
        def getTemplateDatapersistinterfaz(self):
            return self.datapersistinterfaz
        def getTemplateManagerquery(self):
            return self.managerquery
        def getTemplateResponsemessage(self):
            return self.responsemessage

        def getTemplateDatamanager(self):
            return self.datamanager
        def getTemplateDatamanagerinterfaz(self):
            return self.datamanagerinterfaz
        
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
        def setBase(self,base):
            self.base =base
        def getBase(self):
            return self.base

    instance = None

    def __new__(cls):
        if not SharedTemplate.instance:
            SharedTemplate.instance = SharedTemplate._SharedTemplate()
        return SharedTemplate.instance






