python3 -m da -H 10.142.0.2 -n OlympusNode -f --logfilename case12.log --message-buffer-size=$((64*1024)) -D Olympus.da
python3 -m da -H 10.142.0.2 -n ReplicaNode -f --logfilename case12.log --message-buffer-size=$((64*1024)) -D Replica.da
python3 -m da -H 10.142.0.2 -n ReplicaNode -f --logfilename case12.log --message-buffer-size=$((64*1024)) -D Client.da
#python3 -m da -H 10.142.0.5 -n MasterNode -f --logfilename logfile.txt --message-buffer-size=$((64*1024)) -D __init__.da system.conf