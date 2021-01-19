import random
import string


class Code:
    def gen_code(self):
        seeds = string.digits
        random_str = random.choices(seeds, k=4)
        code="".join(random_str)
        return code


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


class Checkcode:
    def __init__(self, **kwargs):
        self._width = kwargs['width']
        self._height = kwargs['height']
        self.codelist = None

    @staticmethod
    def codegnertor(x=1):  # 默认为0-9 a-z
        source = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G' \
                                                                                                  'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        if x:
            t = random.sample(source, 4)
        else:
            t = random.sample(source[:9], 4)
        t = "".join(t)
        return t

    def picgenertor(self):
        image = Image.new('RGB', (self._width, self._height), (255, 255, 255))
        font = ImageFont.truetype('./static/font/fonts/Arial.ttf', 18)
        draw = ImageDraw.Draw(image)
        def rndColor():
            return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

        def rndColor2():
            return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

        for x in range(self._width):
            for y in range(self._height):
                draw.point((x, y), fill=rndColor())
        for t in range(4):
            draw.text((self._width / 4 * t + self._width / 12, 10), self.codelist[t], font=font, fill=rndColor2())
        begin = (0, random.randint(0, self._height))
        end = (self._width, random.randint(0, self._height))
        draw.line([begin, end], fill=(0, 0, 0), width=3)
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        # image = image.transform((self._width + 30, self._height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0),Image.BILINEAR)  # 创建扭曲
        return image

    def __getitem__(self, key):
        if (key == 'picture'):
            self.codelist = self.codegnertor()
            return self.picgenertor()
        elif (key == "size"):
            return self._width, self._height
        elif (key == 'checkcode'):
            return self.codelist
        else:
            raise Exception('the key %s is valiad!' % key)

    def __str__(self):
        return 'code genertor'

# x = Checkcode(width=100, height=60)  # width,height为验证码图片
# # s = Checkcode.codegnertor()  # 随机生成验证码 x--->1 0-9 A--Z   x--->0 0-9
#
# pic = x['picture']  # image对象
# print(x._checkcode)
# pic.save('./1.png')  # 储存图片
