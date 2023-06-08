import src.build.shared.SharedTemplate as template
import src.common.UtilDictionary as utildic
class BuildMapper:
    def build(self, structureJson):
        templ = template.SharedTemplate()
        self.template = templ.getTempleteMapper()
        self.types_own = templ.getTypeOun()
        self.types = templ.getTypeStructure()
        self.structure = structureJson
        self.structuregeneral = templ.getStructure()
        self.doHead()
        self.doImport()
        self.doSet()
        return self.template

    def doHead(self):

        self.template = self.template.replace("<package>","mapper."+ self.structure["name"].lower())
        self.template = self.template.replace("<DTO>", self.structure["name"])
        self.template = self.template.replace("<Name>", self.structure["name"])

    def doImport(self):
        token = []
        token.append("import " + self.structure["package"]+"."+self.structure["name"] + ";\n")
        for item in self.structure["attributes"]:
            try:
                if item["foreing-key"] == 'y':
                    token.append("import " + self.types_own[self.getFk(item)["name"]] + ";\n")
                else:
                    token.append("import " + self.types_own[item["type"]] + ";\n")

            except KeyError:
                print('Clave no encontrada')

        self.template = self.template.replace("<import>", ''.join(token))

    #Metodo que arma todos los set del Mapper
    def doSet(self):
        templ = template.SharedTemplate()
        token = []
        idx = 0
        aliasParent = templ.getLetras(idx)
        for item in self.structure["attributes"]:
            token.append("\t entity.set" + item["name"].capitalize() + " (resultSet.get"+self.types["types-bd"][item["type"]]+"(\""+aliasParent + "_" + item["name"]+"\")); \n")

        # Filtro los atributos que son Fk
        listFk = list(utildic.filter_dict_by_attribute(self.structure["attributes"], "foreing-key", "y"))
        for item in listFk:
            itemFk = self.structuregeneral[item["foreing"]["name"]]
            idx = idx + 1
            alias = templ.getLetras(idx)
            #Se instancian las clases foraneas
            token.append("\n\t"+itemFk["name"]+" "+alias+itemFk["name"].lower()+"= new "+itemFk["name"]+"();\n")
            # Busco los atributos de los FK
            for item in itemFk["attributes"]:
                token.append("\t"+alias+itemFk["name"].lower()+".set" + item["name"].capitalize() + " (resultSet.get"+self.types["types-bd"][item["type"]]+"(\"" + alias + "_" + item["name"] + "\"));\n ")
            token.append("\tentity.set" +itemFk["name"].capitalize()+"("+alias+itemFk["name"].lower()+")\n\n")
        self.template = self.template.replace("<body-set-entity>", '\t'.join(token))
    # Retorna el objeto Foreing Key
    def getFk(self, item):
        return self.structuregeneral[item["foreing"]["name"]]