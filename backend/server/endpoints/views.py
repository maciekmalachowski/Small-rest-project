from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import pandas as pd
import json

class BaseRowsView(APIView): # Outputs 3 persons with id 0-2
    def get(self, request, **kwargs):
        self.data = pd.read_csv('jupyter-files/df.csv')
        id_min = 0
        id_max = 2

        details_of_person = []
        for index in range(id_min, id_max+1):
            all_people = json.loads(self.data.to_json(orient='records'))
            details_of_person.append(all_people[index])
        return Response(details_of_person)

class SingleRowView(APIView): #Outputs single person
    def get(self, request, **kwargs):
        self.data = pd.read_csv('jupyter-files/df.csv')
        try:
            id = int(kwargs.get('id', None))
            if id < 0:
                return Response("Wrong values in http link. Values must be greater than 0.", status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response("Wrong values in http link. Try to change it to integers.", status=status.HTTP_400_BAD_REQUEST)

        details_of_person = []
        all_people = json.loads(self.data.to_json(orient='records'))
        details_of_person.append(all_people[id])
        return Response(details_of_person)

class ManyRowsView(APIView): #Outputs many persons
    def get(self, request, **kwargs):
        self.data = pd.read_csv('jupyter-files/df.csv')
        try:
            id_min = int(kwargs.get('id_min', None))
            id_max = int(kwargs.get('id_max', None))
            if id_min < 0 or id_max < 0:
                return Response("Wrong values in http link. Values must be greater than 0.", status=status.HTTP_400_BAD_REQUEST)
            if id_min > id_max:
                return Response("Wrong values in http link. First value must be less than the second.", status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response("Wrong values in http link. Try to change it to integers.", status=status.HTTP_400_BAD_REQUEST)

        details_of_person = []
        for index in range(id_min, id_max+1):
            all_people = json.loads(self.data.to_json(orient='records'))
            details_of_person.append(all_people[index])
        return Response(details_of_person)