'''
何荣华最牛逼
'''
__all__ = ['str']
def str():
    s = {"S.isdigit()":"判断字符串中的字符是否全为数字","S.isalpha()":"判断字符串是否全为英文字母",
        "S.islower()":"判断字符串所有字符是否全为小写英文字母","S.isupper()":"判断字符串所有字符是否全为大写英文字母",
        "S.isspace()":'判断字符串是否全为空白字符',
'S.center(width[,fill])':"将原字符串居中，左右默认填充空格",
'S.count(sub[, start[,end]])':'获取一个字符串中子串的个数',
"S.find(sub[, start[,end]])":"获取字符串中子串sub的索引,失败返回-1",
"S.strip()":"返回去掉左右空白字符的字符串",
"S.lstrip()":"返回去掉左侧空白字符的字符串",
"S.rstrip()":"返回去掉右侧空白字符的字符串",
'S.upper()':"生成将英文转换为大写的字符串",
"S.lower()":"生成将英文转换为小写的字符串",
"S.replace(old, new[, count])":"将原字符串的old用new代替，生成一个新的字符串",
"S.startswith(prefix[, start[, end]])":"返回S是否是以prefix开头，如果以prefix开头返回True,否则返回False",
'S.endswith(suffix[, start[, end]])':'返回S是否是以suffix结尾，如果以suffix结尾返回True,否则返回False',
'S.title()':'生成每个英文单词的首字母大写字符串',
'S.isnumeric()':'判断字符串是否全为数字字符'}
    for k,v in s.items():
        print(k,v,sep=":")
def list():
    l = {'L.index(v [, begin[, end]])':'返回对应元素的索引下标, begin为开始索引，end为结束索引,当 value 不存在时触发ValueError错误',
'L.insert(index, obj)':'将某个元素插放到列表中指定的位置',
'L.count(x)':'返回列表中元素的个数',
'L.remove(x)':'从列表中删除第一次出现在列表中的值',
'L.copy()':'复制此列表（只复制一层，不会复制深层对象)',
'L.append(x)':'向列表中追加单个元素',
'L.extend(lst)':'向列表追加另一个列表',
'L.clear()':'清空列表,等同于 L[:] = []',
'L.sort(reverse=False)':'将列表中的元素进行排序，默认顺序按值的小到大的顺序排列',
'L.reverse()':'列表的反转，用来改变原列表的先后顺序',
'L.pop([index])':'删除索引对应的元素，如果不加索引，默认删除最后元素，同时返回删除元素的引用关系',
'S.split(sep=None)':'将字符串使用sep作为分隔符分割S字符串，返回分割后的字符串列表，当不给定参数时默认用空白字符作为分隔符分割',
'S.join(iterable)':'用可迭代对象中提供的字符串,返回一个中间用S进行分隔的字符串'}
    for k,v in l.items():
        print(k,v,sep=":")
def dict():
    d = {'D.clear()':'清空字典',
'D.pop(key)':'移除键，同时返回此键所对应的值',
'D.copy()':'返回字典D的副本,只复制一层(浅拷贝)',
'D.update(D2)':'将字典 D2 合并到D中，如果键相同，则此键的值取D2的值作为新值',
'D.get(key, default)':'返回键key所对应的值,如果没有此键，则返回default',
'D.keys()':'返回可迭代的 dict_keys 集合对象',
'D.values()':'返回可迭代的 dict_values 值对象',
'D.items()':'返回可迭代的 dict_items 对象'}
    for k,v in d.items():
        print(k,v,sep=":")
def set():
    e = {'S.add(e)':'在集合中添加一个新的元素e；如果元素已经存在，则不添加',
'S.remove(e)':'从集合中删除一个元素，如果元素不存在于集合中，则会产生一个KeyError错误',
'S.discard(e)':"从集合S中移除一个元素e,在元素e不存在时什么都不做;",
'S.clear()':'清空集合内的所有元素',
"S.copy()":"将集合进行一次浅拷贝",
"S.pop()":"从集合S中删除一个随机元素;如果此集合为空，则引发KeyError异常",
"S.update(s2)":"用 S与s2得到的全集更新变量S",
"S.difference(s2)":"用S - s2 运算，返回存在于在S中，但不在s2中的所有元素的集合",
"S.difference_update(s2)":"等同于 S = S - s2",
"S.intersection(s2)":"等同于 S & s2",
"S.intersection_update(s2)":"等同于S = S & s2",
"S.isdisjoint(s2)":"如果S与s2交集为空返回True,非空则返回False",
"S.issubset(s2)":"如果S与s2交集为非空返回True,空则返回False",
"S.issuperset(...)":"如果S为s2的子集返回True,否则返回False",
"S.symmetric_difference(s2)":"返回对称补集,等同于 S ^ s2",
"S.symmetric_difference_update(s2)":"用 S 与 s2 的对称补集更新 S",
"S.union(s2)":"生成 S 与 s2的全集"}
    for k,v in e.items():
        print(k,v,sep=":")


    