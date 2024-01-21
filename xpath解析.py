'''
    xpath解析：最常用且便捷高效的一种解析方式
        xpath解析原理：
            1. 实例化一个etree的对象，并且需要将被解析的页面源码数据加载到该对象中
            2. 标签定位，通过调用etree对象中的xpath方法结合xpath表达式实现标签的定位和内容的捕获

        环境安装
            pip install lxml

        如何实现一个etree对象   from lxml import etree
            1. 将本地的html文档中的源码数据加载到etree对象中
                etree.parse(filePath)
            2. 可以将从互联网上获取的源码数据加载到该对象中
                etree.HTML('page_text)
            xpath('xpath表达式'):
                /: 表示从根节点开始定位，表示一个层级
                //: 表示多个层级，表示从任意位置开始定位
                属性定位：//div[@class='song'] tag[@attrName='attrValue']
                索引定位：//div[@class='song'/p[3]]         # 此处的[3]不是列表中的3（从0开始），而是表示一个偏移量，是从1开始的
                取文本：
                    /text():    获取标签的直系内容
                        tree.xpath('[@class="tang"]//li[5]/a/text()')
                    //text():   获取标签下所有的文本内容
                        tree.xpath('[@class="tang"]//text()')
                取属性：
                    /@attrName
                    (/img/@src) 

'''

from lxml import etree

if __name__ == '__main__':
    # 实例化一个etree对象，并且将解析的源码加载到该对象中
    tree = etree.parse('baidu.html')
    r = tree.xpath('/html/head/title')
