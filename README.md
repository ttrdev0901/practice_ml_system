# practice_ml_system

## Fast API
- [公式](https://fastapi.tiangolo.com/ja)
- セキュリティ:
    - https://fastapi.tiangolo.com/ja/tutorial/security/first-steps/
    - https://fastapi.tiangolo.com/ja/tutorial/security/oauth2-jwt/


## SQLAlchemy
- https://docs.sqlalchemy.org/en/14/orm/tutorial.html
## docker
- mysql
    - https://hub.docker.com/_/mysql
    - timezone
    - https://salumarine.com/checking-timezone-on-mysql/
-postgresql
    - https://hub.docker.com/_/postgres

## .pthファイルでインポート設定
- https://www.sejuku.net/blog/66459

# VScode
- python language server
    - Pylanceだとsqlalchemyの補完がいまいち: declarative_baseが出ない
    - Jediに変更

# Curl
```bash
curl -X POST \
http://localhost:8000/projects/ \
-H 'Content-Type: application/json' \
-d '{"project_name": "sample_project", "description": "description"}'
```

### タスク
- DB Migration導入
    - https://alembic.sqlalchemy.org/en/latest/

- ユーザー認証
以下の順番で学習していく
1. 公式のセキュリティをやる
2. FastAPI-loginなどの拡張機能を試す

- appをdocker-composeに含める

- appのRemote-container設定

- テキストを進める