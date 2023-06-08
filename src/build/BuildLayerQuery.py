
import src.build.dml.BuildQuery as bdqu
import src.io.ManagerFile as managerfile
import src.java.util.Package as package
class BuildLayerQuery:
    def buildComponent(self,structure):
        token=[]
        bdquery = bdqu.BuildQuery()
        pack = package.Package()
        managerFile = managerfile.ManagerFile()
        for item in structure:
            textFile=bdquery.buildSelectForId(structure[item])
            textFileForAll = bdquery.buildSelectForAll(structure[item])
            token.append('"select_'+structure[item]["name"]+'_byid":')
            token.append('"'+textFile+'",')
            token.append('"select_' + structure[item]["name"] + '_forall":')
            token.append('"' + textFileForAll + '",')

        path=pack.create("D:/temp/","sql")
        managerFile.write("D:/temp/"+path+"/sql.json","{"+"".join(token)[0:-1]+"}")