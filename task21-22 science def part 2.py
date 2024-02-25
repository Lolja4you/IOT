# Task 21
def calculate_velocity(x):
    max_velocity = 0
    for i in range(1, len(x)):
        max_velocity = max(abs(x[i] - x[i-1]) / 0.01, max_velocity)
    return max_velocity

x = [1, 3, 4, 7, 8, 9, 10]
print(calculate_velocity(x))

# Task 22
melt = {"Ag2O": 160, "Al2O3": 2053, "O2": 218, "AsH3": 117, "B2O3": 450}
def find_oxides(melt: dict):
    oxides_melting_temperatures = [melt[compound] for compound in melt if "O" in compound]
    return ' '.join(map(str, oxides_melting_temperatures))
print(find_oxides(melt))