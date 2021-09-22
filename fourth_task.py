# input_data - function in which the user sets the weight of each gold bar
# fill_knapsack recursive function - that is a solution of the problem
# number_of_different_bars- number of different bars
def input_data(number_of_different_bars):
    weight_of_bars = []
    i = 0
    while i < number_of_different_bars:
        bar = int(input("Enter the weight of the bar "))
        if bar > 0:
            i += 1
            weight_of_bars.append(bar)
        else:
            print("Incorrect input, the weight of bar must be > 0. Try again.")
    return weight_of_bars


# capacity - knapsack's capacity, weight- weights of gold bars
def fill_knapsack(capacity, weight, number_of_different_bars):
    # end of function(when capacity is 0 or we have no bars
    if number_of_different_bars == 0 or capacity == 0:
        return 0
    # check if weight of the bar more than the capacity of our knapsack
    # if the weight of the bar is greater than capacity,
    # this bar bar can't be included in optimal solution

    if weight[number_of_different_bars - 1] > capacity:
        return fill_knapsack(capacity, weight, number_of_different_bars - 1)
    else:
        # consider all subsets of bars and calculate the
        # total weight of all subsets.
        # Consider the only subsets whose total weight is smaller than capacity
        # From all such subsets, pick the maximum weight subset and return the weight of it.

        return max(
            weight[number_of_different_bars - 1] + fill_knapsack(capacity - weight[number_of_different_bars - 1],
                                                                 weight,
                                                                 number_of_different_bars - 1),
            fill_knapsack(capacity, weight, number_of_different_bars - 1))


try:
    capacity_of_knapsack = int(input("Enter the capacity of ur knapsack "))
    if capacity_of_knapsack < 0:
        print("Capacity of ur knapsack must be > -1")
    else:
        num_of_different_bars = int(input("Enter the number of bars with different weight "))
        print(fill_knapsack(capacity_of_knapsack, input_data(num_of_different_bars), num_of_different_bars))
except ValueError:
    print("Incorrect input. Try again")
except IndexError:
    print("Number of bars with different weight must be > -1")
except EOFError or KeyboardInterrupt:
    print("Error, incorrect input! Try again.")
