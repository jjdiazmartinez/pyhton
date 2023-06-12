import src.build.shared.SharedTemplate as template
import src.common.UtilDictionary as utildic
class BuildDataManager:
    def build(self, structureJson):
        templ = template.SharedTemplate()
        self.template = templ.getTemplateDatamanager()
        self.types_own = templ.getTypeOun()
        self.structure = structureJson
        self.structuregeneral = templ.getStructure()
        self.doHead()
        self.doImport()
        self.doSaveUpdate()
        return self.template
    def doHead(self):
        base = template.SharedTemplate().getBase()
        self.template = self.template.replace("<package>", base["groupId"] + ".datamanager." + self.structure["name"].lower())
        self.template = self.template.replace("<DTO>", self.structure["name"])
        self.template = self.template.replace("<DTOParam>",self.structure["name"].lower())
        self.template = self.template.replace("<base-package>", base["groupId"])

    def doImport(self):
        base = template.SharedTemplate().getBase()
        token = []
        token.append("import " + base["groupId"] + "." + self.structure["package"] + "." + self.structure["name"] + ";\n")
        token.append("import " + base["groupId"] + ".datamanager." + self.structure["name"].lower() + ".DataManager" + self.structure["name"] + ";\n")
        token.append("import " + base["groupId"] + ".datacces." + self.structure["name"].lower() +"."+self.structure["name"]+ "DataAcces;\n")

        self.template = self.template.replace("<IMPORT>", ''.join(token))
    def doSaveUpdate(self):
        tokenField = []
        listPk = list(utildic.filter_dict_by_attribute(self.structure["attributes"], "pk", "y"))
        tokenField.append("entity.get" + listPk[0]["name"].capitalize() + "()")
        self.template = self.template.replace("<KEY>", "".join(tokenField))