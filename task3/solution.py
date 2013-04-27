class Person:

    def __init__(self, name, gender, birth_year, father=None, mother=None):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.father = father
        self.children_list = []
        if father:
            father.set_child(self)
        self.mother = mother
        if mother:
            mother.set_child(self)

    def get_brothers(self):
        brothers_from_mother = self.__get_parents_children(self.mother, 'M')
        brothers_from_father = self.__get_parents_children(self.father, 'M')
        brothers = set(brothers_from_mother + brothers_from_father)
        if self in brothers:
            brothers.remove(self)
        return list(brothers)

    def get_sisters(self):
        sisters_from_mother = self.__get_parents_children(self.mother, 'F')
        sisters_from_father = self.__get_parents_children(self.father, 'F')
        sisters = set(sisters_from_mother + sisters_from_father)
        if self in sisters:
            sisters.remove(self)
        return list(sisters)

    def children(self, gender='M/F'):
        if gender == 'M/F':
            return self.children_list
        else:
            return [child for child in self.children_list
                                    if child.gender == gender]

    def set_child(self, child):
        self.children_list.append(child)

    def is_direct_successor(self, child):
        if child in self.children_list:
            return True
        else:
            return False

    def gender(self):
        return self.gender

    def __get_parents_children(self, parent, gender):
        if parent:
            return parent.children(gender)
        else:
            return []