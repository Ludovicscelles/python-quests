print("Imported my_module ...")

test = "Test string"

def hello_world():
    print("Hello, World!")

def find_index(to_search, target):
    """Find the index of a value in a sequence."""
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1

# Variables
PI = 3.14159
GRAVITY = 9.81

# Variables globales utiles

WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
YEAR_MONTHS = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def factorial(n):

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

# other way to do it:

def factorial_iterative(n):

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1

    for i in range(2, n + 1):
        result *= i
    return result

def circle_area(radius):
    return PI * (radius ** 2)

def cinematic_energy(mass, velocity):
    return 0.5 * mass * (velocity ** 2)

# fonctions pour calculer la moyenne, la médiane et l'écart type d'une liste de nombres

def mean(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        # Si le nombre d'éléments est pair, retourner la moyenne des deux éléments du milieu
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def ecart_type(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    mean_value = mean(numbers)
    variance = sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def clear_data(data):
    return [x for x in data if x is not None and x != '']

def count_occurrences(numbers):
    return {num: numbers.count(num) for num in set(numbers)}

# fonction pour normaliser les données dans une liste dans une plage de 0 à 1
def normalize_data(data):
    if not data:
        raise ValueError("The list is empty.")
    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val
    if range_val == 0:
        raise ValueError("All numbers in the list are the same.")
    # Normalize each value in the list to a range of 0 to 1
    return [(x - min_val) / range_val for x in data]

def growth_rate(initial_value, final_value):
    if initial_value <= 0:
        raise ValueError("Initial value must be greater than zero.")
    return (final_value - initial_value) / initial_value * 100

# fonction pour calculer la fréquence relative d'une liste de catégories
# La fréquence relative est le nombre d'occurrences d'une catégorie divisé par le nombre total d'éléments dans la liste.
def relative_frequency(data):
    if not data:
        raise ValueError("The list is empty.")
    total_count = len(data)
    occurrences = count_occurrences(data)
    return {key: value / total_count for key, value in occurrences.items()}

# fonction pour détecter les valeurs aberrantes dans une liste de nombres en utilisant la méthode du z-score
def outlier_zscore(data, threshold=3):
    if not data:
        raise ValueError("The list is empty.")
    mean_value = mean(data)
    std_dev = ecart_type(data)
    if std_dev == 0:
        raise ValueError("Standard deviation is zero, cannot compute z-scores.")
    return [x for x in data if abs((x - mean_value) / std_dev) > threshold]

def find_mode(data):
    if not data:
        raise ValueError("The list is empty.")
    occurrences = count_occurrences(data)
    return max(occurrences, key=occurrences.get)

def round_list(numbers, decimals=2):
    if not numbers:
        raise ValueError("The list is empty.")
    return [round(num, decimals) for num in numbers]
