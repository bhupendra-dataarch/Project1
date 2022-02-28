import boto3
ec2 = boto3.client('ec2', region_name='us-west-2')
ec2.start_instances(InstanceIds=['i-0abd28b94f096826a'])
#print('starting your instances: ' + str(instances))
#print(instances['InstanceId'])
