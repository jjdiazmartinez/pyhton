import src.build.dto.BuildDto as buildDto
import src.io.ManagerFile as managerfile
import src.java.util.Package as package
import src.build.shared.SharedTemplate as template
class BuildLayerDto:

    def buildComponent(self,structure):
        bulddto = buildDto.BuildDto()
        pack = package.Package()
        managerFile = managerfile.ManagerFile()
        base = template.SharedTemplate().getBase()
        for item in structure["entity"]:
            textFile = bulddto.build(structure["entity"][item])
            path=pack.create(base["realpath"],base["groupId"]+"."+structure["entity"][item]["package"])
            managerFile.write(base["realpath"]+path+"/"+structure["entity"][item]["name"]+".java",textFile)
