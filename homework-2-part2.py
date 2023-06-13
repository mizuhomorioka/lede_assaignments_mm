#Mizuho MOrioka
#Jun 7th 2023
#Homework2,Part2

#PART TWO: Lists
countries=["Japan","Colombia","Peru","Germany","Brazil","China","US"]
for country in countries:
    print(country)
countries.sort()
print(countries[0])
print(countries[-2])

countries.remove("Japan")

for country in countries:
    print(country.upper())

#PART TWO: Dictionaries

#jomon sugi 20170-7200 japanese cedar yakushima japan

tree={'name':"Jomon Sugi",'spiecies':"Japanese cedar",'age':2170,'location_name':"Yakushima,Japan",'latitude':30.336946,'longitude':130.531103}
print(tree['name'],"is a",tree['age'], "year old tree that is in", tree['location_name'])
#The coordinates of New York City are 40.7128° N, 74.0059° W. 
if tree["latitude"]<40.7128:
    print("The tree",tree["name"],"in",tree["location_name"],"is south of NYC")
else:
    print("The tree",tree["name"],"in",tree["location_name"],"is north of NYC")

user_age=input("How old are you?")
user_age=int(user_age)
age_difference=tree['age']- user_age
if age_difference>0:
    print(tree["name"],"was",age_difference,"old than you are born")
else:
    print("You are",age_difference,"years older than",tree["name"])

#PART TWO: Lists of dictionaries
places=[{'name':"Moscow",'latitude':55.758664,'longitude':37.619292},{'name':"Tehran",'latitude':35.668208,'longitude':51.374414},{'name':"Falkland Islands",'latitude':-51.796719,'longitude':-58.594932},{'name':"Seoul",'latitude':37.566983,'longitude':126.978235},{'name':"Santiago",'latitude':-33.451856,'longitude':-70.650466}]
for place in places:
    name=place['name']
    latitude=place['latitude']
    if int(latitude)>0:
        print(name,"is above equater")
    else:
        print(name,"is below equater")
    if name =="Falkland Islands":
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")

for place in places:
    latitude=place['latitude']
    tree_lat=tree['latitude']
    name=place['name']
    if int(latitude) > int(tree_lat):
        print(name,"is north of", tree["name"])
    else:
        print(name, "is south of",tree["name"])
