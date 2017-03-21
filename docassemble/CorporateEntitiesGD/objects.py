# This is a Python module in which you can write your own Python code,
# if you want to.
#
# Include this module in a docassemble interview by writing:
# ---
# modules:
#   - docassemble.CorporateEntitiesGD.objects
# ---
#
# Then you can do things like:
# ---
# objects:
#   - favorite_fruit: Fruit
# ---
# mandatory: True
# question: |
#   When I eat some ${ favorite_fruit.name },
#   I think, "${ favorite_fruit.eat() }"
# ---
# question: What is the best fruit?
# fields:
#   - Fruit Name: favorite_fruit.name
# ---
#from docassemble.base.core import DAObject
#
#class Fruit(DAObject):
#    def eat(self):
#        return "Yum, that " + self.name + " was good!"

from docassemble.base.util import Organization

class Company(Organization):
    """Represents a corporate entity."""
    def init(self, *pargs, **kwargs):
        #if not hasattr(self, 'name') and 'name' not in kwargs:
        #    self.name = Name()
        # begin custom attributes
        if 'structure' not in kwargs:
            self.structure = 'unincorporated'
            #how do I force it to query for structure?
        # end custom attributes
        return super(Company, self).init(*pargs, **kwargs)

    def longform(self, structure):
        if self.structure is 'LLC':
            return 'Limited Liability Company'
        elif self.structure is 'PLLC':
            return 'Professional Limited Liability Company'
        elif self.structure is 'INC':
            return 'Corporation'
        elif self.structure is 'LP':
            return 'Limited Partnership'
        elif self.structure is 'LLP':
            return 'Limited Liability Partnership'
            else:
                return 'Unknown Structure Type'
