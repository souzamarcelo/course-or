from pyomo.environ import *

m = 3                # fornecedores
n = 3                # clientes
a = [5, 7, 3]        # estoques
b = [7, 3, 5]        # demandas
c = [[3, 1, 100],    # custos
     [4, 2, 4],
     [100, 3, 3]]

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão: para cada par depósito x cliente
model.x = Var([i for i in range(m)], [j for j in range(n)], domain = NonNegativeReals)

def objective_function(model):
    result = 0
    for i in range(m):
        for j in range(n):
            result += model.x[i,j] * c[i][j]
    return result

# Função objetivo
#model.obj = Objective(expr = sum(model.x[i,j]*c[i][j] for i in range(m) for j in range(n)))
model.obj = Objective(rule = objective_function)

# Restrições
model.cons = ConstraintList()

for i in range(m):
    model.cons.add(expr = sum(model.x[i,j] for j in range(n)) <= a[i])

for j in range(n):
    model.cons.add(expr = sum(model.x[i,j] for i in range(m)) == b[j])

# Solução
solver = SolverFactory('glpk')
solver.solve(model).write()

print('Custo total:', model.obj())
for i in range(m):
    for j in range(n):
        print(i + 1, '-->', j + 1, ':', model.x[i,j]())