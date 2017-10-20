from subprocess import call
call(['lxterminal', '-e', "", "python -m da -n ClientNode -D Client.da"])
call(['lxterminal', '-e', "python -m da -n ReplicaNode -D Replica.da"])
call(['lxterminal', '-e', "python -m da -n OlympusNode -D Olympus.da"])
call(['lxterminal', '-e', "python -m da -M -n init __init__.da"])





