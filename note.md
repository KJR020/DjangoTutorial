# 学習ノート

- [学習ノート](#学習ノート)
  - [はじめての Django アプリ作成、その 1](#はじめての-django-アプリ作成その-1)
    - [プロジェクトを作成する](#プロジェクトを作成する)
    - [開発用サーバー](#開発用サーバー)
    - [Polls アプリケーションをつくる](#polls-アプリケーションをつくる)
    - [はじめてのビュー作成](#はじめてのビュー作成)
      - [path関数](#path関数)
  - [はじめての Django アプリ作成、その2](#はじめての-django-アプリ作成その2)
    - [Database の設定](#database-の設定)
      - [migrate](#migrate)
    - [モデルの作成](#モデルの作成)
    - [モデルを有効にする](#モデルを有効にする)
    - [API で遊んでみる](#api-で遊んでみる)
    - [Django Adminの紹介](#django-adminの紹介)
  - [初めてのDjangoアプリ作成、その3](#初めてのdjangoアプリ作成その3)
    - [オーバービュー](#オーバービュー)
    - [もっとビューを書いてみる](#もっとビューを書いてみる)
    - [実際に動作するビューを書く](#実際に動作するビューを書く)
    - [ショートカット: render()](#ショートカット-render)
    - [404 エラーの送出](#404-エラーの送出)
    - [ショートカット: get\_object\_or\_404()](#ショートカット-get_object_or_404)
    - [テンプレートシステムを使う](#テンプレートシステムを使う)
    - [テンプレート内のハードコードされたURLを削除](#テンプレート内のハードコードされたurlを削除)
    - [URL 名の名前空間](#url-名の名前空間)
  - [はじめての Django アプリ作成、その 4](#はじめての-django-アプリ作成その-4)
    - [簡単なフォームを書く](#簡単なフォームを書く)
    - [汎用ビューを使う: コードが少ないのはいいことだ](#汎用ビューを使う-コードが少ないのはいいことだ)
    - [URLconf の修正](#urlconf-の修正)
    - [views の修正](#views-の修正)
  - [参考](#参考)


最初に仮想環境を構築

`python -m venv .venv`

`pip install django`

## はじめての Django アプリ作成、その 1

### プロジェクトを作成する

### 開発用サーバー

### Polls アプリケーションをつくる

### はじめてのビュー作成

#### path関数

- 4つの引数を取る。`route`と`view`は必須。`kwargs`, `name`はoptional
- route: URLパターンを含む文字列。`urlpatterns`のパターンから始まる。リストを順に下から参照し、URLと一致するものを探す。
- view: マッチする正規表現を見つけると`view`関数が呼び出される。  
その際は、`HttpRequest`オブジェクトを第一引数。  
キーワード引数として、`route`からキャプチャされた値を渡す。
- kwargs: 任意のキーワード引数を辞書としてビューにわたす。
- name: urlに名前をつけておくと、Djangoのどこからでも参照できるらしい。便利そう。

## はじめての Django アプリ作成、その2

### Database の設定

#### migrate

migrateはバックエンドとなる。データベースの初期設定。テーブルの作成を行う。

>migrate コマンドは INSTALLED_APPS の設定を参照するとともに、 mysite/settings.py ファイルのデータベース設定に従って必要なすべてのデータベースのテーブルを作成します。このデータベースマイグレーションはアプリと共に配布されます (これらについては後ほどカバーします)。マイグレーションを実施するたび、メッセージを見ることになります。もしこれに興味を引かれたら、Djangoが作成したテーブルを表示するために、コマンドラインクライアントであなたのデータベースの種類に合わせて \dt (PostgreSQL)、SHOW TABLES; (MySQL)、 .tables (SQLite)、もしくは SELECT TABLE_NAME FROM USER_TABLES; (Oracle) とタイプしてみましょう。

SQLite以外のDBを使用する場合は、バインディングをインストールする必要がある。  
一旦SQLiteでチュートリアルを進めて、後ほど置き換える形で学習を進める

コマンド

```bash
python manage.py migrate
```

### モデルの作成

- モデルは本質的に、データベースのレイアウトと、それに付随するメタデータらしい
- Djangoの設計思想から、マイグレーションをモデルに含めているらしい。  
  - Ruby On Railsとの設計思想の違いはどこから生まれているのか気になった。

>設計思想
>
>モデルは、手持ちのデータに対する唯一無二の決定的なソースです。モデルには自分が格納したいデータにとって必要不可欠なフィー ルドと、そのデータの挙動を収めます。 Django は DRY 則 に従っています。 Django のモデルの目的は、ただ一つの場所でデータモデルを定義し、そこから自動的にデータを取り出すことにあります。
>
>これはマイグレーションを含みます - たとえば、Ruby On Rails と違って、マイグレーションは完全にモデルのファイルから生成されます。マイグレーションは本質的には単なる履歴です。Django はデータベーススキーマをアップデートしながら履歴を進んでいき、現在のモデルに合致させることができます。

modelは以下のように、models.pyを編集する。

```python
from django.db import models


class Question(models.Model):
    question_text = models.ChatField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey()
    choice = models.CharField(max_length=200)
    votes = models.IntegerChoices(default=0)
```

モデルはdjango.db.models.Modelのサブクラスとして作成する。  
各クラスは、クラス変数としてDBのテーブル列(フィールド)と対応する。  
モデル定義から自動的にテーブルスキーマを生成してくれる。

### モデルを有効にする

### API で遊んでみる

- インタラクティブモードでAPI操作。questionを追加

### Django Adminの紹介

## 初めてのDjangoアプリ作成、その3

### オーバービュー

- ビューとは、特定の機能を提供するWEBページの型である
- ページそれぞれ各々のテンプレートがある
- Djangoは返すビューを、リクエストされたURLから決定する
- URLパターンは下記のようなURLを一般化したもの  
  ex) `/newarchive/<year>/<month>/`
- DjangoはURLからビュー取得する際に、URLconfを仕様する

### もっとビューを書いてみる

- `/polls/34/`をリクエストすると、`ROOT_URLCONF`に指定された`mysite.urls`をロードする
- `urlspatterns`という変数を探し、順番にパターンを走査する
- `:`はコンバータとパターン名を区切る

### 実際に動作するビューを書く

### ショートカット: render()

- 引数として、requestオブジェクト、テンプレート名(str)、コンテキスト(辞書)
- `render`関数を使うと、テンプレートを指定のコンテキストでレンダリングし、HttpResponseオブジェクトを返す

### 404 エラーの送出

- リクエストしたIDをもつ質問が存在しないとき、Http404を返す
- 一般的化すると、リクエストしたURLに該当するオブジェクトが存在しないといった状況

### ショートカット: get_object_or_404()

- 404エラーを返すためのヘルパー関数, HttpResponseもしくはHttp404を返す
- 効率的にエラー処理をかける

### テンプレートシステムを使う

### テンプレート内のハードコードされたURLを削除

- 一部ハードコードしていた部分が存在した
  - `<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>`
- 以下のように変更。Djangoのテンプレート構文`{% url %}`で動的にURLを指定できる。
  - `<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>`

### URL 名の名前空間

- `polls/urls.py`に`app_name`変数を定義することで、URLconfに名前空間を追加できる

## はじめての Django アプリ作成、その 4

### 簡単なフォームを書く
- HTMLテンプレートにform要素を追加する
    
    ```HTML
    <form action="{% url 'polls:vote' question.id %}" method="post">
    {% csrf_token %}
    <fieldset>
        <legend><h1>{{ question.question_text }}</h1></legend>
        {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
        {% for choice in question.choice_set.all %}
            <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
            <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
        {% endfor %}
    </fieldset>
    <input type="submit" value="Vote">
    </form>
    ```
    
    - formタグの`action="{% url 'polls:vote' question.id %}"`ってなんだろうか？
        - どういう文法か？順番に引数として渡されるはず、positional argsとしてparseされる？
    - `forloop.counter`は`for`タグのる＾プから、何回ループが実行されたか？の回数
    - クロスサイトリクエストフォージェリ対策で、POSTフォームには、 `{% csrf_token %}` テンプレートタグを使う
        - HTML上は何も表示されないが、レンダリングされるとCSRF対策の隠しフォームが生成される
        `<input type='hidden' name='csrfmiddlewaretoken' value='X3tB3GHJyLr4n1UADOXe5jU6CvBvI6EP' />`   
        valueの値はランダムのトークンで、サーバー側での検証に使われる
            - 具体的にどうやって？使われるのか？
- `vote()`関数の実装
  
  ```Python
  from django.db.models import F
  from django.http import HttpResponse, HttpResponseRedirect
  from django.shortcuts import get_object_or_404, render
  from django.urls import reverse

  from .models import Choice, Question


  # ...
    def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(
                request,
                "polls/detail.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                },
            )
        else:
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
  ```
    - POSTデータに`choice`がない場合、`request.POST["choice"]`は`KeyError`を送出する
    - 
       

### 汎用ビューを使う: コードが少ないのはいいことだ


### URLconf の修正

### views の修正

## 参考

- 公式ドキュメント
  - https://docs.djangoproject.com/ja/5.0/
- コミットメッセージのprefixの付け方
  - https://qiita.com/muranakar/items/20a7927ffa63a5ca226a  
