import random

people = ["A", "B", "J", "K", "Y"]

def main():
	#shuffle spots 1-5
	firstSpots = random.sample(people, len(people))
	#shuffle spots 6-10
	secondSpots = random.sample(people, len(people))
	#for each person, find the tuple (a,b), where a is their spot in the first 5 picks and b is their spot in the 2nd 5 picks
	peopleSpots = {}
	for p in people:
		a = firstSpots.index(p)
		b = secondSpots.index(p) + len(people)
		peopleSpots[p] = (a,b)

	#for each person, flip a coin to determine which of their teams picks in the first 5 picks and which picks in the 2nd 5 picks
	spots = {}
	for p in people:
		(a,b) = peopleSpots[p]
		if random.random() < 0.5:
			spots[a] = p + "1"
			spots[b] = p + "2"
		else:
			spots[a] = p + "2"
			spots[b] = p + "1"

	#sort the map to get the draft order
	for k in sorted(spots):
		print((k, spots[k]))


if __name__ == "__main__":
	main()