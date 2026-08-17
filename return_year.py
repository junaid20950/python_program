birth_dates = [1900, 1920, 1950, 1900]
death_dates = [1950, 1960, 1970, 1940]
def highet_year(birth_dates,death_dates):
    events=[]
    for i in birth_dates:
        events.append((i,1))
    for j in death_dates:
        events.append((j+1,-1))
    events.sort()

    max_population = 0
    current_population = 0
    peak_year = None
    for year, change in events:
        current_population+=change
        if current_population > max_population:
            max_population = current_population
            peak_year = year

    return f"peak_year:{peak_year}"
    # return f"events:{events}"
print(highet_year(birth_dates,death_dates))