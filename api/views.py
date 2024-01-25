from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from .functions import remove_bg, get_country_code
from django.conf import settings
from .models import MobileApp, Country
import os
# Create your views here.

IMAGE_FILES = [
    "jpg",
    'jpeg',
    'png',
    'webp',
]


class RemoveBg(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        try:
            # secret_key = request.data.get('api_key', None)
            # package = request.data.get('packagename', None)
            # time = request.data.get('time', None)
            # country_code = get_country_code(time)
            #
            # if country_code['status'] == False:
            #     return JsonResponse({
            #         "status": "failed",
            #         "message": f'{country_code["data"]["message"]}',
            #         "data": None
            #     },
            #         status=status.HTTP_400_BAD_REQUEST,
            #         safe=False
            #     )
            # if not MobileApp.objects.filter(token=secret_key, package_name=package, is_active=True).exists():
            #     return JsonResponse({"status": 'failed', "message": f"invalid api-key/packagename", "data": None},
            #                         status=status.HTTP_400_BAD_REQUEST)

            img = request.FILES.get('img')
            file_extension = os.path.splitext(img.name)[1]
            file_extension = file_extension.lstrip(".")

            if not file_extension.lower() in IMAGE_FILES:
                return JsonResponse({
                    "status": "failed",
                    "message": 'Unsupported file type: {}'.format(file_extension),
                    "data": None
                },
                    status=status.HTTP_400_BAD_REQUEST,
                    safe=False
                )

            res = remove_bg(img)
            return JsonResponse({"status": "success", "message": None, "data": request.build_absolute_uri(settings.MEDIA_URL+res)})

        except Exception as e:
            print(e)
            return JsonResponse({"status": 'failed', "message": "Something went wrong...", "data": None},
                                status=status.HTTP_400_BAD_REQUEST)