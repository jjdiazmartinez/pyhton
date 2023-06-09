import src.build.shared.SharedTemplate as template
import src.common.UtilDictionary as utildic
class BuildDataAcces:
    def build(self, structureJson):
        templ = template.SharedTemplate()
        self.template = templ.getTemplatePersist()
        self.types_own = templ.getTypeOun()
        self.structure = structureJson
        self.structuregeneral = templ.getStructure()
        self.doImport()
        self.doHead()
        self.doInsert()
        self.doUpdate()
        self.doGet()
        self.doDelete()
        return self.template
    def doHead(self):
        base = template.SharedTemplate().getBase()
        self.template = self.template.replace("<package>",base["groupId"]+".datacces."+ self.structure["name"].lower())
        self.template = self.template.replace("<DTO>", self.structure["name"])
        self.template = self.template.replace("<NameClass>", self.structure["name"]+"DataAcces")
        self.template = self.template.replace("<base-package>", base["groupId"] )

    def doImport(self):
        base = template.SharedTemplate().getBase()
        token = []
        token.append("import " + base["groupId"]+"."+self.structure["package"] + "." + self.structure["name"] + ";\n")
        token.append("import "+base["groupId"]+".mapper."+ self.structure["name"].lower()+"." + self.structure["name"] + "Mapper;\n")

        self.template = self.template.replace("<IMPORT>", ''.join(token))
    def doInsert(self):
        tokenField = []
        for item in self.structure["attributes"]:
            tokenField.append("entity.get"+item["name"].capitalize() + "(),")

        self.template = self.template.replace("<INSERT_ID>", "insert_"+self.structure["name"])
        self.template = self.template.replace("<PARAM_INSERT>", "".join(tokenField)[0:-1])
    def doUpdate(self):

        tokenField = []
        listNoPk = list(utildic.filter_dict_by_attribute(self.structure["attributes"], "pk", "n"))
        for item in listNoPk:
            tokenField.append("entity.get"+item["name"].capitalize() + "(),")

       #Se coloca el ultimo campo de filtrado como la pK
        listPk = list(utildic.filter_dict_by_attribute(self.structure["attributes"], "pk", "y"))
        tokenField.append("entity.get"+listPk[0]["name"].capitalize()+ "()")

        self.template = self.template.replace("<UPDATE_ID>", "update_" + self.structure["name"] )
        self.template = self.template.replace("<PARAM_UPDATE>", "".join(tokenField))
    def doGet(self):


        self.template = self.template.replace("<QUERY_GET_ALL>", "select_" + self.structure["name"] + "_forall")
        self.template = self.template.replace("<QUERY_BY_ID>", "select_"+self.structure["name"]+"_byid")
        self.template = self.template.replace("<MAPPER>", self.structure["name"] + "Mapper()")
    def doDelete(self):
        self.template = self.template.replace("<DELETE_ID>", "delete_" + self.structure["name"])
