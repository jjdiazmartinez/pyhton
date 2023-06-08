#Filtra un diccionario que tiene dentro objetos
# asi como el ejemplo
#aquarium_creatures = [
# {"name": "sammy", "species": "shark", "tank number": "11", "type": "fish"},
# {"name": "ashley", "species": "crab", "tank number": "25", "type": "shellfish"},
# {"name": "jo", "species": "guppy", "tank number": "18", "type": "fish"},
# {"name": "jackie", "species": "lobster", "tank number": "21", "type": "shellfish"},
# {"name": "charlie", "species": "clownfish", "tank number": "12", "type": "fish"},
# {"name": "olly", "species": "green turtle", "tank number": "34", "type": "turtle"}
#]
# lista = list(utildic.filter_dictionary_set(aquarium_creatures,"name", "jackie"))
def filter_dict_by_attribute(aquarium_creatures, attribute,search_string):
	def iterator_func(item):
            if item[attribute]==search_string:
                return True
            return False

	return filter(iterator_func, aquarium_creatures)