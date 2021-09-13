# data - function in which the user sets the weight of each gold bar
# knapsack recursive function - that is a solution of the problem
# number_of_different_bars- number of different bars
def data(number_of_different_bars):
    i = 0
    while i < number_of_different_bars:
        bar = int(input("Enter the weight of the bar "))
        i += 1
        weight.append(bar)

# capacity - knapsack's capacity, weight- weights of gold bars
def knapsack(capacity, weight, number_of_different_bars):
    # end of function(when capacity is 0 or we have no bars
    if number_of_different_bars == 0 or capacity == 0:
        return 0
    # check if weight of the bar more than the capacity of our knapsack
    # if the weight of the bar is greater than capacity,
    # this bar bar can't be included in optimal solution

    if (weight[number_of_different_bars - 1] > capacity):
        return knapsack(capacity, weight, number_of_different_bars - 1)
    else:
        # consider all subsets of bars and calculate the
        # total weight of all subsets.
        # Consider the only subsets whose total weight is smaller than capacity
        # From all such subsets, pick the maximum weight subset and return the weight of it.

        return max(
            weight[number_of_different_bars - 1] + knapsack(capacity - weight[number_of_different_bars - 1], weight,
                                                            number_of_different_bars - 1),
            knapsack(capacity, weight, number_of_different_bars - 1))


weight = []
capacity = int(input("Enter the capacity of ur knapsack "))
number_of_different_bars = int(input("Enter the number of bars with different weight "))
data(number_of_different_bars)
print(knapsack(capacity, weight, number_of_different_bars))
