from fastapi import Depends

def global_dep()-> None:
    print("------------ This is global dependency")


GlobalDep = Depends(global_dep)