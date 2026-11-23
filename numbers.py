data = [5, 10, 15, 10, 20, 25, 30, 10, 35, 40, 15, 45]


def get_total(data):
    result = 0
    index = 0

    while index < len(data):
        result = result + data[index]
        index += 1

    return result


def get_average(data):
    total = get_total(data)
    count = len(data)
    return total / count


def get_median_and_mode(data):
    ordered_data = sorted(data)
    n = len(ordered_data)

    if n % 2 != 0:
        middle = ordered_data[n // 2]
    else:
        first = ordered_data[n // 2 - 1]
        second = ordered_data[n // 2]
        middle = (first + second) / 2

    frequency = {}
    for item in data:
        if item not in frequency:
            frequency[item] = 1
        else:
            frequency[item] += 1

    max_count = max(frequency.values())
    common = []

    for item in frequency:
        if frequency[item] == max_count:
            common.append(item)

    return middle, common


print("Total:", get_total(data))
print("Average:", get_average(data))
print("Median and Mode:", get_median_and_mode(data))