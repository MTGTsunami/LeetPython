def stringFormattedWeeklyPrices(dailyPrice):
    l, r = 0, 6
    summ = 0
    for i in range(7):
        summ += dailyPrice[i]

    out = []
    while r < len(dailyPrice):
        out.append(str('{:.2f}'.format(float(summ/7))))
        summ -= dailyPrice[l]
        l += 1
        r += 1
        if r < len(dailyPrice):
            summ += dailyPrice[r]
    return out


print(stringFormattedWeeklyPrices([7,8,8,11,9,7,5,6]))