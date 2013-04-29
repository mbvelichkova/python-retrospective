class Person:

    def __init__(self, name, gender, birth_year, father=None, mother=None):
        self.name, self.gender, self.birth_year = name, gender, birth_year
        self.children_list = []

        self.father = father
        if father:
            father.set_child(self)
        self.mother = mother
        if mother:
            mother.set_child(self)

    def get_brothers(self):
        return self.__get_silbling('M')

    def get_sisters(self):
        return self.__get_silbling('F')

    def children(self, gender=None):
        if gender:
            return [child for child in self.children_list
                                    if child.gender == gender]
        else:
            return self.children_list

    def set_child(self, child):
        self.children_list.append(child)

    def is_direct_successor(self, child):
        if child in self.children_list:
            return True
        else:
            return False

    def gender(self):
        return self.gender

    def __get_silbling(self, gender=None):
        siblings_mother_side = self.mother.children(gender)
        siblings_father_side = self.father.children(gender)

        siblings = set(siblings_mother_side + siblings_father_side)
        if self in siblings:
            siblings.remove(self)

        return list(siblings)
