def load_name_list(filename):
    with open(filename) as f:
        return [name.capitalize() for name in (line.strip() for line in f) if len(name) > 0]

female_names = load_name_list('data/female-names.txt')
male_names = load_name_list('data/male-names.txt')
last_names = load_name_list('data/last-names.txt')

