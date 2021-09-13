# knapsack recursive function that is a solution of the problem
# capacity - knapsack's capacity, weight- weights of gold bars,
# number_of_different_bars- number of different bars
def knapsack(capacity, weight, number_of_different_bars):
    # end of function(when capacity is 0 or we have no bars
    if number_of_different_bars == 0 or capacity == 0:
        return 0
    # check if weight of the bar more than the capacity of our knapsack
    # if the weight of the bar is greater than capacity,
    # then we return this function with another bar
    #
    if (weight[number_of_different_bars - 1] > capacity):
        return knapsack(capacity, weight, number_of_different_bars - 1)
    else:
        return max(
            weight[number_of_different_bars - 1] + knapsack(capacity - weight[number_of_different_bars - 1], weight,
                                                            number_of_different_bars - 1),
            knapsack(capacity, weight, number_of_different_bars - 1))


weight = []
capacity = int(input("Enter the capacity of ur knapsack "))
number_of_different_bars = int(input("Enter the number of bars with different weight "))
i = 0
while i < number_of_different_bars:
    bar = int(input("Enter the weight of the bar "))
    i += 1
    weight.append(bar)
print(knapsack(capacity, weight, number_of_different_bars))
