import psutil
#import os

#CPU stats
CPU_Count = psutil.cpu_count(logical=False)*10
print(CPU_Count)

#CPU_percent = psutil.cpu_percent(interval=None)
#print(CPU_percent)

#Virtual Memory

Virtual_memory = psutil.virtual_memory().available
Virtual_memory = Virtual_memory / (1024 * 1024 * 100)
print(Virtual_memory)

#Inactive_memory = psutil.virtual_memory().inactive / (1024 * 1024)
#print("Inactive Memory")
#print(Inactive_memory)

#swap memory
#swap_memory = psutil.swap_memory().free/(1024*1024)
#print(swap_memory)

#Disk Usage 
disk_usage_total = psutil.disk_usage('/').total/(1024*1024 *1024)
print(disk_usage_total)

disk_usage = psutil.disk_usage('/').free/(1024*1024 *1024)
print(disk_usage)

#Disk_read_time = psutil.disk_io_counters().read_time
#print(Disk_read_time)

#Disk_write_time = psutil.disk_io_counters().write_time
#print(Disk_write_time)

#network Statistics
#packets_sent = psutil.net_io_counters().packets_sent
#print(packets_sent)

#packets_received = psutil.net_io_counters().packets_recv
#print(packets_received)

#user_time = psutil.cpu_times().user / 1000
#print("user time")
#print(user_time)

#system_time = psutil.cpu_times().system /1000
#print("system time")
#print(system_time)

#idle_time = psutil.cpu_times().idle /1000
#print("Idle time")
#print(idle_time)

cpu_freq = int(psutil.cpu_freq().current/100)
#print("cpu_freq")
print(cpu_freq)

#ctx_switeches = psutil.cpu_stats().ctx_switches
#print("ctx_switches")
#print(ctx_switeches)
