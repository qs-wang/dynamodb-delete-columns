import boto3


def scan_table_and_remove(profile, region, table, properties, primary):
    session = boto3.session.Session(profile_name=profile)
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table(table)
    scan = None

    count = 0
    while scan is None or 'LastEvaluatedKey' in scan:
        if scan is not None and 'LastEvaluatedKey' in scan:
            scan = table.scan(
                ProjectionExpression='#k',
                ExpressionAttributeNames={
                    '#k': primary
                },
                ExclusiveStartKey=scan['LastEvaluatedKey'],
            )
        else:
            scan = table.scan(ProjectionExpression=primary)

        for item in scan['Items']:
            remove_properties(table, primary, item[primary], properties)
            count = count + 1

    return count


def remove_properties(table, primary, key, properties):
    props = ','.join(properties)
    table.update_item(
        Key={primary: key},
        UpdateExpression='Remove {}'.format(props),
    )
