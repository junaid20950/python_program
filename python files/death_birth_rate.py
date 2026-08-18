birth_dates = [1900, 1920, 1950, 1900]
death_dates = [1950, 1960, 1970, 1940]
def find_highest_population_year(births, deaths):
    # Create change logs: +1 for a birth, -1 for a death the following year
    # (assuming a person is included in the population for their death year)
    events = []
    
    for birth in births:
        events.append((birth, 1))
    for death in deaths:
        events.append((death + 1, -1))
        
    # Sort events by year. If years are equal, deaths (-1) process before births (+1)
    events.sort()
    
    max_population = 0
    current_population = 0
    peak_year = None
    
    # Sweep through the years chronologically
    for year, change in events:
        current_population += change
        
        # Track the absolute peak population
        if current_population > max_population:
            max_population = current_population
            peak_year = year
            
    return peak_year

# --- Example Usage ---
birth_dates = [1900, 1920, 1950, 1900]
death_dates = [1950, 1960, 1970, 1940]

print(find_highest_population_year(birth_dates, death_dates))
# Output: 1920
