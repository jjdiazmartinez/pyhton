import src.java.util.Package as package
import src.io.ManagerFile as managerfile
import src.build.java.layer.BuildMapper as buildMap
import src.build.java.layer.BuildDataAcces as buildDataA
class BuildLayerMapper:

    def buildComponent(self, structure):
        buildMapper=buildMap.BuildMapper()
        buildDataAcces=buildDataA.BuildDataAcces()
        pack = package.Package()
        managerFile = managerfile.ManagerFile()

        for item in structure:

            textFile = buildMapper.build(structure[item])
            textFileDataAcces = buildDataAcces.build(structure[item])

            path = pack.create("D:/temp/", "mapper."+ structure[item]["name"].lower())
            managerFile.write("D:/temp/" + path + "/" + structure[item]["name"] + "Mapper.java", textFile)

            path = pack.create("D:/temp/", "datacces." + structure[item]["name"].lower())
            managerFile.write("D:/temp/" + path + "/" + structure[item]["name"] + "DataAccesImpl.java", textFileDataAcces)