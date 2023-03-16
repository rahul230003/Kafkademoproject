from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from kafka import KafkaProducer
import json


def myview(request):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    task_id = "1234"
    task_name = "Process data"
    producer.send('sampleTopic', {'task_id': task_id, 'task_name': task_name})
    return HttpResponse("Task assigned")

