# twitchTransFreeNext CustomBuild
[日本語解説](#日本語)

This software is for Windows7 or later Only<br />
Original ttfn(twitchtransFN) is here https://github.com/sayonari/twitchTransFreeNext

# Download
[latest Release](https://github.com/crest-streamer/twitchTransFreeNext/releases/latest)<br />
To run on Windows 7 or later<br />
twitchTransFN_windows.zip<br />
To run on MacOS Intel Chip<br />
twitchTransFN_macos.tar.gz<br />
To run on Linux<br />
twitchTransFN_linux.tar.gz<br />
<br /><br />
To run on any OS with Python<br />
twitchTransFreeNext_python.zip

# memo
## support language (google translator)
https://cloud.google.com/translate/docs/languages

# secret functions
## choose trans destination language (for one text)
At the time of translation, you can select the target language like `en:` at the beginning of the sentence.  
Example) ru: Hello -> привет там

NOTE: When rewriting config.txt, please delete the `#` mark at the beginning of each setting value!

# Required Files
<li>Executable Binaly</li>
<pre>twitchTransFN.exe
config.py</pre>
<li>Execute with Python(Developer's operating environment is Python 3.9.13)</li>
<pre>twitchTransFN.py
config.py
requirements.txt</pre>
please Edit config.py with notepad or any TextEditer.
if completed edit then Overwrite.

<hr>
# Customize point
  <li>Remove TTS related</li>
  <li>Can Edit Ready Message(original message is "has landed!" but this ver deleted)</li>
  if you want no message send then blank of Start_Message 
  <li>Enabled color selection</li>
  if you want your setting color then blank of Trans_TextColor
  <li>Don't translate emotes-only chats</li>
  <li>Add setting to convert specific words to specified words</li>
  <li>Add setting W-only comments are not translated</li>
  <li>Add "!des" command. this is Chat about the last update description</li>
  <hr>

# How to Execute with Python
1.Install Python3.x(Developer's operating environment is Python 3.9.13)<br>
2.run command with Command Pronpt/Terminal # pip(or pip3 or pip3.x) install -r requirements.txt<br />
3.run command with Command Pronpt/Terminal # python(or python3 or python3.x) twitchTransFN.py<br />
4.If it translates after a test chat, it is a success. enjoy!<br />
5.Ctrl+C is Terminate<br />
  <hr>
  
# 日本語

# twitchTransFreeNext CustomBuild
本ソフトウェアはWindows7以降専用です。それ以前のOSやMac/Linuxに関してはpythonで実行してください。<br />
オリジナルの翻訳ちゃんFreeNextは https://github.com/sayonari/twitchTransFreeNext です。(大感謝！)

# ダウンロード
[最新版](https://github.com/crest-streamer/twitchTransFreeNext/releases/latest)<br />
Windows7以降の方は下記を<br />
twitchTransFN_windows.zip<br />
MacOS(Intelチップ)の方は下記を<br />
twitchTransFN_macos.tar.gz<br />
Linuxの方は下記を<br />
twitchTransFN_linux.tar.gz<br />
<br /><br />
OS問わずPythonで実行する方は「twitchTransFreeNext_python.zip」を<br />
ダウンロードして下さい。

# memo
## グーグル翻訳で対応している言語一覧
https://cloud.google.com/translate/docs/languages

# 必要なファイル
<li>実行ファイル</li>
<pre>twitchTransFN.exe
config.py</pre>
<li>Pythonで動かす用ファイル</li>
<pre>twitchTransFN.py
config.py
requirements.txt</pre>
config.pyをメモ帳等で開き、編集して保存してください。<br />

# 変更点
  <li>読み上げ機能関連を全削除
  <li>準備完了時の「has landed!」チャットを削除。代わりに自分の入れたいメッセージを入力可能。<br />
    もし何もチャットしたくない場合は「Start_Message」の項目を「''」に設定してください。
  <li>色選択を自分で設定出来るように変更<br />
    翻訳用アカウントで「/color #FF0000」等で色を指定し、それを維持したい時は<br />
    「Trans_TextColor」の項目を「''」に設定してください。<br />
    色の名前を入力した場合はオリジナルと同様に色変更を行います。
  <li>スタンプのみのチャットは翻訳しない</li>
  <li>特定の単語を指定した単語に変換する設定の追加</li>
  <li>wのみのコメントを翻訳しない設定の追加</li>
  <li>!desコマンドの追加(最新のverup情報をコメントします)</li>
<hr>
    
# Pythonでの実行方法
1.Python3.xをインストールします。(開発者の動作環境は3.9.13です)<br />
2.「pip(or pip3 or pip3.x) install -r requirements.txt」をコマンドプロンプト/ターミナル/端末で実行します。<br />
3.「python(or python3 or python3.x) twitchTransFN.py」をコマンドプロンプト/ターミナル/端末で実行します。<br />
4.テストチャットをして翻訳されれば成功です。<br />
5.コマンドプロンプト/ターミナル/端末で「Ctrl+C」キーを同時押しすると終了します。<br />
    
## command: (version)
`!ver`: print the software version.

`!des`: Chat about the last update description.

# Thanks
Thanks to Pioneers!
The developer of ...
- Google
- googletrans by ssut
    - https://github.com/ssut/py-googletrans
- TwitchIO
    - https://github.com/TwitchIO/TwitchIO

# Developer Info.

| Title | Automatic Translator for Twitch Chat (Next Generation) |
|--|--|
| Developer | husband_sayonari_omega |
| github | https://github.com/sayonari/twitchTransFreeNext |
| Webpage | http://www.sayonari.com/trans_asr/ |
| mail | sayonari@gmail.com |
| Twitter | [sayonari](https://twitter.com/sayonari) |

# Special Thanks
[sayonari(西村良太)大先生](https://github.com/sayonari/twitchTransFreeNext) <br />
[yuniruyuni大先生](https://github.com/yuniruyuni)
