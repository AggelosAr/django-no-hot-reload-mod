from django.urls import include, path


urlpatterns = [
    path("code_modifier/", include("django_no_hot_reload_mod.src.code_modifier.urls")),
    path("", include("example_app.urls")),
]
