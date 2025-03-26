from pyomo.environ import *

# Volume do pedido
V = 100

# Teor alcoólico desejado
A = 0.06

components = {
    'Cerveja A': {'A': 0.058, 'P': 0.28},
    'Cerveja B': {'A': 0.037, 'P': 0.25},
    'Água':      {'A': 0.000, 'P': 0.05},
    'Vinho':     {'A': 0.083 ,'P': 0.40},
}

# Lista de componentes
C = components.keys()

# Modelo
model = ConcreteModel()

# Variáveis de decisão: uma para cada componente
model.x = Var(C, domain = NonNegativeReals)

# Função objetivo
model.cost = Objective(expr = sum(model.x[c] * components[c]['P'] for c in C))

# Restrições
model.vol = Constraint(expr = sum(model.x[c] for c in C) == V)
model.alc = Constraint(expr = sum(model.x[c] * components[c]['A'] for c in C) == A * V)

# Solução
solver = SolverFactory('glpk')
solver.solve(model)

print('Mistura ótima')
for c in C:
    print('>', c, ':', model.x[c](), 'litros')
print()
print('Volume =', model.vol(), 'litros')
print('Custo = $', model.cost())