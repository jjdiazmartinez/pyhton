# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import src.build.shared.SharedTemplate as template
import src.io.ManagerFile as managerfile
import src.build.java.BuildLayerDto as buildLayDto
import src.build.java.BuildLayerQuery as buildLayerQ
import src.build.java.BuildLayerMapper as buildLayerM
import src.build.java.BuildLayerException as buildLayerEx
import src.build.java.BuildLayerConfig as buildLayerCon
import src.build.java.BuildLayerDatamanager as buildLayerDat
import json
def build():

    managerFile = managerfile.ManagerFile()
    data_structure = managerFile.load("D:/Areas/tool-python/estructura-py/src/source/resource.json")

    templ = template.SharedTemplate()

    structure=json.loads(data_structure)
    templ.setStructure(structure["entity"])
    templ.setBase(structure["base"])
    buildLayerDto = buildLayDto.BuildLayerDto()
    buildLayerMapper  =buildLayerM.BuildLayerMapper()
    buildLayerQuery= buildLayerQ.BuildLayerQuery()
    buildLayerException=buildLayerEx.BuildLayerException()
    buildLayerConfig=buildLayerCon.BuildLayerConfig()
    buildLayerDatamanager=buildLayerDat.BuildLayerDatamanager()

    buildLayerDto.buildComponent(structure)
    buildLayerQuery.buildComponent(structure)
    buildLayerMapper.buildComponent(structure)
    buildLayerException.buildComponent()
    buildLayerConfig.buildComponent()
    buildLayerDatamanager.buildComponent(structure)




if __name__ == '__main__':
    build()


