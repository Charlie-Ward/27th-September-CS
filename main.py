def score_calculator(results):
    global points
    points = 0
    for i in range(len(results) - 1):
        match results[i]:
            case "W":
                points += 2
            case "D":
                points += 1
            case "L":
                points += 0
            case _:
                print(f'Error at result number {i+1}')
    return points

results = ['W','L','W','W','W','W','W','D','W','L','L','L']
score_calculator(results)
print(f'Total points: {points}')