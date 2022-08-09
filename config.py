######################################################
# PLEASE CHANGE FOLLOWING CONFIGS ####################
# 翻訳を利用する配信チャンネルのIDを入力してください。
Twitch_Channel          = 'Your Stream Channel ID'

# If you have set a DisplayName, you must still enter your user name
# 表示名を設定していても、ユーザーIDを入力してください。
Trans_Username          = 'Your Translate User ID'
# Visit to https://twitchapps.com/tmi/ and Complete Connect with Your Trans_Username Account
# https://twitchapps.com/tmi/ を開いて、Connectを押し、必要に応じて許可を押してoauthパスワードを入手してください。
Trans_OAUTH             = 'oauth:'

#######################################################
# OPTIONAL CONFIGS ####################################
# Please select a display color for the name of your translation account from the list below and enter it.
# If you do not enter a color, the color you set yourself will be applied.
# 翻訳アカウントの名前の表示色を下記リストから選択して入力ください。
# 入力されていない場合はご自身で設定した色が適用されます。
Trans_TextColor         = ''
# Blue, Coral, DodgerBlue, SpringGreen, YellowGreen, Green, OrangeRed, Red, GoldenRod, HotPink, CadetBlue, SeaGreen, Chocolate, BlueViolet, and Firebrick

# Please Enter Your Native Language. if When Other Language in Chat be able to Translation to Your Native Language
# 設定した言語をベース言語とし、他言語からはデフォルトでベース言語に翻訳します。

# Language List is Get From https://cloud.google.com/translate/docs/languages and Please Set ISO-639-1 Code
# 言語リストは https://cloud.google.com/translate/docs/languages ここで確認してください。
# ISO-639-1 コード欄の文字を入力する必要があります。
lang_TransToHome        = 'ja'

# Please enter your preferred language of translation.
# If there is a chat in your native language, the software will translate it into your preferred language.
# 設定した言語を翻訳ベース言語とし、ベース言語からはデフォルトで翻訳ベース言語に翻訳します。
lang_HomeToOther        = 'en'

# If you hope Show Chatter's Name in TranslationChat be able to True. If not hope then Set False
# 翻訳後チャットに、翻訳元チャットの発言者IDを表示したい場合はTrueを、しない場合はFalseを入力してください。
Show_ByName             = True

# if you want the language of the source and the translated language to be displayed in the post-translation chat
# then True if you do, or False if you don't
# 翻訳後チャットに、翻訳元チャットの言語と翻訳先の言語を表示したい場合はTrueを、しない場合はFalseを入力してください。
Show_ByLang             = True

# If you have a language you don't want translated, enter the ISO-639-1 code in the format ['code','code2']
# 翻訳されたくない言語があれば、['code','code2']という形式でISO-639-1 コードを入力してください。
Ignore_Lang             = []
# If you have users you do not want translated, enter their UserName (not DisplayName) in the format ['user','user2']
# 翻訳されたくないユーザがいる場合は、['user','user2']という形式でユーザーID(表示名ではない)を入力てください。
Ignore_Users            = ['Nightbot', 'BikuBikuTest']
# If you have a Keyword you don't want translated, enter their Keywords in the format ['Keyword','Keyword2']
# If the keyword exists in the source chat, no translation will be done
# 翻訳されたくない単語がある場合は、['単語','単語2']という形式でその単語を入力してください。該当する単語があれば、翻訳を実施しません。
Ignore_Line             = ['http', 'BikuBikuTest', '888', '８８８']
# If you have a Keyword you don't want translated, enter their Keywords in the format ['Keyword','Keyword2']
# If the keywords are present in the source chat, they will be removed and translated
# 翻訳されたくない単語がある場合は、['単語','単語2']という形式でその単語を入力してください。
# 該当する単語があれば、その単語を削除してから翻訳します。
Delete_Words            = ['saatanNooBow', 'BikuBikuTest']

# Once the software is ready, type your message if you wish to send a message in the channel chat. If blank, nothing is sent.
# 翻訳の準備が完了したときに、自分のチャンネルに送信するチャットメッセージを入力してください。空欄の場合は何も送信されません。
Start_Message           = ''

# if you want replace word then setting this. example:{'befour':'after','befour2':'after2'}
# 置換したい単語の組み合わせを{'置換前':'置換後','置換前2':'置換後2'}の形式で入力してください。
Replace_Words           = {'':''}

# Select the translate engine ('deepl' or 'google')
Translator              = 'deepl'

# if comment is w only then not translate=True, go translate=False
# wのみ(w以降wが続くだけ)のコメントは翻訳しない=True、翻訳する=False
Ignore_Only_ww          = True

# This Setting's Only Translate DeepL
# ここで設定した言語はDeepLで翻訳し、設定されていない言語はGoogle(もしくはGAS)で翻訳します。
# Default DeeplTrans    = {'de':'DE', 'en':'EN', 'fr':'FR', 'es':'ES', 'pt':'PT', 'it':'IT', 'nl':'NL', 'pl':'PL', 'ru':'RU', 'ja':'JA', 'zh-CN':'ZH'}
# Example Chinese not Deepl {'de':'DE', 'en':'EN', 'fr':'FR', 'es':'ES', 'pt':'PT', 'it':'IT', 'nl':'NL', 'pl':'PL', 'ru':'RU', 'ja':'JA'}
DeeplTrans              = {'de':'DE', 'en':'EN', 'fr':'FR', 'es':'ES', 'pt':'PT', 'it':'IT', 'nl':'NL', 'pl':'PL', 'ru':'RU', 'ja':'JA', 'zh-CN':'ZH'}

# Use Google Apps Script for tlanslating
# e.g.) GAS_URL         = 'https://script.google.com/macros/s/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/exec'
GAS_URL                 = ''

# If you meet any bugs, You can check some error message using Debug mode (Debug = True)
Debug                   = False
