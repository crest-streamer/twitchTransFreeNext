######################################################
# PLEASE CHANGE FOLLOWING CONFIGS ####################
Twitch_Channel          = 'cool_me_315'

Trans_Username          = 'cool_me_trans'
Trans_OAUTH             = 'oauth:mfvb70c5ygwnmymwpv1zijm07j44u2'

#######################################################
# OPTIONAL CONFIGS ####################################
Trans_TextColor         = ''
# Blue, Coral, DodgerBlue, SpringGreen, YellowGreen, Green, OrangeRed, Red, GoldenRod, HotPink, CadetBlue, SeaGreen, Chocolate, BlueViolet, and Firebrick

lang_TransToHome        = 'ja'
lang_HomeToOther        = 'en'

Show_ByName             = False
Show_ByLang             = False

Ignore_Lang             = ['ja']
Ignore_Users            = ['Nightbot', 'BikuBikuTest']
Ignore_Line             = ['http', 'BikuBikuTest', '888', '８８８']
Delete_Words            = ['saatanNooBow', 'BikuBikuTest']

Start_Message           = ''

Replace_Words           = {'ww':'lol'}
Ignore_Only_ww          = True
# if you make TTS for only few lang, please add langID in the list
# for example, ['ja'] means Japanese only, ['ko','en'] means Korean and English are TTS!
ReadOnlyTheseLang       = []

# Select the translate engine ('deepl' or 'google')
Translator              = 'deepl'

# This Setting's Only Translate DeepL
# ここで設定した言語はDeepLで翻訳し、設定されていない言語はGoogle(もしくはGAS)で翻訳します。
# Default DeeplTrans    = {'de':'DE', 'en':'EN', 'fr':'FR', 'es':'ES', 'pt':'PT', 'it':'IT', 'nl':'NL', 'pl':'PL', 'ru':'RU', 'ja':'JA', 'zh-CN':'ZH'}
DeeplTrans              = {'de':'DE', 'en':'EN', 'fr':'FR', 'es':'ES', 'pt':'PT', 'it':'IT', 'nl':'NL', 'pl':'PL', 'ru':'RU', 'ja':'JA'}

# Use Google Apps Script for tlanslating
# e.g.) GAS_URL         = 'https://script.google.com/macros/s/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/exec'
GAS_URL                 = 'https://script.google.com/macros/s/AKfycbzzhWlbMyaMHwgqZVzb3r9Pp7ArhcHZIPkH4qtDZORXNZYejGWXDlWa2lyXChKG4vNN/exec'

# If you meet any bugs, You can check some error message using Debug mode (Debug = True)
Debug                   = True