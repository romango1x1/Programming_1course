def most_popular_number(votes):
    counter = {}
    max_count = 0
    most_popular = 0

    for allvotes in votes:
        if allvotes in counter:
            counter[allvotes] += 1
        else:
            counter[allvotes] = 1

        if counter[allvotes] > max_count or (counter[allvotes] == max_count and allvotes < most_popular):
            most_popular = allvotes
            max_count = counter[allvotes]

    return most_popular


num_tests = int(input())

for _ in range(num_tests):
    num_votes = int(input())
    votes = [int(input()) for _ in range(num_votes)]

    print(most_popular_number(votes))

# https://www.eolymp.com/uk/submissions/15428528
