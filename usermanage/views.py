import json

from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.views.generic import View
from django.http import JsonResponse
from django.db.utils import IntegrityError
from .models import Users


# Create your views here.
class UsersView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(UsersView, self).dispatch(request, *args, **kwargs)

    def get(self, request, pk=0):
        if pk:
            try:
                user = Users.objects.get(pk=pk)
                user = model_to_dict(user)
                return JsonResponse({'code': 200, 'message': 'success', 'data': user}, status=200)
            except Users.DoesNotExist:
                return JsonResponse({'code': 404, 'message': '用户不存在'}, status=200)
        data = json.loads(request.body) if request.body else {}
        users = list(Users.objects.filter(**data).all().values())
        return JsonResponse({'code': 200, 'message': 'success', 'data': users}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        try:
            user = Users.objects.create(**data)
            user = model_to_dict(user)
            return JsonResponse({'code': 201, 'message': 'created', 'data': user}, status=201)
        except IntegrityError:
            return JsonResponse({'code': 400, 'message': '身份证号码已存在！'}, status=200)

    def put(self, request, pk=0):
        data = json.loads(request.body)
        user = Users.objects.get(pk=pk)
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        user = model_to_dict(user)
        return JsonResponse({'code': 200, 'message': 'updated', 'data': user}, status=200)

    def delete(self, request, pk=0):
        user = Users.objects.get(pk=pk)
        user.delete()
        return JsonResponse({'code': 204, 'message': 'deleted'}, status=204)
