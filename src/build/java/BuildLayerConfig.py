import src.build.shared.SharedTemplate as template
import src.java.util.Package as package
import src.io.ManagerFile as managerfile
class BuildLayerConfig:
    def buildComponent(self):
        base = template.SharedTemplate().getBase()
        pack = package.Package()
        managerFile = managerfile.ManagerFile()
        templateManagerQuery = template.SharedTemplate().getTemplateManagerquery()
        templateManagerQuery = templateManagerQuery.replace("<package>", base["groupId"])
        path = pack.create(base["realpath"], base["groupId"] + ".config")

        managerFile.write(base["realpath"] + path + "/" + "ManagerQuery.java", templateManagerQuery)