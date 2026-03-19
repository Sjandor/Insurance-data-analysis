# import the csv library
import csv

# empty lists for analysis
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

# getting the lists and loading them
def load_list_data(lst, csv_file, column_name):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst

load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


# Analysis time

# average ages
def average_age(ages):
    total_ages = 0
    for age in ages:
        total_ages += int(age)   # convert to int
    return total_ages / len(ages)


# more men or more women?
def sexes_count(sexes):
    men = 0
    women = 0
    for sex in sexes:
        if sex == 'male':
            men += 1
        else:
            women += 1
    return men, women


# yearly average cost
def average_cost(insurance_charges):
    total_cost = 0
    for cost in insurance_charges:
        total_cost += float(cost)   # convert to float
    return total_cost / len(insurance_charges)

# How many people per region?
def regions_count(regions):
    northwest = 0
    southwest = 0
    northeast = 0
    southeast = 0

    for region in regions:
        if region == 'northwest':
            northwest += 1
        elif region == 'southwest':
            southwest += 1
        elif region == 'northeast':
            northeast += 1
        elif region == 'southeast':
            southeast += 1

    return northwest, southwest, northeast, southeast

# getting the initial results!

print("Average age: ", average_age(ages))

men, women = sexes_count(sexes)
print("Number of men: ", men)
print("Number of women: ", women)

print("Average insurance cost:", average_cost(insurance_charges))

nw, sw, ne, se = regions_count(regions)
print("Northwest: ", nw)
print("Southwest: ", sw)
print("Northeast: ", ne)
print("Southeast: ", se)

# on average, how do men compare to women with their insurance cost?
def average_cost_by_sex(sexes, insurance_charges):
    male_total = 0
    female_total = 0
    male_count = 0
    female_count = 0

    for i in range(len(sexes)):
        cost = float(insurance_charges[i])

        if sexes[i] == 'male':
            male_total += cost
            male_count += 1
        else:
            female_total += cost
            female_count += 1

    avg_male = male_total / male_count
    avg_female = female_total / female_count

    return avg_male, avg_female

# on average, what region has the highest average cost?
def average_cost_by_region(regions, insurance_charges):
    northwest_total = 0
    southwest_total = 0
    northeast_total = 0
    southeast_total = 0

    northwest_count = 0
    southwest_count = 0
    northeast_count = 0
    southeast_count = 0

    for i in range(len(regions)):
        region = regions[i]
        cost = float(insurance_charges[i])

        if region == 'northwest':
            northwest_total += cost
            northwest_count += 1
        elif region == 'southwest':
            southwest_total += cost
            southwest_count += 1
        elif region == 'northeast':
            northeast_total += cost
            northeast_count += 1
        elif region == 'southeast':
            southeast_total += cost
            southeast_count += 1

    # calculate averages
    northwest_avg = northwest_total / northwest_count
    southwest_avg = southwest_total / southwest_count
    northeast_avg = northeast_total / northeast_count
    southeast_avg = southeast_total / southeast_count

    return northwest_avg, southwest_avg, northeast_avg, southeast_avg

# do more men or more women smoke?
def smoker_by_sex(sexes, smoker_statuses):
    male_smokers = 0
    female_smokers = 0

    for i in range(len(sexes)):
        if smoker_statuses[i] == 'yes':
            if sexes[i] == 'male':
                male_smokers += 1
            else:
                female_smokers += 1

    return male_smokers, female_smokers

# how much higher is the smoker's insurance compared to a non-smoker's insurance on average?
def smoker_vs_nonsmoker_cost(smoker_statuses, insurance_charges):
    smoker_total = 0
    nonsmoker_total = 0
    smoker_count = 0
    nonsmoker_count = 0

    for i in range(len(smoker_statuses)):
        cost = float(insurance_charges[i])

        if smoker_statuses[i] == 'yes':
            smoker_total += cost
            smoker_count += 1
        else:
            nonsmoker_total += cost
            nonsmoker_count += 1

    avg_smoker = smoker_total / smoker_count
    avg_nonsmoker = nonsmoker_total / nonsmoker_count

    difference = avg_smoker - avg_nonsmoker

    return avg_smoker, avg_nonsmoker, difference

# the new print statements for analysis:
male_avg, female_avg = average_cost_by_sex(sexes, insurance_charges)
print("Average cost for men: ", male_avg)
print("Average cost for women: ", female_avg)

nw, sw, ne, se = average_cost_by_region(regions, insurance_charges)

print("Northwest average:", nw)
print("Southwest average:", sw)
print("Northeast average:", ne)
print("Southeast average:", se)

# find highest
highest = max(nw, sw, ne, se)

if highest == nw:
    print("Highest average cost: Northwest")
elif highest == sw:
    print("Highest average cost: Southwest")
elif highest == ne:
    print("Highest average cost: Northeast")
else:
    print("Highest average cost: Southeast")


# Do more men or more women smoke?

male_smokers, female_smokers = smoker_by_sex(sexes, smoker_statuses)

print("Male smokers: ", male_smokers)
print("Female smokers: ", female_smokers)





