import src.build.shared.SharedTemplate as template

class BuildDataAccesInterfaz:
    def build(self, structureJson):
        templ = template.SharedTemplate()
        self.template = templ.getTemplateDatapersistinterfaz()
        self.structure = structureJson

        self.doImport()
        self.doHead()

        return self.template

    def doHead(self):
        base = template.SharedTemplate().getBase()
        self.template = self.template.replace("<package>", base["groupId"] + ".datacces." + self.structure["name"].lower())
        self.template = self.template.replace("<DTO>", self.structure["name"])
        self.template = self.template.replace("<NameClass>", self.structure["name"] + "DataAcces")
        self.template = self.template.replace("<base-package>", base["groupId"])

    def doImport(self):
        base = template.SharedTemplate().getBase()
        token = []
        token.append("import " + base["groupId"] + "." + self.structure["package"] + "." + self.structure["name"] + ";\n")

        self.template = self.template.replace("<IMPORT>", ''.join(token))

