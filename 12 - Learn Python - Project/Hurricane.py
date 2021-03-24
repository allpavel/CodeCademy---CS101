names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
new_damage = []


def update_damage(list_of_damages):
    for damage in damages:
        if damage == "Damages not recorded":
            new_damage.append(damage)
        elif "B" in damage:
            damage = float(damage.replace("B", "")) * 1000000000
            new_damage.append(int(damage))
        elif "M" in damage:
            damage = float(damage.replace("M", "")) * 1000000
            new_damage.append(int(damage))
    return new_damage


update_damage(damages)
# print(new_damage)

# 2
dict_of_hurricane = {}


def hurricane_list(name, month, year, max_sustained_wind, area_affected, damage, death):
    new_dicts = {name: {"Months": month, "Years": year, "Max Sustained Winds": max_sustained_wind,
                       "Area Affected": area_affected, "Damage": damage, "Deaths": death}
                for name, month, year, max_sustained_wind, area_affected, damage, death
                in list(zip(names, months, years, max_sustained_winds, areas_affected, new_damage, deaths))}
    return dict_of_hurricane.update(new_dicts)


hurricane_list(names, months, years, max_sustained_winds, areas_affected, new_damage, deaths)

# print(dict_of_hurricane)

# 3

new_dict = {}


def years_of_hurricanes(dict_of_hurricanes):
    for key, value in dict_of_hurricanes.items():
        current_year = value["Years"]
        current_cane = {key: value}
        if current_year not in new_dict:
            new_dict[current_year] = [current_cane]
        else:
            new_dict[current_year].append(current_cane)


years_of_hurricanes(dict_of_hurricane)
# print(new_dict)


# 4
new_dict = {}


def counter_of_areas(some_dict):
    for key, value in dict_of_hurricane.items():
        for area in value["Area Affected"]:
            if area in new_dict:
                new_dict[area] += 1
            else:
                new_dict[area] = 1


counter_of_areas(dict_of_hurricane)


# print(new_dict)


# 5
def find_max(another_dict):
    max_val = max(new_dict.values())
    final_max = {k: v for k, v in new_dict.items() if v == max_val}
    return final_max


# print(find_max(new_dict))


# 6
def find_max_death(*args):
    dict_deaths = {}
    for key, value in dict_of_hurricane.items():
        dict_deaths[key] = value["Deaths"]
    max_death_value = max(dict_deaths.values())
    final_max_death_value = {k: v for k, v in dict_deaths.items() if v == max_death_value}
    return final_max_death_value


# print(find_max_death(dict_of_hurricane))

# 7
mortality_dict = {0: [],
                  1: [],
                  2: [],
                  3: [],
                  4: [],
                  5: []}


def mortality_rate(*args):
    for key, value in dict_of_hurricane.items():
        current_mortality = value["Deaths"]
        current_cane = {key: value}
        if 0 < current_mortality < 100:
            mortality_dict[1].append(current_cane)
        elif 100 <= current_mortality < 500:
            mortality_dict[2].append(current_cane)
        elif 500 <= current_mortality < 1000:
            mortality_dict[3].append(current_cane)
        elif 1000 <= current_mortality < 10000:
            mortality_dict[4].append(current_cane)
        elif 10000 <= current_mortality:
            mortality_dict[5].append(current_cane)
        else:
            mortality_dict[0].append(current_cane)


mortality_rate(dict_of_hurricane)


# print(mortality_dict)


# 8 Calculating Hurricane Maximum Damage

def find_max_damage(*args):
    dict_max_damage = {}
    for key, value in dict_of_hurricane.items():
        if value["Damage"] != "Damages not recorded":
            dict_max_damage[key] = value["Damage"]
    max_damage_value = max(dict_max_damage.values())
    final_max_damage_value = {k: v for k, v in dict_max_damage.items() if v == max_damage_value}
    return final_max_damage_value


print(find_max_damage(dict_of_hurricane))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


def rate_damage(*args):
    damage_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key, value in dict_of_hurricane.items():
        current_mortality = value["Damage"]
        current_cane = {key: value}
        if value["Damage"] != "Damages not recorded":
            if 0 < current_mortality < 100000000:
                damage_dict[1].append(current_cane)
            elif 100000000 <= current_mortality < 1000000000:
                damage_dict[2].append(current_cane)
            elif 1000000000 <= current_mortality < 10000000000:
                damage_dict[3].append(current_cane)
            elif 10000000000 <= current_mortality < 50000000000:
                damage_dict[4].append(current_cane)
            elif 50000000000 <= current_mortality:
                damage_dict[5].append(current_cane)
            else:
                damage_dict[0].append(current_cane)
    return damage_dict


print(rate_damage(dict_of_hurricane))