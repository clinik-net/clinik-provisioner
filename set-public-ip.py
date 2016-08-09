import boto3
import json
import time
from pprint import pprint

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

with open('instance.json') as data_file:    
    data = json.load(data_file)

instanceId = data["Instances"][0]["InstanceId"]
ready = True

while (ready):
    instance = ec2.Instance(instanceId)
    print "Waiting instance to be ready... (", instance.state["Name"], ")"
    if (instance.state["Name"] == 'running'):
        ready = False
    time.sleep(5)

client = boto3.client('ec2')
client.associate_address(InstanceId=instanceId, PublicIp='52.67.122.104', AllowReassociation=True)
print "Associating public ip 52.67.122.104 to instance ", instanceId, "..."
