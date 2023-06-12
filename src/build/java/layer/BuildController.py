import src.build.shared.SharedTemplate as template

class BuildController:
    def build(self, structureJson):
        templ = template.SharedTemplate()
        self.template = templ.getTemplateController()
        self.types_own = templ.getTypeOun()
        self.structure = structureJson
        self.structuregeneral = templ.getStructure()
        self.doHead()
        self.doImport()
        return self.template
    def doHead(self):
        base = template.SharedTemplate().getBase()
        self.template = self.template.replace("<package>", base["groupId"] + ".controler." + self.structure["name"].lower())
        self.template = self.template.replace("<DTO>", self.structure["name"])
        self.template = self.template.replace("<DTOParam>",self.structure["name"].lower())
        self.template = self.template.replace("<base-package>", base["groupId"])

    def doImport(self):
        base = template.SharedTemplate().getBase()
        token = []
        token.append("import " + base["groupId"] + "." + self.structure["package"] + "." + self.structure["name"] + ";\n")
        token.append("import " + base["groupId"] + ".businesslogic." + self.structure["name"].lower() + ".BusinessLogic" +self.structure["name"] + ";\n")

        self.template = self.template.replace("<IMPORT>", ''.join(token))
