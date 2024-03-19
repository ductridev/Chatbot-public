import requests
import wolframalpha
import random
import urllib.parse
import os
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv('WOLFRALPHA_APP_ID')
client = wolframalpha.Client(APP_ID)

from googletrans import Translator
translator = Translator()

def removeBrackets(variable):
    return variable.split('(')[0]


def resolveListOrDict(variable):
    if isinstance(variable, list):
        return variable[0]['plaintext']
    else:
        return variable['plaintext']





def search_and_solve(input, is_general=True):
    input = translator.translate(input, dest='en')
    input = input.text
    input = urllib.parse.quote(input)
    #print(input)
    URL = 'http://api.wolframalpha.com/v1/result?i=%s&appid=%s' % (input, APP_ID)
    try:
        res = None
        print("Is generall: --->",is_general)
        if is_general == True:
            res = requests.get(URL)
            if res.status_code == 200:
                result = translator.translate(str(res.content, 'utf-8'), dest='vi').text
                result = result.replace('->', ' =')
                return {
                    "result": result
                }
        else:
            res = client.query(input)
            if res['@success'] == 'true':   
                try:
                    res = next(res.results)
                    if int(res['@numsubpods']) > 1:
                        res = [el['plaintext'] for el in res['subpod']]
                        res = ",".join(res)
                    else:
                        res = res['subpod']['plaintext']
                    return {
                        "result": translator.translate(str(res.content, 'utf-8'), dest='vi').text
                    }
                except:
                    res = res['pod'][1]
                    if int(res['@numsubpods']) > 1:
                        res = [el['plaintext'] for el in res['subpod']]
                        res = ",".join(res)
                    else:
                        res = res['subpod']['plaintext']
                    return {
                        "result": translator.translate(str(res.content, 'utf-8'), dest='vi').text
                    }
            elif res['didyoumeans']:
                # print(res['didyoumeans'])
                related_question = res['didyoumeans']
                if int(related_question['@count'])>1:
                    for related in related_question["didyoumean"]:
                        return search_and_solve(related["#text"], is_general=False)
                else:
                    return search_and_solve(related_question["didyoumean"]["#text"], is_general=False)

        return {"result": False}
    except:
        return {"result": False}
