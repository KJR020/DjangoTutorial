# 学習ノート

- [学習ノート](#学習ノート)
  - [やったことメモ](#やったことメモ)
    - [はじめてのビュー作成](#はじめてのビュー作成)
      - [path関数](#path関数)
    - [Databaseの設定](#databaseの設定)
      - [migrate](#migrate)
    - [モデルの作成](#モデルの作成)
  - [参考](#参考)

## やったことメモ

最初に仮想環境を構築

`python -m venv .venv`

`pip install django`

### はじめてのビュー作成

#### path関数

- 4つの引数を取る。`route`と`view`は必須。`kwargs`, `name`はoptional
- route: URLパターンを含む文字列。`urlpatterns`のパターンから始まる。リストを順に下から参照し、URLと一致するものを探す。
- view: マッチする正規表現を見つけると`view`関数が呼び出される。  
その際は、`HttpRequest`オブジェクトを第一引数。  
キーワード引数として、`route`からキャプチャされた値を渡す。
- kwargs: 任意のキーワード引数を辞書としてビューにわたす。
- name: urlに名前をつけておくと、Djangoのどこからでも参照できるらしい。便利そう。

### Databaseの設定

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

モデルは本質的に、データベースのレイアウトと、それに付随するメタデータらしい

設計思想として、マイグレーションをモデルに含めているらしい。  
Ruby On Railsとの設計思想の違いはどこから生まれているのか気になった。

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

## 参考

- https://qiita.com/muranakar/items/20a7927ffa63a5ca226a  
コミットメッセージのprefixの付け方
