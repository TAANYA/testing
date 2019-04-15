from ortools.linear_solver import pywraplp
import numpy as np


def main(n):
    solver = pywraplp.Solver("n_queens",pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    
    x = [[solver.IntVar(0,1,'x%i%i' %(i,j)) for i in range(n)] for j in range(n)]
    
    solver.Minimize(0)
    constraint1 = [solver.Constraint(1,1) for i in range(n)]
    constraint2 = [solver.Constraint(1,1) for i in range(n)]
    constraint3 = [solver.Constraint(0,1) for i in range(n-1)]
    constraint4 = [solver.Constraint(0,1) for i in range(n-2)]
    constraint5 = [solver.Constraint(0,1) for i in range(n-2)]
    constraint6 = [solver.Constraint(0,1) for i in range(n-2)]
    constraint7 = solver.Constraint(0,1)
    for i in range(n):
        for j in range(n):
            constraint1[i].SetCoefficient(x[i][j],1)
    for j in range(n):
        for i in range(n):
            constraint2[j].SetCoefficient(x[i][j],1)
    for d in range(2,n+1):
        for i in range(d):
            constraint3[d-2].SetCoefficient(x[d-i-1][i],1)
    for d in range(2,n):
        for i in range(n-d+1):
            constraint4[d-2].SetCoefficient(x[n-i-1][d+i-1],1)
    for i in range(n):
        constraint7.SetCoefficient(x[i][i],1)
    for k in range(2,n):
        for i in range(k):
            constraint5[k-2].SetCoefficient(x[i][i+n-k],1)
            constraint6[k-2].SetCoefficient(x[i+n-k][i],1)
    
    result_status = solver.Solve()
    if result_status == solver.OPTIMAL:
        print("Optimal")
        for i in range(len(x)):
            for j in range(n):
                print(x[i][j].solution_value(),end='\t')
            print("\n")

    else:
        print("Infeasible")
    
        
if __name__ == "__main__":
    main(8)