import boto3

def lambda_handler(event, context):
    # Entrada (json)
    bucket = event['body']['bucket']
    directorio = event['body']['directorio']

    if not directorio.endswith('/'):
        directorio += '/'

    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=bucket, Key=directorio)
        mensaje = f"Directorio '{directorio}' creado en bucket '{bucket}'."
        status = 200
    except Exception as e:
        mensaje = f"Error al crear directorio: {str(e)}"
        status = 500

    # Salida
    return {
        'statusCode': status,
        'body': {
            'mensaje': mensaje
        }
    }
