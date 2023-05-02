# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
def update_damages_func():
  updated_damages = []
  for damage in damages:
    M = 1000000
    B = 1000000000
    if "M" in damage:
      number = float(damage[:-1])
      damage_new = float(number * M)
      updated_damages.append(damage_new)
    elif "B" in damage:
      number = float(damage[:-1])
      damage_new = float(number * B)
      updated_damages.append(damage_new)
    elif damage == "Damages not recorded":
      updated_damages.append(damage)
  return updated_damages

# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
              
# test function by updating damages
updated_damages = update_damages_func()

# 2 
# Create a Table
# Create and view the hurricanes dictionary

#List variable to store hurricane names for dictionary
hurricanes_names = [x for x in names]
#List variable to store values for dictionary 
hurricanes_values = []
#Iterate through each names to add values to hurricanes_values list using the ff format:
for index in range(len(names)):
  hurricanes_values.append({"Name": names[index],
 "Month": months[index],
 "Year": years[index],
 "Max Sustained Wind": max_sustained_winds[index],
 "Areas Affected": areas_affected[index],
 "Damage": updated_damages[index],
 "Deaths": deaths[index]})
#print(hurricanes_values)

#Create a dictionary using the lists: hurricanes_names as key, and hurricanes_values are values
hurricanes = {key:value for key,value in zip(hurricanes_names, hurricanes_values)}
print("Hurricanes Dictionary: \n\t", hurricanes)

# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key

#Write a function that converts the current dictionary of hurricanes to a new dictionary, where they keys are years and the values are lists containing a dictionary for each hurricane that occurred that year
current_cane = {key:value for key, value in zip(years, hurricanes_values)}

print("\n\nHurricanes by Year: \t", current_cane)

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
all_areas = []
for areas in areas_affected:
  for area in areas:
    all_areas.append(area)

hurricane_areas_affected = list(zip(names,areas_affected))

print("\n\nHurricane and Affected Areas: \t", hurricane_areas_affected)

affected_areas_count = {}
for area in all_areas:
  if area not in affected_areas_count:
    affected_areas_count[area] = 1
  elif area in affected_areas_count:
    affected_areas_count[area] += 1    

#Keys are affected areas, values are the counts how many times the areas were affected
print("\n\nAffected areas and counts: ",affected_areas_count) 

# 5 
# Calculating Maximum Hurricane Count
max_area = ""
max_area_count = 0
for area in affected_areas_count:
  count = affected_areas_count.get(area)
  if count > max_area_count:
    max_area_count = count
    max_area = area

# find most frequently affected area and the number of hurricanes involved in
print("\nMost Hit Area: ", max_area, "\nMax Area Count: ", max_area_count)

# 6
# Calculating the Deadliest Hurricane
hurricane_deaths = {key:value for key, value in list(zip(names, deaths))}
print("\nHurricane and deaths: ", hurricane_deaths)

max_mortality_cane = ""
max_mortality = 0
for hurricane in hurricanes:
  count = hurricane_deaths.get(hurricane)
  if count > max_mortality:
    max_mortality = count
    max_mortality_cane = hurricane

# find highest mortality hurricane and the number of deaths
print("\nHurricane: ", max_mortality_cane, "\nMax mortality: ", max_mortality)

# 7
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
# Rating Hurricanes by Mortality
hurricane_mortality_scale_rating = {}
for hurricane in hurricane_deaths:
  toll = hurricane_deaths.get(hurricane)
  if 0 <= toll <=100:
    hurricane_mortality_scale_rating[hurricane] = 1
  elif 101 <= toll <= 500:  
    hurricane_mortality_scale_rating[hurricane] = 2
  elif 501 <= toll <= 1000:
    hurricane_mortality_scale_rating[hurricane] = 3
  elif toll <= 10000:
    hurricane_mortality_scale_rating[hurricane] = 4
  else:
    hurricane_mortality_scale_rating[hurricane] = 5 

# categorize hurricanes in new dictionary with mortality severity as key
print("\nHurricanes with mortality severity ratings: \n\t", hurricane_mortality_scale_rating)

rating_dict0 = []
rating_dict1 = []
rating_dict2 = []
rating_dict3 = []
rating_dict4 = []
rating_dict5 = []

for hurricane in hurricane_mortality_scale_rating:
  if hurricane_mortality_scale_rating.get(hurricane) == 0:
    rating_dict0.append(hurricane)
  elif hurricane_mortality_scale_rating.get(hurricane) == 1:
    rating_dict1.append(hurricane)
  elif hurricane_mortality_scale_rating.get(hurricane) == 2:
    rating_dict2.append(hurricane)
  elif hurricane_mortality_scale_rating.get(hurricane) == 3:
    rating_dict3.append(hurricane)
  elif hurricane_mortality_scale_rating.get(hurricane) == 4:
    rating_dict4.append(hurricane)
  elif hurricane_mortality_scale_rating.get(hurricane) == 5:
    rating_dict5.append(hurricane)

rating_values = rating_dict0, rating_dict1, rating_dict2, rating_dict3, rating_dict4, rating_dict5

rating_keys = [0,1,2,3,4,5]

hurricanes_by_mortality = {key:value for key, value in list(zip(rating_keys, rating_values))}

print("\n\nHurricanes by mortality: ", hurricanes_by_mortality)

# 8 Calculating Hurricane Maximum Damage
hurricane_damages = {key:value for key, value in list(zip(names, updated_damages))}

print("\nHurricane Damages Dictionary: ", hurricane_damages)
# find highest damage inducing hurricane and its total cost
max_damage_hurricane = ""
max_damage = 0
for hurricane in hurricane_damages:
  current_dmg = hurricane_damages.get(hurricane)
  if current_dmg == "Damages not recorded":
    continue
  elif current_dmg >= max_damage:  
    max_damage = current_dmg
    max_damage_hurricane = hurricane
print("\nHurricane with greatest damage: \t", max_damage_hurricane, "\nTotal Damages: ", max_damage) 
  
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000,
                5: 50000000001}

dmg_scale0 = []
dmg_scale1 = []
dmg_scale2 = []
dmg_scale3 = []
dmg_scale4 = [] 
dmg_scale5 = []

hurricane_dmg_scales = {}

for hurricane in hurricane_damages:
  toll = hurricane_damages.get(hurricane)
  if toll == "Damages not recorded":
    hurricane_dmg_scales[hurricane] = 0
  elif 0 <= toll <=100000000:
    hurricane_dmg_scales[hurricane] = 1
  elif 100000000 <= toll <= 1000000000:  
    hurricane_dmg_scales[hurricane] = 2
  elif 1000000000 <= toll <= 10000000000:
    hurricane_dmg_scales[hurricane] = 3
  elif 10000000000 <= toll <= 50000000000:
    hurricane_dmg_scales[hurricane] = 4
  elif toll > 50000000000:
    hurricane_dmg_scales[hurricane] = 5

print("\nHurricane Damage Scales: ", hurricane_dmg_scales)

for hurricane in hurricane_dmg_scales:
  rating_scale = hurricane_dmg_scales.get(hurricane)
  if rating_scale == 0:
    dmg_scale0.append(hurricane)
  elif rating_scale == 1:
    dmg_scale1.append(hurricane)
  elif rating_scale == 2:
    dmg_scale2.append(hurricane)
  elif rating_scale == 3:
    dmg_scale3.append(hurricane)
  elif rating_scale == 4:   
    dmg_scale4.append(hurricane) 
  elif rating_scale == 5:   
    dmg_scale5.append(hurricane)  

# categorize hurricanes in new dictionary with damage severity as key
dmg_scale_values = dmg_scale0, dmg_scale1, dmg_scale2, dmg_scale3, dmg_scale4, dmg_scale5

dmg_scale_rating_key = [0,1,2,3,4,5]

hurricanes_by_damage = {key:value for key, value in list(zip(dmg_scale_rating_key, dmg_scale_values))}

print("\nHurricane Damage Scales by severity: ", hurricanes_by_damage)
