from classes import Round, Person

### Round class tests ###
print("Testing Round Class")

#arrange
new_round = Round()
expected = []


#act 

# assert
assert new_round.list_of_drinks == expected


print("True -- Round Class List")

#arrange
new_drink = "Cola"
expected_1 = [new_drink]
#act
new_round.add_to_order(new_drink)
actual = new_round.list_of_drinks
#assert
assert  actual == expected_1
print("True -- Add a drink")

#arrange

# Testing new_round.list_of_drinks
expected = 1

#act
actual = new_round.size()

#assert

assert expected == actual
print("True -- Size Method ")
0
### Person ###

A_single_person = Person()

#arrange


#act



#assert

assert actual == expected
#assert actual_1 == expected_1