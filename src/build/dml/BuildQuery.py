import src.build.shared.SharedTemplate as template
import src.common.UtilDictionary as utildic
class BuildQuery:
    def buildSelectForId(self, structureDto):
        templ = template.SharedTemplate()
        token=["SELECT "]
        self.structuredto = structureDto
        self.structuregeneral = templ.getStructure()


        selectTest = self.doSelect()
        fromText = self.doFrom()
        whereText =self.doWhere()
        token.append(selectTest)
        token.append("FROM ")
        token.append(fromText )
        token.append("WHERE ")
        token.append(whereText )

        return "".join(token)
    def buildSelectForAll(self, structureDto):
        templ = template.SharedTemplate()
        token=["SELECT "]
        self.structuredto = structureDto
        self.structuregeneral = templ.getStructure()


        selectTest = self.doSelect()
        fromText = self.doFrom()
        whereText =self.doWhere()
        token.append(selectTest)
        token.append("FROM ")
        token.append(fromText )
        return "".join(token)
    def doFrom(self):
        templ = template.SharedTemplate()
        token = []
        idx=0
        aliasParent = templ.getLetras(idx)
        token.append(self.structuredto["table"]+" "+aliasParent+" ")


        #Filtro los atributos que son Fk
        listFk = list(utildic.filter_dict_by_attribute(self.structuredto["attributes"],"foreing-key", "y"))
        for item in listFk:
            token.append(" INNER JOIN ")
            #Con los datos del nombre del FK lo busco en la estructura general
            itemFk = self.structuregeneral[item["foreing"]["name"]]
            idx=idx+1
            alias = templ.getLetras(idx)
            token.append(itemFk["table"] + " " +alias)
            #Busco el campo primario de la entidad Fk
            listPkFk = list(utildic.filter_dict_by_attribute(itemFk["attributes"], "pk", "y"))
            token.append(" ON "+aliasParent+"."+item["name"]+"="+alias+"."+listPkFk[0]["name"]+" ")

        return "".join(token)+" "
    def doSelect(self):
        templ = template.SharedTemplate()
        token = []
        idx = 0
        aliasParent = templ.getLetras(idx)
        for item in self.structuredto["attributes"]:
            token.append(aliasParent + "." + item["name"] +" AS "+aliasParent+"_"+item["name"]+",")

        # Filtro los atributos que son Fk
        listFk = list(utildic.filter_dict_by_attribute(self.structuredto["attributes"], "foreing-key", "y"))
        for item in listFk:
            itemFk = self.structuregeneral[item["foreing"]["name"]]
            idx = idx + 1
            alias = templ.getLetras(idx)
            #Busco los atributos de los FK
            for item in itemFk["attributes"]:
                token.append(alias + "." + item["name"] + " AS " + alias + "_" + item["name"]+",")
        #[0:-1] no toma en cuenta la ultima posicion de la cadena para quitar la ultima coma
        return "".join(token)[0:-1]+" "

    def doWhere(self):
        templ = template.SharedTemplate()
        token = []
        idx = 0
        aliasParent = templ.getLetras(idx)
        listPk = list(utildic.filter_dict_by_attribute(self.structuredto["attributes"], "pk", "y"))
        token.append(aliasParent+"."+listPk[0]["name"] + " = ?")
        return "".join(token)







