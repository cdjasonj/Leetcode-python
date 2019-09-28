import re
# string0 = '刘德华的歌'
# string1 = '播放刘德华的歌'
# string2 = '来一首刘德华的歌'
# string3 = '请给我播放刘德华的歌'
# string4 = '能不能帮我播放刘德华的歌'
# string5 = '我想听刘德华的歌'
# string6 = '小布小布我想听刘德华的歌'
# string7 = '小欧小欧放一个刘德华的歌'


string0 = '来一个刘赟的沙漠骆驼'
string1 = '放一个刘赟的沙漠骆驼'
string2 = '我想听刘赟的沙漠骆驼'
string3 = '播放刘赟的沙漠骆驼'

strings = [string0,string1,string2,string3]
singer_rule = '(?:小布小布|小欧小欧)?(?:能不能|请)?(?:给我|帮我)?(?:播放|来一首|唱|唱一个|来一个|我想听|放一个|来一段)?(.*)的歌'
song_rule = '(?:小布小布|小欧小欧)?(?:能不能|请)?(?:给我|帮我)?(?:打开网易云音乐播放|打开酷狗音乐播放|打开QQ音乐播放|用网易云音乐播放|用酷狗音乐播放|用QQ音乐播放|播放歌曲|来一首|唱|唱一个|来一个|我想听|放一个|放一首|来一段)?(.*)'

for string in strings:
    print(re.findall(song_rule,string))