import urllib.request
import urllib.parse
from json import loads
from easygui import msgbox, buttonbox, enterbox

def translator_MS(content='', fr='en', to='zh-CHS'):
    url = 'https://www.bing.com/ttranslate?&category=&IG=65263B70382D4368B5B768103385999C&IID=translator.5038.3'
    data = {}
    data['text'] = content
    data['from'] = fr
    data['to'] = to
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')
    result = loads(html)['translationResponse']
    msgbox(result, '翻译结果：')
    feeling = buttonbox('您对翻译结果是否满意？', choices=('满意[1]', '一般[2]', '不满意[3]'))
    if feeling == '满意[1]':
        msgbox('感谢您对小韩的支持^_^')
    elif feeling == '一般[2]':
        msgbox('感觉一般是几个意思？瞧谁不起吗？')
    else:
        msgbox('不满意那你去找微软呀，都是他翻译的！')
    # print('翻译结果：%s' % result)

def is_Chinese(content):
    for ch in content:
        if '\u4e00' <= ch <= '\u9fff':
            return True
        else:
            return False

def translate():
    content = enterbox('请输入需要翻译的内容：')
    # content = input('请输入需要翻译的内容：')
    if not is_Chinese(content):
        translator_MS(content)
    else:
        translator_MS(content, fr='zh-CHS', to='en')

if __name__ == '__main__':
    msgbox('欢迎使用小韩翻译', 'Welcom')
    msgbox('本软件支持中-英与英-中翻译，翻译结果由微软Bing翻译提供！\n（使用时请确保您的网络已连接）', '声明')
    # print('此翻译结果由微软Bing翻译提供！（请确保您的网络已连接）')
    # while True:
    translate()
        # print('\n')
