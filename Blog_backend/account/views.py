from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import ProfileSerializer
from .models import Profile


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def accountOverView(request):
    api_urls = {
        "overview": "api/account/",
        "register": "api/account/register",
        "login": "api/account/login",
        "refresh": "api/account/refresh",
        "dashboard": "api/account/dashboard",
        "get User": "api/account/user/:pk",
        "update self": "api/account/dashboard/update",
        "delete account": "api/account/dashboard/delete",
    }
    return Response(api_urls, status=status.HTTP_200_OK)


@permission_classes([permissions.AllowAny])
@api_view(['POST'])
def registerView(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def dashboardView(request):
    user = request.user
    profile = Profile.objects.get(pk=user.id)

    if profile is not None:
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def updateSelfView(request):
    user = request.user
    profile = Profile.objects.get(pk=user.id)

    if profile is not None:
        serializer = ProfileSerializer(instance=profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def deleteSelfView(request):
    user = request.user
    profile = Profile.objects.get(pk=user.id)

    if profile is not None:
        profile.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def getUserView(request, pk):
    profile = Profile.objects.get(pk=pk)
    
    if profile is not None:
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)