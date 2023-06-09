import src.java.util.Package as package
import src.io.ManagerFile as managerfile
import src.build.java.layer.BuildMapper as buildMap
import src.build.java.layer.BuildDataAcces as buildDataA
import src.build.java.layer.BuildDataAccesInterfaz as buildDataAccesIn
import src.build.shared.SharedTemplate as template
class BuildLayerMapper:

    def buildComponent(self, structure):
        buildMapper=buildMap.BuildMapper()
        buildDataAcces=buildDataA.BuildDataAcces()
        buildDataAccesInterfaz = buildDataAccesIn.BuildDataAccesInterfaz()
        pack = package.Package()
        managerFile = managerfile.ManagerFile()
        base = template.SharedTemplate().getBase()

        for item in structure["entity"]:

            textFile = buildMapper.build(structure["entity"][item])
            textFileDataAcces = buildDataAcces.build(structure["entity"][item])
            textFileDataAccesInterfaz = buildDataAccesInterfaz.build(structure["entity"][item])

            path = pack.create(base["realpath"], base["groupId"]+".mapper."+ structure["entity"][item]["name"].lower())
            managerFile.write(base["realpath"] + path + "/" + structure["entity"][item]["name"] + "Mapper.java", textFile)

            path = pack.create(base["realpath"], base["groupId"]+".datacces." + structure["entity"][item]["name"].lower())
            managerFile.write(base["realpath"] + path + "/" + structure["entity"][item]["name"] + "DataAccesImpl.java", textFileDataAcces)
            managerFile.write(base["realpath"] + path + "/" + structure["entity"][item]["name"] + "DataAcces.java", textFileDataAccesInterfaz)