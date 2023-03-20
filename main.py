user_choice = input("What word do you want?")
wordlist = [
    "abundant",
    "baffle",
    "beleaguered",
    "burgeon",
    "coalesce",
    "convivial",
    "corpulent",
    "craven",
    "deft",
    "deleterious",
    "dilapidated",
    "eclectic",
    "effervescent",
    "elusive",
    "enigmatic",
    "ephemeral",
    "erudite",
    "ethereal",
    "exacerbate",
    "exorbitant",
    "exquisite",
    "fallow",
    "feckless",
    "florid",
    "fortuitous",
    "frugal",
    "furtive",
    "garrulous",
    "grandiose",
    "hackneyed",
    "hallowed",
    "haughty",
    "heuristic",
    "impeccable",
    "impetuous",
    "implacable",
    "indefatigable",
    "indomitable",
    "insidious",
    "insipid",
    "insolent",
    "intransigent",
    "jaunty",
    "languid",
    "lissome",
    "lugubrious",
    "luminous",
    "magnanimous",
    "maladroit",
    "mendacious",
    "mercurial",
    "meticulous",
    "munificent",
    "nadir",
    "nefarious",
    "obtuse",
    "pallid",
    "panacea",
    "perfidious",
    "perfunctory",
    "pernicious",
    "perspicacious",
    "pervasive",
    "petulant",
    "platitudinous",
    "precipitous",
    "prosaic",
    "quiescent",
    "quixotic",
    "recondite",
    "reprobate",
    "resilient",
    "reticent",
    "sanguine",
    "sardonic",
    "spurious",
    "supercilious",
    "taciturn",
    "turgid",
    "ubiquitous",
    "unctuous",
    "verdant",
    "vituperative",
    "wistful"
]

def binary_search(lst, target):
    if not lst:
        return False

    print("Searching in list:", lst)

    mid = len(lst) // 2
    guess = lst[mid]

    print("Guessing:", guess)

    if guess == target:
        return True
    elif guess < target:
        return binary_search(lst[mid+1:], target)
    else:
        return binary_search(lst[:mid], target)

if binary_search(wordlist, user_choice):
    print("Found", user_choice)
else:
    print("Word not found")
