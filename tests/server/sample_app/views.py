from django.http import JsonResponse


def sample(request):
    return JsonResponse({"message": "original"})
