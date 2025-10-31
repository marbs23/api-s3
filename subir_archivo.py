import boto3
import base64

def lambda_handler(event, context):
    # Entrada (json)
    bucket = event['body']['bucket']
    directorio = event['body'].get('directorio', '')
    nombre_archivo = event['body']['archivo']
    contenido_base64 = event['body']['contenido']

    if directorio and not directorio.endswith('/'):
        directorio += '/'

    # Decodificar contenido Base64
    try:
        contenido_bytes = base64.b64decode(contenido_base64)
    except Exception:
        return {'statusCode': 400, 'body': {'mensaje': 'Contenido Base64 inválido'}}

    s3 = boto3.client('s3')
    key = f"{directorio}{nombre_archivo}"

    try:
        s3.put_object(Bucket=bucket, Key=key, Body=contenido_bytes)
        mensaje = f"Archivo '{nombre_archivo}' subido correctamente a '{bucket}/{key}'."
        status = 200
    except Exception as e:
        mensaje = f"Error al subir archivo: {str(e)}"
        status = 500

    # Salida
    return {
        'statusCode': status,
        'body': {
            'mensaje': mensaje
        }
    }
