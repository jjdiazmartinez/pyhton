
import src.build.dml.BuildQuery as bdqu
import src.build.dml.BuildDml as budml
import src.io.ManagerFile as managerfile
import src.java.util.Package as package
import src.build.shared.SharedTemplate as template
class BuildLayerQuery:
    def buildComponent(self,structure):
        token=[]
        bdquery = bdqu.BuildQuery()
        buildDml=budml.BuildDml()
        pack = package.Package()
        managerFile = managerfile.ManagerFile()
        base = template.SharedTemplate().getBase()
        for item in structure["entity"]:
            textFile=bdquery.buildSelectForId(structure["entity"][item])
            textFileForAll = bdquery.buildSelectForAll(structure["entity"][item])
            textInsert = buildDml.buildInsert(structure["entity"][item])
            textUpdate = buildDml.buildUpdate(structure["entity"][item])
            textDelete = buildDml.buildDelete(structure["entity"][item])
            token.append('"select_'+structure["entity"][item]["name"]+'_byid":')
            token.append('"'+textFile+'",')

            token.append('"select_' + structure["entity"][item]["name"] + '_forall":')
            token.append('"' + textFileForAll + '",')

            token.append('"insert_' + structure["entity"][item]["name"] + '":')
            token.append('"' + textInsert + '",')

            token.append('"update_' + structure["entity"][item]["name"] + '":')
            token.append('"' + textUpdate + '",')

            token.append('"delete_' + structure["entity"][item]["name"] + '":')
            token.append('"' + textDelete + '",')


        managerFile.write(base["resources"]+"/sql.json","{"+"".join(token)[0:-1]+"}")