from pyDatalog import pyDatalog

pyDatalog.clear()

# Define female/1 predicate
pyDatalog.create_terms('female')
female('Hillary')
female('Lena')
female('Lisa')
female('Elise')

# Define male/1 predicate
pyDatalog.create_terms('male')
male('Mike')
male('Lennari')
male('Donald')
male('Usaim')
male('Adam')
male('Simon')
male('Joar')
male('Dan')

# Define parent/2 predicate
pyDatalog.create_terms('parent')
parent('Mike', 'Lennari')
parent('Mike', 'Lena')
parent('Lennari', 'Donald')
parent('Lennari', 'Hillary')
parent('Lennari', 'Usaim')
parent('Lennari', 'Adam')
parent('Lennari', 'Simon')
parent('Donald', 'Lisa')
parent('Donald', 'Joar')
parent('Hillary', 'Elise')
parent('Usaim', 'Dan')

# Define father/1 predicate
pyDatalog.create_terms('father')
X = pyDatalog.Variable()  # Create X variable
Y = pyDatalog.Variable()  # Create Y variable
father(X, Y) <= male(X) & parent(X, Y)

# Define sister/2 predicate
pyDatalog.create_terms('sister')
X = pyDatalog.Variable()  # Create X variable
Y = pyDatalog.Variable()  # Create Y variable
Z = pyDatalog.Variable()  # Create Z variable
sister(X, Y) <= female(X) & parent(Z, X) & parent(Z, Y) & (X != Y)

# Define grandmother/2 predicate
pyDatalog.create_terms('grandmother')
grandmother(X, Z) <= female(X) & parent(X, Y) & parent(Y, Z)

# Define cousin/2 predicate
pyDatalog.create_terms('cousin')
cousin(X, Y) <= parent(Z, X) & parent(W, Y) & (Z != W) & sibling(Z, W)

# Define grandfather/2 predicate
pyDatalog.create_terms('grandfather')
grandfather(X, Y) <= male(X) & parent(X, Z) & parent(Z, Y)

# Define mother/1 predicate
pyDatalog.create_terms('mother')
mother(X, Y) <= female(X) & parent(X, Y)

# Define brother/2 predicate
pyDatalog.create_terms('brother')
brother(X, Y) <= male(X) & parent(Z, X) & parent(Z, Y) & (X != Y)

# Define uncle/2 predicate
pyDatalog.create_terms('uncle')
uncle(X, Y) <= male(X) & parent(Z, Y) & sibling(Z, X)

# Define aunty/2 predicate
pyDatalog.create_terms('aunty')
aunty(X, Y) <= female(X) & parent(Z, Y) & sibling(Z, X)

# Define sibling
pyDatalog.create_terms('sibling')
sibling(X, Y) <= parent(Z, X) & parent(Z, Y) & (X != Y)

# Query to return the cousin of Adam
print(cousin('Adam', X))

# Query to return the grandfather of Elise
print(grandfather(X, 'Elise'))
