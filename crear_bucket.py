import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']

    s3 = boto3.client('s3')
    try:
        s3.create_bucket(Bucket=nombre_bucket)
        mensaje = f"Bucket '{nombre_bucket}' creado correctamente."
        status = 200
    except Exception as e:
        mensaje = f"Error al crear bucket: {str(e)}"
        status = 500

    # Salida
    return {
        'statusCode': status,
        'body': {
            'mensaje': mensaje
        }
    }