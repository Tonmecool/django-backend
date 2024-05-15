from django.http import HttpRequest
from django.urls import path

from ninja import NinjaAPI

from core.api.schemas import PingResponseSchema


api = NinjaAPI()


@api.get("/ping", response=PingResponseSchema)
def ping(request: HttpRequest) -> PingResponseSchema:
    return PingResponseSchema(result=True)


urlpatterns = [
    path("", api.urls),
]
