from django.urls import include, path
import content.views

# 二级路由
urlpatterns = [
    path('hello_world', content.views.hello_world)
]
