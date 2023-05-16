import boto3

def create_cloudwatch_alarm(instance_id):
    client = boto3.client('cloudwatch')

    alarm_name = 'CPUUsageAlarm'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    comparison_operator = 'GreaterThanThreshold'
    threshold = 80.0
    evaluation_periods = 5
    period = 60
    statistic = 'Average'
    alarm_description = 'Alarm when CPU usage exceeds 80% for 5 consecutive minutes'
    alarm_actions = []  # Specify the actions to perform when the alarm state is triggered

    dimensions = [
        {
            'Name': 'InstanceId',
            'Value': instance_id
        },
    ]


  response = client.put_metric_alarm(
        AlarmName=alarm_name,
        ComparisonOperator=comparison_operator,
        EvaluationPeriods=evaluation_periods,
        MetricName=metric_name,
        Namespace=namespace,
        Period=period,
        Statistic=statistic,
        Threshold=threshold,
        ActionsEnabled=True,
        AlarmActions=alarm_actions,
        AlarmDescription=alarm_description,
        Dimensions=dimensions
    )

    print(f"CloudWatch alarm '{alarm_name}' created successfully.")

# Replace 'INSTANCE_ID' with your actual EC2 instance ID
instance_id = 'INSTANCE_ID'

create_cloudwatch_alarm(instance_id)
