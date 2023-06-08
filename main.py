# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import src.build.shared.SharedTemplate as template
import src.io.ManagerFile as managerfile
import src.build.BuildLayerDto as buildLayDto
import src.build.BuildLayerQuery as buildLayerQ
import json
def build():

    managerFile = managerfile.ManagerFile()
    data_structure = managerFile.load("D:/Areas/tool-python/estructura-py/src/source/resource.json")

    templ = template.SharedTemplate()

    structure=json.loads(data_structure)
    templ.setStructure(structure)

    buildLayerDto = buildLayDto.BuildLayerDto()
    buildLayerQuery= buildLayerQ.BuildLayerQuery()
   # buildLayerDto.buildComponent(structure)
    buildLayerQuery.buildComponent(structure)




if __name__ == '__main__':
    build()


