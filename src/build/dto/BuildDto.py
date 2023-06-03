import json
import src.build.shared.SharedTemplate as template
class BuildDto:

    def build(self,structureJson):

        templ = template.SharedTemplate()
        self.template=templ.getTempleteDto()
        self.types_own =templ.getTypeOun()
        self.structure=structureJson

        self.types=templ.getTypeStructure()
        self.doPackage()
        self.doImport()
        self.doName()
        self.buildAttribute()
        self.doSet()
        self.doGet()
        #Almaceno los type propios que se van creando
        templ.setType(self.structure["name"],self.structure["package"]+"."+self.structure["name"])
        return self.template

    def doPackage(self):
        self.template=self.template.replace("<package>",self.structure["package"])
    def doName(self):
        self.template = self.template.replace("<name>", self.structure["name"])
    def buildAttribute(self):

        token = []
        for item in self.structure["attributes"]:
            token.append("private "+item["type"]+" "+item["name"]+";\n")

        self.template = self.template.replace("<atribute>", '\t'.join(token))



    def doImport(self):
        token=[]
        for item in self.structure["attributes"]:
            try:
                if  self.types["types"][item["type"]]!="":
                    token.append("import "+self.types["types"][item["type"]]+";\n")
            except KeyError:
                print('Clave no encontrada')

        for item in self.structure["attributes"]:
            try:
                token.append("import " + self.types_own[item["type"]] + ";\n")
            except KeyError:
                print('Clave no encontrada')

        self.template = self.template.replace("<import>", ''.join(token))

    def doSet(self):
        token = []
        for item in self.structure["attributes"]:
            token.append("public void set" + item["name"].capitalize() + "("+item["type"]+" "+item["name"]+")  {\n")
            token.append("\t\t this."+item["name"]+"="+item["name"]+";\n")
            token.append("}\n")

        self.template = self.template.replace("<body-set>", '\t'.join(token))
    def doGet(self):
        token = []
        for item in self.structure["attributes"]:
            token.append("public " + item["type"] + " get" + item["name"].capitalize() + "()  {\n")
            token.append("\t\t return this." + item["name"] +";\n")
            token.append("}\n")
        self.template = self.template.replace("<body-get>", '\t'.join(token))