#Implementacion de Sysprep para personalizacion de imagen
#Codigo creado por Eguis Suarez - Especialista TI Fcom Spa

import os
import subprocess
from Bloatware import Bloatware


#Eliminacion de Bloatware de Windows

def Bloat_Command(Bloatware):
    for Bloat in Bloatware:
        subprocess.run(["powershell", "Get-AppxProvisionedPacke", "-Online", "|", "Where-Object", f"DisplayName -Like '{Bloat}'", "|", "Remove-AppxProvisionedPackage", "-Online"])
        print(f"Eliminando paquetes {Bloat}")

Bloat_Command()