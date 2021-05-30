from django.urls import path, register_converter, re_path
from .convertes import YearConverter
from .views import (by_year_posts, posts_view, detail_view)

app_name="posts"
register_converter(YearConverter, "yyyy")

urlpatterns = [
    path("", posts_view),
    path("<int:id>", detail_view, name="detail_view"),
    path("<yyyy:year>", by_year_posts, {"month":"Enero"}, name="posts_by_year"),
    re_path(r"(?P<year>[0-9]{4})", by_year_posts, name="by_year_regex"),

]

"""
Lo que pasa Django como argumentos a la view
1. request (objeto HTTPRequest)
2. url args , en el orden correspondiente

tipos de datos que Djanog hace match
-int
-str
-slug
-uuid
-path

usando group names in regex:
(?P<name>pattern)

Extra args for the view, 3 tercer argumento opcional
path("strig", view, {'name': value} )

Reverse
El proceso de contruir una url a partir de objetos Python.
reverse(namespace:name, karg)
"""