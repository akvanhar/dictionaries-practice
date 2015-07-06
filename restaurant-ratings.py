# your code goes here
restaurant_ratings = {}

restaurant_file = open("scores.txt")

for line in restaurant_file:
    line = line.rstrip()
    line = line.split(":")
    restaurant_ratings[line[0]] = int(line[1])

for restaurant, rating in sorted(restaurant_ratings.items()):
    print "%s is rated at %d." % (restaurant, rating)
