nosetestを実行する場合の注意

○ GAEクラスを利用する場合の、GAEパス指定(Windowsの場合)
noseGAEを利用する場合、GAE-SDKのパスを指定する必要があります。

オプションで指定するか、「c:\user\<user-name>\.noserc」に、下記のように記述して
noseテスト時のデフォルトオプションとして指定します。

--ｺｺｶﾗ--
[nosetests]
gae-lib-root=C:\Program Files\Google\google_appengine
--ｺｺﾏﾃﾞ--

○ mox(pythonモックライブラリ)を利用する場合
noseの実行オプションに

-s --nologcapture

ex. > nosetests -s --nologcapture -v

このオプションを指定しない場合、キャプチャログが出力されると
verifyの結果を破壊し、正しい結果が見れなくなります。
（正常動作の場合は問題ないので、そのままでもいいかもしんないけど）
