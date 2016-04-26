class AdoptionCenter(object):
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = tuple(map(float, location))
    def get_name(self):
        return self.name
    def get_location(self):
        return self.location
    def get_species_count(self):
        return self.species_types.copy()
    def get_number_of_species(self, species_name):
        try:
            return self.species_types[species_name]
        except:
            return 0
    def adopt_pet(self, species_name):
        count = self.get_number_of_species(species_name)
        if count > 0:
            self.species_types[species_name] -= 1
            if count == 1:
                del self.species_types[species_name]
    def __repr__(self):
        return "AdoptionCenter({}, {}, {})".format(self.name, self.species_types, self.location)


class Adopter():
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        return 1.0*adoption_center.get_number_of_species(self.desired_species)


class FlexibleAdopter(Adopter):
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species # list

    def get_score(self, adoption_center):
        sc = adoption_center.get_species_count()
        #return sc[self.desired_species] +  sum(1 for s in self.considered_species if s in sc)*0.3
        return Adopter.get_score(self, adoption_center) + sum(sc[s] for s in self.considered_species if s in sc)*0.3


class FearfulAdopter(Adopter):
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species # str
    def get_score(self, adoption_center):
        score = Adopter.get_score(self, adoption_center) - 0.3*adoption_center.get_number_of_species(self.feared_species)
        return score if score > 0 else 0.0

class AllergicAdopter(Adopter):
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species # list
    def get_score(self, adoption_center):
        sc = adoption_center.get_species_count()
        if any(a in sc for a in self.allergic_species):
            return 0.0
        else:
            return Adopter.get_score(self, adoption_center)

class MedicatedAllergicAdopter(AllergicAdopter):
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness # dictionary

    def get_score(self, adoption_center):
        sc = adoption_center.get_species_count()
        min_eff = 1.0
        for _as in self.allergic_species:
            if _as in sc and self.medicine_effectiveness[_as] < min_eff:
                min_eff = self.medicine_effectiveness[_as]
        return min_eff * Adopter.get_score(self, adoption_center)

import random
class SluggishAdopter(Adopter):
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_linear_distance(self, to_location):
        x1, y1 = self.location
        x2, y2 = to_location
        return ((x1-x2)**2 + (y1-y2)**2)**0.5

    def get_score(self, adoption_center):
        to = adoption_center.get_location()
        distance = self.get_linear_distance(to)
        score = Adopter.get_score(self, adoption_center)

        if distance < 1:
            factor = 1.0
        elif 3 > distance >= 1:
            factor = 0.7 + random.random()*0.2
        elif 5 > distance >= 3:
            factor = 0.5 + random.random()*0.2
        else:
            factor = 0.1 + random.random()*0.4

        return score * factor

# ac = AdoptionCenter('ac', {'Dog':10, 'Cat':20, 'Horse':10}, (1,2))
# j = Adopter('j', 'Cat')
# print j.get_score(ac)

# fa = FlexibleAdopter('fc', 'Dog', ['Cat'])
# print fa.get_score(ac)

# fa = FearfulAdopter('fc', 'Dog', 'Cat')
# print fa.get_score(ac)

# ad = AllergicAdopter('ad', 'Dog', ['Cat'])
# print ad.get_score(ac)

# md = MedicatedAllergicAdopter('md', 'Dog', ['Cat', 'Horse'], {'Cat':1.0, 'Horse':1.0})
# print md.get_score(ac)

# sd = SluggishAdopter('sd', 'Dog', (1, 1))
# print sd.get_linear_distance(ac.get_location())
# print sd.get_score(ac)


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    res = []
    for ac in list_of_adoption_centers:
        res.append([ac, adopter.get_score(ac)])
    sorted_ac = sorted(res, key = lambda x: (-x[1], x[0].get_name()))
    return [x[0] for x in sorted_ac]

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    res = []
    for ad in list_of_adopters:
        score = ad.get_score(adoption_center)
        res.append([ad, score])
    sorted_ad = sorted(res, key = lambda x: (-x[1], x[0].get_name()))
    return [x[0] for x in sorted_ad]
