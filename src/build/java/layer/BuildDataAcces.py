import src.build.shared.SharedTemplate as template
import src.common.UtilDictionary as utildic
class BuildDataAcces:
    def build(self, structureJson):
        templ = template.SharedTemplate()
        self.template = templ.getTemplatePersist()
        self.types_own = templ.getTypeOun()
        self.structure = structureJson
        self.structuregeneral = templ.getStructure()

        self.doHead()
        return self.template
    def doHead(self):

        self.template = self.template.replace("<package>","datacces."+ self.structure["name"].lower())
        self.template = self.template.replace("<DTO>", self.structure["name"])
        self.template = self.template.replace("<NameClass>", self.structure["name"]+"DataAcces")