// コンテナにインスペクション
$ docker-compose exec node bash

// コンテナ内でAngularアプリ作成
root@8dfd8ec7933f:/projects# ng new angular-app

// 引き継ぐ場合(gitで共有された場合など)
root@8dfd8ec7933f:/projects# npm install

// 作成したAngularアプリ直下に移動
root@8dfd8ec7933f:/projects# cd /projects/angular-app

// Angularアプリの起動
root@8dfd8ec7933f:/projects/angular-app# ng serve --host 0.0.0.0
