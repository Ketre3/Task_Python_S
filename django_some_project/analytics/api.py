from django.db.models import Count, F
from django.utils.dateparse import parse_date

from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Account
from post.models import Like


class LikesStatisticView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        date_from = parse_date(request.GET['date_from'])
        date_to = parse_date(request.GET['date_to'])
        aggregated_likes = Like.objects.values(date=F('updated_at')) \
                                        .filter(updated_at__gte=date_from, updated_at__lte=date_to) \
                                        .annotate(count=Count("id"))
        return Response(aggregated_likes)


class UserStatisticView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username, format=None):
        user = get_object_or_404(Account, username=username)
        data = {
            "username": username,
            "last_login": user.last_login,
            "last_activity": user.last_activity,
        }
        return Response(data)
