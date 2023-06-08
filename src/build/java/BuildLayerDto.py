import src.build.dto.BuildDto as buildDto
import src.io.ManagerFile as managerfile
import src.java.util.Package as package
import src.build.LayerInterfaz as layerInterfaz
class BuildLayerDto:

    def buildComponent(self,structure):
        bulddto = buildDto.BuildDto()
        pack = package.Package()
        managerFile = managerfile.ManagerFile()
        for item in structure:
            textFile = bulddto.build(structure[item])
            path=pack.create("D:/temp/",structure[item]["package"])
            managerFile.write("D:/temp/"+path+"/"+structure[item]["name"]+".java",textFile)
