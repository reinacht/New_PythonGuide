def force(mass, a):
    return str(mass * a) + 'N'

def weight(mass):
    return str(mass * 9.8) + 'N'

def pressure(f, A):
    return str(f / A) + 'Pa'


## listrik
def resistant1(V, I):
    return str(V / I) + 'Ω'

def resistant2(rho:float , l:float, A:float):
    return str(rho * (l / A)) + 'Ω'

