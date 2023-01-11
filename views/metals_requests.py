METALS = [
    {
        "id": 1,
        "metal": "Gold",
        "price": 90.36
    },
    {
        "id": 2,
        "metal": "Platinum",
        "price": 95.20
    },
    {
        "id": 3,
        "metal": "Palladium",
        "price": 80.22
    },
    {
        "id": 4,
        "metal": "Copper",
        "price": 29.99
    }
]


def get_all_metals():
    return METALS


# Function with a single parameter
def get_single_metal(id):
    # Variable to hold the found metal, if it exists
    requested_metal = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for metal in METALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if metal["id"] == id:
            requested_metal = metal

    return requested_metal


def create_metal(metal):
    # Get the id value of the last animal in the list
    max_id = METALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    metal["id"] = new_id

    # Add the animal dictionary to the list
    METALS.append(metal)

    # Return the dictionary with `id` property added
    return metal
