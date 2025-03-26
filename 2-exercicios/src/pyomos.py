from pyomo.environ import *

def occ():
    #from pyomo.environ import *

    model = ConcreteModel()

    model.x = Var([1,2], domain = NonNegativeReals)

    model.obj = Objective(expr = 1500 * model.x[1] + 1000 * model.x[2], sense = maximize)

    model.con1 = Constraint(expr = model.x[1] + model.x[2] <= 30)
    model.con2 = Constraint(expr = model.x[1] >= 10)
    model.con3 = Constraint(expr = model.x[2] >= 10)

    opt = SolverFactory('glpk')
    results = opt.solve(model)

    print('Status:', results.solver.status)
    print('Termination criterion:', results.solver.termination_condition)
    if results.solver.termination_condition == 'optimal':
        print('Optimal solution cost:', model.obj.expr())
        print('Optimal solution is x1 =', model.x[1].value, 'and x2 =', model.x[2].value)


def ulern():
    #from pyomo.environ import *

    model = ConcreteModel()

    model.e = Var(domain = NonNegativeReals)
    model.d = Var(domain = NonNegativeReals)

    def objective_function(model):
        return model.e + 2 * model.d

    model.obj = Objective(rule = objective_function, sense = maximize)

    def con1(model):
        return model.e + model.d <= 10

    def con2(model):
        return model.e - model.d >= 0

    def con3(model):
        return model.d <= 4

    model.con1 = Constraint(rule = con1)
    model.con2 = Constraint(rule = con2)
    model.con3 = Constraint(rule = con3)

    opt = SolverFactory('glpk')
    opt.solve(model).write()
    print('\n\nOptimal solution')
    print('Study:', model.e())
    print('Fun:', model.d())
    print('Value:', model.obj())


def showsell():
    #from pyomo.environ import *

    model = ConcreteModel()

    model.x1 = Var(domain = NonNegativeReals)
    model.x2 = Var(domain = NonNegativeReals)

    model.obj = Objective(expr = model.x1 + 25 * model.x2, sense = maximize)

    model.con1 = Constraint(expr = 15 * model.x1 + 300 * model.x2 <= 10000)
    model.con2 = Constraint(expr = model.x1 - 2 * model.x2 >= 0)
    model.con3 = Constraint(expr = model.x1 <= 400)

    opt = SolverFactory('glpk')
    opt.solve(model)
    print('Optimal solution:')
    print('Radio:', model.x1())
    print('TV:', model.x2())
    print('Efficiency:', model.obj())


def empregos():
    #from pyomo.environ import *

    model = ConcreteModel()

    model.x = Var([1,2], domain = NonNegativeReals)

    model.obj = Objective(expr = 8 * model.x[1] + 6 * model.x[2], sense = minimize)

    model.constraints = ConstraintList()
    model.constraints.add(expr = model.x[1] >= 5)
    model.constraints.add(expr = model.x[1] <= 12)
    model.constraints.add(expr = model.x[2] >= 6)
    model.constraints.add(expr = model.x[2] <= 10)
    model.constraints.add(expr = model.x[1] + model.x[2] >= 20)

    opt = SolverFactory('glpk')
    results = opt.solve(model)

    print('Status:', results.solver.status)
    print('Termination criterion:', results.solver.termination_condition)
    if results.solver.termination_condition == 'optimal':
        print('Total stress:', model.obj.expr())
        print(f'Opt. solution is {model.x[1].value}h at store 1 and {model.x[2].value}h at store 2!')


def oilco():
    #from pyomo.environ import *

    model = ConcreteModel()

    model.x = Var([1,2], domain = NonNegativeReals)

    model.obj = Objective(expr = model.x[1] + model.x[2], sense = minimize)

    model.constraints = ConstraintList()
    model.constraints.add(expr = 0.2 * model.x[1] + 0.1 * model.x[2] >= 14)
    model.constraints.add(expr = 0.25 * model.x[1] + 0.6 * model.x[2] >= 30)
    model.constraints.add(expr = 0.1 * model.x[1] + 0.15 * model.x[2] >= 10)
    model.constraints.add(expr = 0.15 * model.x[1] + 0.1 * model.x[2] >= 8)
    model.constraints.add(expr = 0.6 * model.x[1] - 0.4 * model.x[2] >= 0)
    
    opt = SolverFactory('glpk')
    opt.solve(model).write()
    print('\n\nOptimal solution')
    print('x1:', model.x[1]())
    print('x2:', model.x[2]())
    print('Value:', model.obj())


def daytrader():
    #from pyomo.environ import *

    model = ConcreteModel()

    model.x = Var([1,2], domain = NonNegativeReals)

    model.obj = Objective(expr = model.x[1] + model.x[2], sense = minimize)

    model.constraints = ConstraintList()
    model.constraints.add(expr = 0.1 * model.x[1] + 0.25 * model.x[2] >= 10000)
    model.constraints.add(expr = -0.6 * model.x[1] + 0.4 * model.x[2] <= 0)
    
    opt = SolverFactory('glpk')
    opt.solve(model).write()
    print('\n\nOptimal solution')
    print('x1:', model.x[1]())
    print('x2:', model.x[2]())
    print('Value:', model.obj())


empregos()