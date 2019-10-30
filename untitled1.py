from const import gpad 
def energy_func(mi, ha, vo):
     """ функция, определяющую полную механическую энергию тела, 
         подброшенного на определенную высоту и определенной скоростью 
         над поверхностью Земли
     """
     Ep=mi*gpad*ha
     Ek=(mi*vo**2)/2
     E=Ep+Ek
     
     return E


print(energy_func(10, 23, 3))

