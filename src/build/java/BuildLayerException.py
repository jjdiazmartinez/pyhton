import src.build.shared.SharedTemplate as template
import src.java.util.Package as package
import src.io.ManagerFile as managerfile
class BuildLayerException:
    def buildComponent(self):
        base = template.SharedTemplate().getBase()
        pack = package.Package()
        managerFile = managerfile.ManagerFile()

        templateDataAccesException = template.SharedTemplate().getTemplateDataccesexception()
        templateBusinessLogicException=template.SharedTemplate().getTemplateBusinesslogicexception()
        templateDataManagerException =template.SharedTemplate().getTemplateDatamanagerexception()

        templateDataManagerException = templateDataManagerException.replace("<package>",base["groupId"])
        templateBusinessLogicException = templateBusinessLogicException.replace("<package>", base["groupId"])
        templateDataAccesException = templateDataAccesException.replace("<package>", base["groupId"])

        path = pack.create(base["realpath"], base["groupId"] + ".exception")
        managerFile.write(base["realpath"] + path + "/" + "DataAccesException.java", templateDataAccesException)
        managerFile.write(base["realpath"] + path + "/" + "BusinessLogicException.java", templateBusinessLogicException)
        managerFile.write(base["realpath"] + path + "/" + "DataManagerException.java", templateDataManagerException)

