import sys
import csv
from string import Template

#読み込みファイル
args = sys.argv

load = args[1] if (len(args) > 1 and args[1] !='') else 'temp.html'

#テンプレート用ファイル読み込み
t = open(load,'r',encoding='shift-jis')
html = t.read()
t.close();

#テンプレート作成
temp = Template(html)

#流し込み用CSV読み込み
f =open('data.csv','r')

#CSVから辞書に変換
reader = csv.DictReader(f)

#書き込み
newfile = open('marge_temp.txt','w');
for row in reader:
 output = temp.substitute(row)
 output = output + '\n'
 newfile.write(output)
f.close()
newfile.close()
