# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
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

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# print(damages)
# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:

conversion = {"M": 1000000,
              "B": 1000000000}
updated_damages = []

damages_length = len(damages)


def list_to_float(data):
    print('Updating damges data to numeric form')
    for cost in data:
        if cost == 'Damages not recorded':
            updated_damages.append(cost)
        elif cost[-1:] == 'M':
            cost_strip = cost.strip('M')
            cost_float = float(cost_strip) * conversion['M']
            updated_damages.append(cost_float)
        elif cost[-1:] == 'B':
            cost_strip_b = cost.strip('B')
            cost_b_float = float(cost_strip_b) * conversion['B']
            updated_damages.append(cost_b_float)
    if len(data) == len(updated_damages):
        print("Data Updated Succesfully ")
    else:
        print("Some data did not sync corectly")


list_to_float(damages)

length_updated_damages = len(updated_damages)

print("Length of damages data is {}: ".format(damages_length))
print("Length of updated damages data is: {}".format(length_updated_damages))
print('-' * 20)


# write your construct hurricane dictionary function here:

def hurricane_dict(names_list, months_list, years_list, max_sustained_winds_list, areas_affected_list,
                   updated_damages_list, deaths_list):
    hurricanes = {}
    for index in range(len(names_list)):
        hurricanes[names_list[index]] = {
        "Name": names_list[index],
        "Month": months_list[index],
        "Year": years_list[index],
        "Max Sustained Wind": max_sustained_winds_list[index],
        "Areas Affected": areas_affected_list[index],
        "Damages": updated_damages_list[index],
        "Deaths": deaths_list[index]
    }
    print("There are {} Hurricanes in the Hurricane dataset".format(len(hurricanes)))
    return hurricanes


hurricanes = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print('-' * 20)


# write your construct hurricane by year dictionary function here:

def year_of_hurricane(data):
    hurricane_by_year = {}
    for cane in data:
        current_year = data[cane]['Year']
        current_cane = data[cane]
        if current_year not in hurricane_by_year:
            hurricane_by_year[current_year] = [current_cane]
        else:
            hurricane_by_year[current_year].append(current_cane)
    return hurricane_by_year


hurricane_by_year = year_of_hurricane(hurricanes)
print('-' * 20)


# write your count affected areas function here:

def affected_areas(data):
    area_count_dict = {}
    for cane in data:
        current_area = data[cane]['Areas Affected']
        for i in current_area:
            if i not in area_count_dict:
                area_count_dict[i] = 1
            else:
                area_count_dict[i] += 1
    return area_count_dict


affected_areas_count = affected_areas(hurricanes)
print(affected_areas_count)
print('-' * 20)


# write your find most affected area function here:

def most_hit_areas(data):
    max_area = 'Yucatn Peninsula'
    max_area_count = 0
    for area in data:
        if data[area] > max_area_count:
            max_area_count = data[area]
            max_area = area

    return print("The most affected area was {0} with {1} recorded hurricanes affecting the area".format(max_area,
                                                                                                         max_area_count))


most_hit_areas(affected_areas_count)

print('-' * 20)


# write your greatest number of deaths function here:

def most_deaths_cane(data):
    max_mortality_cane = 'Cuba I'
    max_mortality = 0
    for area in data:
        if data[area]['Deaths'] > max_mortality:
            max_mortality_cane = area
            max_mortality = data[area]['Deaths']

    return print(
        "The most deaths by hurricane was {0} with {1} recorded deaths from hurricanes".format(max_mortality_cane,
                                                                                               max_mortality))


most_deaths_cane(hurricanes)

print('-' * 20)
# write your catgeorize by mortality function here:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
hurricane_mortality_ratings = {}


def cat_cane_by_mortality_rating(data):
    hurricane_mortality_ratings[0] = []
    hurricane_mortality_ratings[1] = []
    hurricane_mortality_ratings[2] = []
    hurricane_mortality_ratings[3] = []
    hurricane_mortality_ratings[4] = []

    for cane in data:
        if data[cane]['Deaths'] < 100:
            hurricane_mortality_ratings[0].append(cane)
        elif data[cane]['Deaths'] < 500:
            hurricane_mortality_ratings[1].append(cane)
        elif data[cane]['Deaths'] < 1000:
            hurricane_mortality_ratings[2].append(cane)
        elif data[cane]['Deaths'] < 10000:
            hurricane_mortality_ratings[3].append(cane)
        else:
            hurricane_mortality_ratings[4].append(cane)
    return hurricane_mortality_ratings


cane_mortality_rating = cat_cane_by_mortality_rating(hurricanes)

print(cane_mortality_rating)
print('There are {0} Hurricanes catgorozed as ahaving a mortalitiy rating of 0: \n{1}'.format(
    len(cane_mortality_rating[0]), cane_mortality_rating[0]))
print('-' * 10)
print('There are {0} Hurricanes catgorozed as ahaving a mortalitiy rating of 1: \n{1}'.format(
    len(cane_mortality_rating[1]), cane_mortality_rating[1]))
print('-' * 10)
print('There are {0} Hurricanes catgorozed as ahaving a mortalitiy rating of 2: \n{1}'.format(
    len(cane_mortality_rating[2]), cane_mortality_rating[2]))
print('-' * 10)
print('There are {0} Hurricanes catgorozed as ahaving a mortalitiy rating of 3: \n{1}'.format(
    len(cane_mortality_rating[3]), cane_mortality_rating[3]))
print('-' * 10)
print('There are {0} Hurricanes catgorozed as ahaving a mortalitiy rating of 4: \n{1}'.format(
    len(cane_mortality_rating[4]), cane_mortality_rating[4]))
print('-' * 20)

# write your greatest damage function here:
float_damages = []


def most_damage_cane(cane, damages):
    max_cane = ''
    max_damages = 0

    cane_damages = {}
    # Strip text from Damages
    for damage in damages:
        if damage == 'Damages not recorded':
            new_damage = 0
            float_damages.append(new_damage)
        else:
            float_damages.append(damage)

    for index in range(len(cane)): cane_damages[names[index]] = float_damages[index]

    print("Hurricanes and damages caused:")
    print(cane_damages)

    # Find most damage and cane
    for cane in cane_damages:
        if cane_damages[cane] > max_damages:
            max_damages = cane_damages[cane]
            max_cane = cane
    print("-" * 20)
    print("The Hurricane that caused the most damage was Hurricane {0} with ${1} of damages recorded".format(max_cane,
                                                                                                             max_damages))


most_damage_cane(names, updated_damages)

# write your catgeorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


def cat_cane_by_damage_rating(data):
    hurricane_damage_ratings = {0: [], 1: [], 2: [], 3: [], 4: []}

    for cane in data:
        if data[cane]['Damages'] == 'Damages not recorded':
            hurricane_damage_ratings[0].append(cane)
        elif data[cane]['Damages'] < damage_scale[1]:
            hurricane_damage_ratings[1].append(cane)
        elif data[cane]['Damages'] < damage_scale[2]:
            hurricane_damage_ratings[2].append(cane)
        elif data[cane]['Damages'] < damage_scale[3]:
            hurricane_damage_ratings[3].append(cane)
        else:
            hurricane_damage_ratings[4].append(cane)
    print(hurricane_damage_ratings)
    return hurricane_damage_ratings


cane_damage_rating = cat_cane_by_damage_rating(hurricanes)

print('There are {0} Hurricanes catgorozed as ahaving a damage rating of 0: \n{1}'.format(len(cane_damage_rating[0]),
                                                                                          cane_damage_rating[0]))
print('-' * 10)
print('There are {0} Hurricanes catgorozed as ahaving a damage rating of 1: \n{1}'.format(len(cane_damage_rating[1]),
                                                                                          cane_damage_rating[1]))
print('-' * 10)
print('There are {0} Hurricanes catgorozed as ahaving a damage rating of 2: \n{1}'.format(len(cane_damage_rating[2]),
                                                                                          cane_damage_rating[2]))
print('-' * 10)
print('There are {0} Hurricanes catgorozed as having a damage rating of 3: \n{1}'.format(len(cane_damage_rating[3]),
                                                                                         cane_damage_rating[3]))
print('-' * 10)
print('There are {0} Hurricanes catgorozed as ahaving a damage rating of 4: \n{1}'.format(len(cane_damage_rating[4]),
                                                                                          cane_damage_rating[4]))
print('-' * 20)
