import src.build.dto.BuildDto as buildDto
import src.build.dml.BuildQuery as bdqu
import src.io.ManagerFile as managerfile
import src.java.util.Package as package
class BuildLayerDto:

    def buildComponent(self,structure):
        bulddto = buildDto.BuildDto()
        bdquery = bdqu.BuildQuery()
        pack = package.Package()
        managerFile = managerfile.ManagerFile()
        for item in structure:
            textFile = bulddto.build(structure[item])
            bdquery.build(structure[item])
            path=pack.create("D:/temp/",structure[item]["package"])
            managerFile.write("D:/temp/"+path+"/"+structure[item]["name"]+".java",textFile)
