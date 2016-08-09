import boto3
import json

ec2 = boto3.resource('ec2')

with open('old.json') as data_file:    
    data = json.load(data_file)

instanceId = data["Instances"][0]["InstanceId"]
instance = ec2.Instance(instanceId)
print "Destroying old instance..."
instance.terminate()
