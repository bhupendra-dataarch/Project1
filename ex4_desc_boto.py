import boto3

client = boto3.client("ec2" , region_name ="us-west-2")
print(Hello)

response = client.describe_instances(
	Filters=[
	{

	'Name': 'instance-state-name' ,
	'Values': ['running']

	}

			])

#print(response)

for reservation in response['Reservations']:
	for inst in reservation['Instances']:
		print(inst['InstanceId'])
