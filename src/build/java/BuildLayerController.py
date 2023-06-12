import src.java.util.Package as package
import src.build.shared.SharedTemplate as template
import src.io.ManagerFile as managerfile
import src.build.java.layer.BuildController as buildCon

class BuildLayerController:

    def buildComponent(self, structure):
        pack = package.Package()
        managerFile = managerfile.ManagerFile()
        base = template.SharedTemplate().getBase()
        buildController = buildCon.BuildController()

        for item in structure["entity"]:
            textFile = buildController.build(structure["entity"][item])


            path = pack.create(base["realpath"],base["groupId"] + ".controler." + "." + structure["entity"][item]["name"].lower())
            managerFile.write(base["realpath"] + path + "/" + structure["entity"][item]["name"] + "Controller.java", textFile)

