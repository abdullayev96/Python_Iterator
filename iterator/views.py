from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer




###############  Default holatda


#
# class UserListIteratorView(APIView):
#     def get(self, request):
#         try:
#             users = User.objects.all()
#             serializers = UserSerializer(users, many=True)
#
#             return Response(serializers.data, status=status.HTTP_200_OK)
#
#         except Exception as e:
#             return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)



#############   Iterator bilan 5000 ++++ foydalanuvchi bolganda effitniy


class UserListIteratorView(APIView):
    def get(self, request):
        users = User.objects.all().iterator(chunk_size=1000)  # 🔁 Iterator ishlatilmoqda
        serialized_data = []

        for user in users:
            serializer = UserSerializer(user)
            serialized_data.append(serializer.data)

        return Response(serialized_data)
