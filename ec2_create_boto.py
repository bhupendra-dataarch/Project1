import boto3
def create_instance():
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    instances = ec2_client.run_instances(
        ImageId="ami-0b2f7a874cbfc4d53",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro")
    print(instances["Instances"][0]["InstanceId"])

    

if __name__ == "__main__":
    create_instance()
