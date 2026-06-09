import json
import boto3

def lambda_handler(event, context):
    try:
        # Parsear body
        body = json.loads(event.get('body', '{}'))
        
        tenant_id = body['tenant_id']
        alumno_id = body['alumno_id']

        # Proceso
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('t_alumnos')
        
        response = table.get_item(
            Key={'tenant_id': tenant_id, 'alumno_id': alumno_id}
        )
        
        # Salida
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'alumno': response['Item']
                })
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Alumno no encontrado'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
