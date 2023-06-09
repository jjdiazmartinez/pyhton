import src.build.shared.SharedTemplate as template
import src.common.UtilDictionary as utildic
class BuildDml:
    def buildInsert(self, structureDto):
        templ = template.SharedTemplate()
        self.structuredto = structureDto
        self.structuregeneral = templ.getStructure()
        values = self.doInsert()
        return "INSERT INTO "+self.structuredto["table"]+" "+values

    def buildUpdate(self, structureDto):
        templ = template.SharedTemplate()
        self.structuredto = structureDto
        self.structuregeneral = templ.getStructure()
        values = self.doUpdate()
        where = self.doWhere()
        return "UPDATE  " + self.structuredto["table"] + " SET " + values+ " "+where
    def buildDelete(self, structureDto):
        templ = template.SharedTemplate()
        self.structuredto = structureDto
        self.structuregeneral = templ.getStructure()
        where = self.doWhere()
        return "DELETE FROM  " + self.structuredto["table"]  + " " + where
    def doInsert(self):
        tokenField=[]
        for item in self.structuredto["attributes"]:
            tokenField.append(item["name"]+",")
        token=[]
        for item in self.structuredto["attributes"]:
            token.append("?,")

        return "("+"".join(tokenField)[0:-1]+") values ("+ "".join(token)[0:-1]+") "

    def doUpdate(self):
        tokenField=[]
        listNoPk = list(utildic.filter_dict_by_attribute(self.structuredto["attributes"], "pk", "n"))
        for item in listNoPk:
            tokenField.append(item["name"]+"=?,")
        return "".join(tokenField)[0:-1]

    def doWhere(self):

        token = []
        listPk = list(utildic.filter_dict_by_attribute(self.structuredto["attributes"], "pk", "y"))
        token.append(listPk[0]["name"] + " = ?")
        return " WHERE "+"".join(token)