#! /usr/bin/python
#
#


##### 2021/12/10 #####
import os
credential_path = "[Google Cloud Platformで取得したJSONのファイル名を記載]"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
##### 2021/12/10 #####


from google.cloud import translate_v2 as translate

text="次は日本語を英語に翻訳します"
target="en"

translate_client = translate.Client()

result = translate_client.translate(text, target_language=target)

print("Text: {}".format(result["input"]))
print("Translation: {}".format(result["translatedText"]))
print("Detected source language: {}".format(result["detectedSourceLanguage"]))