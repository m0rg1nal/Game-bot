import matplotlib.pyplot as plt
import os

# functions
def get_stat(obj, period, dataset):
    plt.plot(dataset.keys(), dataset.values(), 'g-')
    plt.suptitle(f'{obj} per {period}')
    plt.ylabel(obj)
    plt.xlabel(f'{period}s')
    plt.savefig(f'{obj}_stat.png')
    plt.show()


def save_to_txt(obj, period, dataset, filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write(f'{obj} per {period}\n')
    with open(filename, 'a') as file:
        for key, value in dataset.items():
            file.write(f'{key} {value}\n')
    print(f'Data saved to {filename}')

# ...

def load_from_txt(filename):
    dataset = {}
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip the first line
        for line in lines:
            key, value = line.strip().split()
            dataset[int(key)] = float(value)
    return dataset

def greetings():
    return
