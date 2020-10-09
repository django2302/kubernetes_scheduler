#!/usr/bin/env python

import time
import random
import json
import sys
import subprocess
import socket
from kubernetes import client, config, watch
from sdcclient import SdcClient


BestNode = subprocess.check_output([sys.executable, "topsisWithoutPrint.py"])

#print(type(BestNode))
BestNode = BestNode.strip()
#hostname = getHostname(BestNode)
#print(hostname)


def getHostname (IP):
	hosts = open('/etc/hosts' , 'r')
	hostname = []
	#bestHostname = 'Temp'
	print("Input IP is " + IP)
	#print(len(hostname[3][0]))
	for line in hosts:
		hostname.append(line.split())
	length = len(hostname)

	for i in range(length):
		#print (hostname[i][0])
		if hostname[i][0] == IP:
			#print(hostname[i][1])
			#print('here')
			return hostname[i][1]

#print(bestHostname)

hostname = getHostname(BestNode)
print(hostname)


config.load_kube_config()
v1 = client.CoreV1Api()
scheduler_name = "sysdigsched"



def nodes_available():
    ready_nodes = []
    for n in v1.list_node().items:
            for status in n.status.conditions:
                if status.status == "True" and status.type == "Ready":
                    ready_nodes.append(n.metadata.name)
    return ready_nodes


def schedule(name, node, namespace='default'):
    target = client.V1ObjectReference(kind = 'Node', api_version = 'v1', name = node)
    meta = client.V1ObjectMeta(name = name)
    body = client.V1Binding(target = target, metadata = meta)
    try:
        client.CoreV1Api().create_namespaced_binding(namespace=namespace, body=body)
    except ValueError:
        print ("Exception")

   


def main():
    w = watch.Watch()
    for event in w.stream(v1.list_namespaced_pod, "default"):
        if event['object'].status.phase == "Pending" and event['object'].spec.scheduler_name == scheduler_name:
            try:
                print "Scheduling " + event['object'].metadata.name
                res = schedule(event['object'].metadata.name, hostname)
            except client.rest.ApiException as e:
                print json.loads(e.body)['message']


if __name__ == '__main__':
    main()  
