from django.shortcuts import render
from .models import Person,Employe
from .serializers import PersonSerializer,RegisterSerializer,LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.


class PersonsView(APIView):

    def get(self, request):
        try:

            persons = Person.objects.all()
            serializer = PersonSerializer(persons, many = True)

            return Response({
                'data' : serializer.data,
                'message':'Presons fetched successfully..',
            }, status= status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                    'data':{},
                    'message':'someting went wrong',

                }, status= status.HTTP_400_BAD_REQUEST)
        
    
    def post(self, request):

        try:

            data = request.data
            sserializer = PersonSerializer(data = data)

            if not sserializer.is_valid():
                return Response({
                    'data':sserializer.errors,
                    'message':'someting went wrong',
                }, status= status.HTTP_400_BAD_REQUEST)
            
            sserializer.save()

            return Response({
                'data': sserializer.data,
                'message':'person created successfully..',

            }, status= status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                    'data':{},
                    'message':'someting went wrong',

                }, status= status.HTTP_400_BAD_REQUEST)
        


    def patch(self, request):

        try:
            data = request.data
            person_obj = Person.objects.filter(id = data['id'])

            if not person_obj.exists():
                return Response({
                    'data':{},
                    'message':'invalid person id',
                }, status= status.HTTP_400_BAD_REQUEST)
            
            serializer = PersonSerializer(person_obj, data = data, partial = True)

            if not serializer.is_valid():
                return Response({
                    'data':serializer.errors,
                    'message':'someting went wrong',
                }, status= status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                'data': serializer.data,
                'message':'person Updated successfully..',

            }, status= status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                    'data':{},
                    'message':'someting went wrong',

                }, status= status.HTTP_400_BAD_REQUEST)
        
    

    def delete(self, request):
        try:
            data = request.data
            person_obj = Person.objects.filter(id = data['id'])

            if not person_obj.exists():
                return Response({
                    'data':{},
                    'message':'invalid person id',
                }, status= status.HTTP_400_BAD_REQUEST)
            
            person_obj.delete()

            return Response({
                'data': {},
                'message':'person deleted successfully..',

            }, status= status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                    'data':{},
                    'message':'someting went wrong',

                }, status= status.HTTP_400_BAD_REQUEST)



class PersonViewset(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class EmployeViewset(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Employe.objects.all()



class RegisterView(APIView):

    def post(self, request):

        try:
            data = request.data

            serializer = RegisterSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    'data':serializer.errors,
                    'message':'someting went wrong',
                }, status= status.HTTP_400_BAD_REQUEST)
            
            serializer.save()


            return Response({
                'data':{},
                'message':'your account is created',

            }, status= status.HTTP_201_CREATED)
            

        except Exception as e:
            return Response({
                    'data':{},
                    'message':'someting went wrong',

                }, status= status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):

    def post(self, request):

        try:
            data = request.data
            serializer = LoginSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    'data':serializer.errors,
                    'message':'someting went wrong',

                }, status= status.HTTP_400_BAD_REQUEST)
            

            response  =  serializer.get_jwt_token(serializer.data)


            return Response(response, status = status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                    'data':{},
                    'message':'someting went wrong',

                }, status= status.HTTP_400_BAD_REQUEST)