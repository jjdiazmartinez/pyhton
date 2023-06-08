
import src.build.dml.BuildQuery as bdqu
import src.build.dml.BuildDml as budml
import src.io.ManagerFile as managerfile
import src.java.util.Package as package
import src.build.LayerInterfaz as layerInterfaz
class BuildLayerQuery:
    def buildComponent(self,structure):
        token=[]
        bdquery = bdqu.BuildQuery()
        buildDml=budml.BuildDml()
        pack = package.Package()
        managerFile = managerfile.ManagerFile()
        for item in structure:
            textFile=bdquery.buildSelectForId(structure[item])
            textFileForAll = bdquery.buildSelectForAll(structure[item])
            textInsert = buildDml.buildInsert(structure[item])
            textUpdate = buildDml.buildUpdate(structure[item])
            token.append('"select_'+structure[item]["name"]+'_byid":')
            token.append('"'+textFile+'",')

            token.append('"select_' + structure[item]["name"] + '_forall":')
            token.append('"' + textFileForAll + '",')

            token.append('"insert_' + structure[item]["name"] + '":')
            token.append('"' + textInsert + '",')

            token.append('"update_' + structure[item]["name"] + '":')
            token.append('"' + textUpdate + '",')

        path=pack.create("D:/temp/","sql")
        managerFile.write("D:/temp/"+path+"/sql.json","{"+"".join(token)[0:-1]+"}")