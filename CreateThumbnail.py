from __future__ import print_function
import boto3
import os
import sys
import uuid
from PIL import Image
import PIL.Image
     
s3_client = boto3.client('s3')
s3 = boto3.resource('s3')     



def resize_image(image_path, resized_path, predefine_size):
	with Image.open(image_path) as image:
		size = predefine_size
		image.thumbnail(size)
		image.save(resized_path)



def handler(event, context):
	for record in event['Records']:
		
		### Get the metadat of image and bucket
		bucket = record['s3']['bucket']['name']
		key = record['s3']['object']['key'] 
		print("Bucket is : ", bucket)
		print("Key is : ", key)

		### Get Image from S3
		image = s3.meta.client.download_file(bucket, key, '/tmp/1.jpg')


		### Resize the image to 200x200 px and store that to S3
		reside_local_path = '/tmp/w2.jpg'
		resize_image('/tmp/1.jpg', reside_local_path, (200, 200))
		s3_client.upload_file(reside_local_path, bucket, 'w2/'+extract_file_name(key))

		### Resize the image to 400x400 px and store that to S3
		reside_local_path = '/tmp/w4.jpg'
		resize_image('/tmp/1.jpg', reside_local_path, (400, 400))
		s3_client.upload_file(reside_local_path, bucket, 'w4/'+extract_file_name(key))

		### Resize the image to 600x600 px and store that to S3
		reside_local_path = '/tmp/w6.jpg'
		resize_image('/tmp/1.jpg', reside_local_path, (600, 600))
		s3_client.upload_file(reside_local_path, bucket, 'w6/'+extract_file_name(key))


		print("Extract file name is : ",extract_file_name(key))
		print("Done")




def extract_file_name(path):
	return path.split("/")[1]






