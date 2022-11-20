import requests,os

class yinyue(object):
    def __init__(self):
        self.song_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'   # 这是网易云音乐的播放音乐的外链地址,可以发现整个地址只是id不同,更改id即可获取不同的音乐
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}   # headers可以不用加,但加了总没错
        self.data = {'params': 'f/aZ47YnN/ARSX3MAN+RuDUjUpCKw/XhmYBfhAdUrnjZ5KkI2IXx3TfrBFLdGHqAxfVnif7xSysRF74vURIyzMSrroBf+4cPh9WMqQufLApOgH/5OLh/LZWgiZVeDMn8gQuBLu5szRXLrfNDXoPVlqeCC1hb4qrb5C30p5NLzbL3BSYzPIBd8urnSZMnTR3nnTrFZ7oxGfVzLPRF53QYjeitOlJJLlVTu8joB5hnU4lnQlGK2F2VU27YzrL51dy9yAEUjO5cjFY2Ocoa9vf6+A==',
                    'encSecKey': '1c0be5f6e973579de32be840d84c99bf021d63fa67db0e86f01bd589fe1e11d6ec9b66b9b4fc490711a8aad8160b36bbd39d7b52fff5bb4829270d9018c1ae24dc4258175a07fab990f7e1057ad5f1c4e601926628ad88117f455ff5371475a53df6f23c1a23b98ddd3cece5f1d14360d71c19f63d98fe8ffbae1f01cdd1c720'}
    def parse_url(self):
        response = requests.post('https://music.163.com/weapi/cloudsearch/get/web?csrf_token=', data=self.data, headers=self.headers).json()  # .json()是将请求得到的json数据转为python中的字典数据
        songs = response['result']['songs']   # 因为最外壳是一个字典形式，所以可以通过键取出所对应的值
        for song in songs:
            song_name = song['name']
            id = song['id']
            ar = song['ar']    # 发现歌手的名字在一个列表当中，所以也需求去遍历这个列表
            for song_actor in ar:
                actor = song_actor['name']
            # print(id,song_name,actor)
            self.save_songs(song_name,id,actor)    # 注意这个的缩进在for循环的内部，如果在外部就是将for循环遍历的最后一个结果传给save_songs方法,在类class里面叫方法,外面叫函数

    def save_songs(self,song_name,id,actor):
        filename = '音乐'     # 保存的路径
        if not os.path.exists(filename):    # 做个判断,是否存在此路径,若不存在则创建,注意这个创建的是文件夹，文件夹，文件夹，说三遍
            os.makedirs(filename)
        down_url = self.song_url.format(id)    # 拼接完整的下载地址url
        res = requests.get(down_url,headers = self.headers).content     # .content是将其转为二进制数据
        with open(filename+'/{} {}'.format(song_name,actor),'wb')as f:    # 以wb方式打开文件,b就是binary的缩写,代表二进制
            f.write(res)
            print('正在下载...{} {}'.format(song_name,actor))    # 让自己知道下载到哪里了

    def main(self):
        self.parse_url()

if __name__ == '__main__':
    spider = yinyue()
    spider.main()

