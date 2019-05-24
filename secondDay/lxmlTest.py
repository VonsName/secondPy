# __author:  Administrator
# __date:  2019/5/24/024


from lxml import etree

text = '''<div id="u" class=""><a class="toindex" href="/">百度首页</a><a id="imsg" href="http://www.baidu.com/#" onmousedown="return user_c({'fm':'set','tab':'imsg','login':'1'})">消息<span id="s_msg_count" class="s-msg-count">(1)</span></a><a href="javascript:;" name="tj_settingicon" class="pf">设置<i class="c-icon c-icon-triangle-down"></i></a><a href="http://i.baidu.com" id="user" class="username">爱你的小孩死了<i class="c-icon"></i></a></div>'''

# 修正HTML代码
html = etree.HTML(text)

print(etree.tostring(html).decode())

s = html.xpath("//a[@id='imsg']/@href")[0] if len(html.xpath("//a[@id='imsg']/@href")) > 0 else None
print(s)
