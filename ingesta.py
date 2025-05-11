import boto3

ficheroUpload = "usuarios.csv"
ficheroUpload2 = "direccion.csv"
nombreBucket = "usuarios-cloud-pp"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, "usuarios/usuarios.csv")
response2 = s3.upload_file(ficheroUpload2, nombreBucket, "direccion/direccion.csv")

print("Ingesta completada")
