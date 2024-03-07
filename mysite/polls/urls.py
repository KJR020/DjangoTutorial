from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/", views.vote, name="vote"),
]

# /polls/34/へのアクセスがあると、
# DjangoはROOT_URLCONFで指定されたPythonモジュールにmysite.urlsを渡す。
# モジュール内のurlpatternsという変数を探し、順番にパターンを走査する。
# polls/にマッチした箇所が見つかった際に、一致した文字列("polls/")を取り除く
# 残りの文字列を`polls.urls`のURLconfにわたす。
#
