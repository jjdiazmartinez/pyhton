# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import src.build.dto.BuildDto as buildDto
import src.build.shared.SharedTemplate as template
import src.io.ManagerFile as managerfile
import json
def build():
    buld = buildDto.BuildDto()
    managerFile = managerfile.ManagerFile("D:/Areas/tool-python/estructura-py/src/source/resource.json")
    data_structure = managerFile.load()
    templ = template.SharedTemplate()

    structure=json.loads(data_structure)
    for item in structure:
        print(buld.build(structure[item]))



if __name__ == '__main__':
    build()


