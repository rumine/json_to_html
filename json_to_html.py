# coding:utf-8
import json
from collections import OrderedDict
from jinja2 import Environment, FileSystemLoader,Template

#HTMLテンプレートファイルの読み込み
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tmpl = env.get_template('./templates/template.tmlp')

#JSON ファイルの読み込み
json_open = open('test.json', 'r')
#json_load = json.load(json_open)
#順番どおり読むにはOrderedDict が必要
json_load = json.load(open('test.json',encoding='utf-8'),object_pairs_hook=OrderedDict)
#print(json_load)
print (json.dumps(json_load,indent=2,ensure_ascii=False))

#HTML テンプレートに値をセットする
html = tmpl.render(json_to_html= json_load)

#HTML に書き込む(UTF-8にしないと文字化けする)
with open('json_to_html.html',mode='w',encoding='utf-8') as f:
    f.write(str(html))
    
print(html)