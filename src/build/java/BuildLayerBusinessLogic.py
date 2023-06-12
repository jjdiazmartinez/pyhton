import src.java.util.Package as package
import src.build.shared.SharedTemplate as template
import src.io.ManagerFile as managerfile
import src.build.java.layer.BuildBusinessLogic as buildBusLogic
import src.build.java.layer.BuildBusinessLogicInterfaz as buildBusLogicInterfaz


class BuildLayerBusinessLogic:
    def buildComponent(self,structure):
        pack = package.Package()
        managerFile = managerfile.ManagerFile()
        base = template.SharedTemplate().getBase()
        buildBusinessLogic=buildBusLogic.BuildBusinessLogic()
        buildBusinessLogicInterfaz=buildBusLogicInterfaz.BuildBusinessLogicInterfaz()

        for item in structure["entity"]:
            textFile = buildBusinessLogic.build(structure["entity"][item])
            textFileInterfaz=buildBusinessLogicInterfaz.build(structure["entity"][item])

            path=pack.create(base["realpath"],base["groupId"]+".businesslogic."+"."+structure["entity"][item]["name"].lower())
            managerFile.write(base["realpath"] + path + "/BusinessLogic" + structure["entity"][item]["name"] + "Impl.java", textFile)

            managerFile.write(base["realpath"] + path + "/BusinessLogic" + structure["entity"][item]["name"] + ".java", textFileInterfaz)


