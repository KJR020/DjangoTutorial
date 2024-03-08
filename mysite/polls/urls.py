from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# /polls/34/へのアクセスがあると、
# DjangoはROOT_URLCONFで指定されたPythonモジュールにmysite.urlsを渡す。
# モジュール内のurlpatternsという変数を探し、順番にパターンを走査する。
# polls/にマッチした箇所が見つかった際に、一致した文字列("polls/")を取り除く
# 残りの文字列を`polls.urls`のURLconfにわたす。
#
