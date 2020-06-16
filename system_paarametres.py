import psutil
import os

#CPU stats
CPU_Count = psutil.cpu_count(logical=False)
print("CPU Count: " + str(CPU_Count) )

CPU_percent = psutil.cpu_percent(interval=None)
print("CPU Percent: "+ str(CPU_percent))

#Virtual Memory

Virtual_memory = psutil.virtual_memory().available
Virtual_memory = Virtual_memory / (1024 * 1024 )
print("Available Memory : "+ str(Virtual_memory))

#swap memory
swap_memory = psutil.swap_memory().free/(1024*1024)
print("Available swap Memory : "+ str(swap_memory))

#Disk Usage 
disk_usage = psutil.disk_usage('/').free/(1024*1024)
print("Disk Usage :" + str(disk_usage))

Disk_read_time = psutil.disk_io_counters().read_time
print("Disk read time :  " + str(Disk_read_time))

Disk_write_time = psutil.disk_io_counters().write_time
print("Disk Write Time : " + str(Disk_write_time))

#network Statistics
packets_sent = psutil.net_io_counters().packets_sent
print("packets sent " + str(packets_sent))

packets_received = psutil.net_io_counters().packets_recv
print("packets received " + str(packets_received))

#http reponse time 
cmd= 'curl -s -w %{time_total}\\n -o /dev/null http://www.google.com'
os.system(cmd)
