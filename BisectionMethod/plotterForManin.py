import math


def f(x):
    return ((0.3*(x+5))**3-10)


def find_Root_By_Bisection_Method(lower,upper,MAX_ITERATION):
    iteration = 0
    prev_solution = 0
    table = []
    tablel = [[lower,f(lower)]]
    tabler = [[upper,f(upper)]]
    for iteration in range(MAX_ITERATION):
        mid = (lower+upper)/2
        if iteration!=0:
            error = math.fabs((mid-prev_solution)/mid)*100
            data = [mid,f(mid)]
            if error<0.5:
                break
        else:
            data = [mid,f(mid)]
        table.append(data)
        prev_solution = mid
        if f(lower)*f(mid)<0:
            upper = mid
        else:
            lower = mid
        tablel.append([lower,f(lower)])
        tabler.append([upper, f(upper)])
    return table,tablel,tabler;

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    table = find_Root_By_Bisection_Method(-1.999, 0.7, 20)
    header = ["iteration","value","Relative Error"]
    #tt.print(table,header)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
