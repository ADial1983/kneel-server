SIZES = [
    {
        "id": 1,
        "carets": 5,
        "price": 100
    },
    {
        "id": 2,
        "carets": 3,
        "price": 75.88
    },
    {
        "id": 3,
        "carets": 7,
        "price": 339.99
    },
    {
        "id": 4,
        "carets": 0.5,
        "price": 45
    },
    {
        "id": 5,
        "carets": 2.25,
        "price": 66.44
    }
]


def get_all_sizes():
    return SIZES


def get_single_size(id):
    # Variable to hold the found metal, if it exists
    requested_size = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for size in SIZES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if size["id"] == id:
            requested_size = size

    return requested_size

def create_size(size):
    # Get the id value of the last animal in the list
    max_id = SIZES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    size["id"] = new_id

    # Add the animal dictionary to the list
    SIZES.append(size)

    # Return the dictionary with `id` property added
    return size
