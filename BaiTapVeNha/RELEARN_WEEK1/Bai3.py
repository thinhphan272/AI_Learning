string  = "      Hello World!    "

print(f"{string} ater delete spacing {string.strip()}.")

print(f"{string} ater converting to lowercase {string.lower()}.")

print(f"{string} ater converting to uppercase {string.upper()}.")

new_string = string.replace("H", "J", 1)

print(f"{string} after replace H -> J: {new_string}.")