import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')
filters = [{"Name": "tag:Project", "Values":["learn_python"]}]

@click.command()
def list_instances():
    for i in ec2.instances.filter(Filters=filters):
        print(", ".join((
            i.id,
            i.instance_type,
            i.placement["AvailabilityZone"],
            i.state['Name'],
            i.public_dns_name
        )))

if __name__ == '__main__':
    print(list_instances())
