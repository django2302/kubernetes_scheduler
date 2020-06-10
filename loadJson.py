# Python program to read
# json file


import json
import os

#execute a kubectl command
cmd='kubectl get nodes -o json > /tmp/newValues.json'
os.system(cmd)

# JSON file
f = open ('/tmp/newValues.json', "r")

# Reading from file
data = json.loads(f.read())

hostname  =[]
cpu = []
epi_storage = []
memory = []

for p in data['items']:
        hostname.append(p['metadata']['labels']['kubernetes.io/hostname'])
        cpu.append(p['status']['allocatable']['cpu'])
        epi_storage.append(p['status']['allocatable']['ephemeral-storage'])
        memory.append(p['status']['allocatable']['memory'])
f.close()

length = len(memory)

# Iterating the index
# same as 'for i in range(len(list))'
for i in range(length):
    if memory[i].endswith('Ki'):
        memory[i]=memory[i][:-2]


print (hostname)
print (cpu)
print (epi_storage)
print (memory)
