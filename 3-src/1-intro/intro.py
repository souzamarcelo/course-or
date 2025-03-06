from pyomo.environ import *

model = ConcreteModel()

model.x = Var([1,2], domain = NonNegativeReals)

model.obj = Objective(expr = 3 * model.x[1] + 5 * model.x[2], sense = maximize)

model.con1 = Constraint(expr = model.x[1] <= 4)
model.con2 = Constraint(expr = 2 * model.x[2] <= 12)
model.con3 = Constraint(expr = 3 * model.x[1] + 2 * model.x[2] <= 18)

opt = SolverFactory('glpk')
results = opt.solve(model)

print('Status:', results.solver.status)
print('Termination criterion:', results.solver.termination_condition)
if results.solver.termination_condition == 'optimal':
    print('Optimal solution cost:', model.obj.expr())
    print('Optimal solution is x1 =', model.x[1].value, 'and x2 =', model.x[2].value)