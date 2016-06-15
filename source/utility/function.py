# -*- coding:utf-8 -*-  
import re
import os.path
import logging
from thirdpart.chinese.langconv import Converter
import thirdpart.jieba as jieba

def startlog(_format='%(asctime)s: %(levelname)s: %(message)s',_level=logging.INFO):
    '''@return a format logger
    '''
    import logging
    program = os.path.basename(__name__)
    logger = logging.getLogger(program)
    logging.basicConfig(format = _format)
    logging.root.setLevel(level=_level)
    return logger


def tran2simple(line):
    if isinstance(line,list):
        ret = []
        for i in line:
            word = Converter('zh-hans').convert(i.decode('utf-8'))
            word = word.encode('utf-8')
            ret.append(word)
        return ret
    else:
        line = Converter('zh-hans').convert(line.decode('utf-8'))
        return line.encode('utf-8')

def simple2tran(line):
    if isinstance(line,list):
        ret = []
        for i in line:
            word = Converter('zh-hant').convert(i.decode('utf-8'))
            word = word.encode('utf-8')
            ret.append(word)
        return ret
    else:
        line = Converter('zh-hant').convert(line.decode('utf-8'))
        return line.encode('utf-8')

def remove_word(line, encoding = 'utf8'):
    '''
    @param: line should be decode with encoding
    @param: encoding the line's coding mehtod such as utf8 or gbk
    @return: remove no chinese charaters
    '''
    regx = re.compile(u"[\n\s*\r\u4e00-\u9fa5]")
    return "".join(map(lambda x:x.encode(encoding), regx.findall(line)))
    

def seperate_word(line, space=' '):
    '''
    Chinese seperate operation using 3rdpart lib jieba
    more: http://www.oschina.net/p/jieba
    '''
    seg_list = jieba.cut(line)
    return space.join(seg_list)

