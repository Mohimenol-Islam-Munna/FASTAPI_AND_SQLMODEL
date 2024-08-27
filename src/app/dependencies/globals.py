from fastapi import Depends

def global_dep()-> str:
    print("This is global dependency")


GlobalDep = Depends(global_dep)