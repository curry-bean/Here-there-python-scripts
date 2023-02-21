import random

# Define a function to generate a Markov chain from a list of lines
def generate_markov_chain(lines):
    chain = {}
    for line in lines:
        words = line.split()
        for i in range(len(words) - 1):
            if words[i] not in chain:
                chain[words[i]] = []
            chain[words[i]].append(words[i+1])
    return chain

# Load a list of sample poems
with open("poems.txt") as f:
    poems = f.readlines()

# Generate a Markov chain from the sample poems
chain = generate_markov_chain(poems)

# Define a function to generate a new line of poetry from the Markov chain
def generate_line(chain):
    line = ""
    word = random.choice(list(chain.keys()))
    while word not in ["\n", ".", "?", "!"]:
        line += word + " "
        word = random.choice(chain[word])
    return line.capitalize().strip()

# Generate a poem with 4 stanzas, each consisting of 4 lines
for i in range(4):
    for j in range(4):
        print(generate_line(chain))
    print("")
