import json
import boto3


def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        tenant_id = body.get('tenant_id')
        alumno_id = body.get('alumno_id')

        if not tenant_id or not alumno_id:
            return {'statusCode': 400, 'body': json.dumps({'error': 'tenant_id y alumno_id requeridos'})}

        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('t_alumnos')

        item = {
            'tenant_id': tenant_id,
            'alumno_id': alumno_id,
            'alumno_datos': body.get('alumno_datos', {})
        }

        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps({
                "statusCode": 200,
                "message": "Alumno creado exitosamente",
                "data": item
            })
        }
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
