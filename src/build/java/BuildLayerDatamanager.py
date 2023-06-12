import src.io.ManagerFile as managerfile
import src.java.util.Package as package
import src.build.shared.SharedTemplate as template
import src.build.java.layer.BuildDataManager as BuildDataM
import src.build.java.layer.BuildDataManagerInterfaz as BuildDataManagerIn
class BuildLayerDatamanager:
    def buildComponent(self,structure):
        buildDataManager=BuildDataM.BuildDataManager()
        buildDataManagerInterfaz=BuildDataManagerIn.BuildDataManagerInterfaz()
        pack = package.Package()
        managerFile = managerfile.ManagerFile()
        base = template.SharedTemplate().getBase()

        for item in structure["entity"]:
            textFile = buildDataManager.build(structure["entity"][item])
            textFileInterfaz=buildDataManagerInterfaz.build(structure["entity"][item])

            path=pack.create(base["realpath"],base["groupId"]+".datamanager."+"."+structure["entity"][item]["name"].lower())
            managerFile.write(base["realpath"] + path + "/DataManager" + structure["entity"][item]["name"] + "Impl.java", textFile)

            managerFile.write(base["realpath"] + path + "/DataManager" + structure["entity"][item]["name"] + ".java", textFileInterfaz)

