import random

states = [
	{
	    "name": "Alabama",
	    "capital": "Montgomery"
	}, {
	    "name": "Alaska",
	    "capital": "Juneau"
	}, {
	    "name": "Arizona",
	    "capital": "Phoenix"
	}, {
	    "name": "Arkansas",
	    "capital": "Little Rock"
	}, {
	    "name": "California",
	    "capital": "Sacramento"
	}, {
	    "name": "Colorado",
	    "capital": "Denver"
	}, {
	    "name": "Connecticut",
	    "capital": "Hartford"
	}, {
	    "name": "Delaware",
	    "capital": "Dover"
	}, {
	    "name": "Florida",
	    "capital": "Tallahassee"
	}, {
	    "name": "Georgia",
	    "capital": "Atlanta"
	}, {
	    "name": "Hawaii",
	    "capital": "Honolulu"
	}, {
	    "name": "Idaho",
	    "capital": "Boise"
	}, {
	    "name": "Illinois",
	    "capital": "Springfield"
	}, {
	    "name": "Indiana",
	    "capital": "Indianapolis"
	}, {
	    "name": "Iowa",
	    "capital": "Des Moines"
	}, {
	    "name": "Kansas",
	    "capital": "Topeka"
	}, {
	    "name": "Kentucky",
	    "capital": "Frankfort"
	}, {
	    "name": "Louisiana",
	    "capital": "Baton Rouge"
	}, {
	    "name": "Maine",
	    "capital": "Augusta"
	}, {
	    "name": "Maryland",
	    "capital": "Annapolis"
	}, {
	    "name": "Massachusetts",
	    "capital": "Boston"
	}, {
	    "name": "Michigan",
	    "capital": "Lansing"
	}, {
	    "name": "Minnesota",
	    "capital": "St. Paul"
	}, {
	    "name": "Mississippi",
	    "capital": "Jackson"
	}, {
	    "name": "Missouri",
	    "capital": "Jefferson City"
	}, {
	    "name": "Montana",
	    "capital": "Helena"
	}, {
	    "name": "Nebraska",
	    "capital": "Lincoln"
	}, {
	    "name": "Nevada",
	    "capital": "Carson City"
	}, {
	    "name": "New Hampshire",
	    "capital": "Concord"
	}, {
	    "name": "New Jersey",
	    "capital": "Trenton"
	}, {
	    "name": "New Mexico",
	    "capital": "Santa Fe"
	}, {
	    "name": "New York",
	    "capital": "Albany"
	}, {
	    "name": "North Carolina",
	    "capital": "Raleigh"
	}, {
	    "name": "North Dakota",
	    "capital": "Bismarck"
	}, {
	    "name": "Ohio",
	    "capital": "Columbus"
	}, {
	    "name": "Oklahoma",
	    "capital": "Oklahoma City"
	}, {
	    "name": "Oregon",
	    "capital": "Salem"
	}, {
	    "name": "Pennsylvania",
	    "capital": "Harrisburg"
	}, {
	    "name": "Rhode Island",
	    "capital": "Providence"
	}, {
	    "name": "South Carolina",
	    "capital": "Columbia"
	}, {
	    "name": "South Dakota",
	    "capital": "Pierre"
	}, {
	    "name": "Tennessee",
	    "capital": "Nashville"
	}, {
	    "name": "Texas",
	    "capital": "Austin"
	}, {
	    "name": "Utah",
	    "capital": "Salt Lake City"
	}, {
	    "name": "Vermont",
	    "capital": "Montpelier"
	}, {
	    "name": "Virginia",
	    "capital": "Richmond"
	}, {
	    "name": "Washington",
	    "capital": "Olympia"
	}, {
	    "name": "West Virginia",
	    "capital": "Charleston"
	}, {
	    "name": "Wisconsin",
	    "capital": "Madison"
	}, {
	    "name": "Wyoming",
	    "capital": "Cheyenne"
	}
]

total_correct = 0
start_over = True

print('Welcome to the capital game!')

def checkKey(key, index):
	if key in states[index].keys():
		return True
	else:
		return False

print(states[0])

while start_over:

	random.shuffle(states)


	for index in range(len(states)):
		print(f'-------------Question {index + 1}:-------------')
		answer = input(f'What is the capital of {states[index]["name"]}?')
		if not checkKey('correct', index) and not checkKey('incorrect', index):
			states[index]['correct'] = 0
			states[index]['incorrect'] = 0
		if(answer != states[index]['capital']):
			print('Wrong!')
			states[index]['incorrect'] += 1
		else:
			print('Correct!')
			total_correct += 1
			states[index]['correct'] += 1
		print(f"You have answered this question {states[index]['correct']} times correctly and {states[index]['incorrect']} times incorrectly.")
		print('Correct answers out of 50')
		print('Total correct', total_correct)
		print('---------------------------------------')
	check=input(f'Try again? (Y/N)')
	start_over=(True if check =='Y' else False)




