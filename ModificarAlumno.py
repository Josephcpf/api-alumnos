import json
import boto3

def lambda_handler(event, context):
    try:
        # Parsear body
        body = json.loads(event.get('body', '{}'))
        
        tenant_id = body['tenant_id']
        alumno_id = body['alumno_id']
        alumno_datos = body['alumno_datos']

        # Proceso
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('t_alumnos')
        
        response = table.update_item(
            Key={'tenant_id': tenant_id, 'alumno_id': alumno_id},
            UpdateExpression="SET alumno_datos = :datos",
            ExpressionAttributeValues={':datos': alumno_datos},
            ReturnValues="ALL_NEW"
        )
        
        # Salida
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Alumno modificado exitosamente',
                'data': response.get('Attributes')
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
