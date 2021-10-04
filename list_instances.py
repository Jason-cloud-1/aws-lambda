#!/bin/python
import boto3
INSTANCE_STATE = 'running'
AWS_REGION = "ap-northeast-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)

instances = EC2_RESOURCE.instances.all()
instances = EC2_RESOURCE.instances.filter(
            Filters=[
                        {
                                        'Name': 'instance-state-name',
                                                    'Values': [
                                                                        INSTANCE_STATE
                                                                                    ]
                                                            }
                               ]
             ) 
for instance in instances: 
        print(f' - 实例状态： {instance.state["Name"]} ID: {instance.instance_id} 子网ID- {instance.subnet_id} 密钥： {instance.key_name} IP 地址：{instance.public_ip_address}') 
