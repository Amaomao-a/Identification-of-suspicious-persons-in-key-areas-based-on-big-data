import random
import time
from faker import Faker
import pandas as pd


class user:
    firstName = ""  # 用户名
    lastName = ""
    sex = ""        # 性别
    phone = ""      # 用户手机号码
    originLoc = ""  # 用户号码归属地
    callLog = []    # 用户通信行为

    def __init__(self):
        self.basisProducer()
        self.phoneProducer()

    def basisProducer(self):
        # 百家姓中比较大众化的单姓与复姓
        firstNameList = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                        "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" \
                        "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"

        firstNameList2 = "万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空亓官司寇仉督子颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁段干百里东郭南门呼延羊舌微生梁丘左丘东门西门南宫南宫"

        # 男女名字
        girlNameList = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'

        boyNameList = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘 '

        nameList = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝'

        # 随机生成一个姓
        if random.choice(range(100)) > 10:  # 10%的几率获得复姓
            self.firstName = firstNameList[random.choice(range(len(firstNameList)))]
        else:
            i = random.choice(range(len(firstNameList2)))
            self.firstName = firstNameList2[i:i + 2]

        # 性别
        sex = random.choice(range(2))
        if sex > 0:
            self.sex = "女"
        else:
            self.sex = "男"

        # 名字
        name1 = ""
        name2 = ""
        if sex > 0:
            name1 = girlNameList[random.choice(range(len(girlNameList)))]
        else:
            name1 = boyNameList[random.choice(range(len(boyNameList)))]
        if random.choice(range(2)) > 0:
            name2 = nameList[random.choice(range(len(nameList)))]
        self.lastName = name1 + name2

    def phoneProducer(self):
        phoneStart = ["13", "15", "17", "18"]  # 常见的号码前缀

        self.phone = phoneStart[random.randint(0, 3)]
        # 生成一个九位的随机数
        for i in range(1, 10):
            self.phone += str(random.randint(0, 9))

        # 生成一个随机的号码归属地
        provinceList = ["河北省", "山西省", "辽宁省", "吉林省", "黑龙江省", "江苏省", "浙江省", "安徽省", "福建省", "江西省", "山东省",
                        "河南省", "湖北省", "湖南省", "广东省", "海南省", "四川省", "贵州省", "云南省", "陕西省", "甘肃省", "青海省", "台湾省",
                        "北京市", "天津市", "上海市", "重庆市",
                        "内蒙古自治区", "广西壮族自治区", "宁夏回族自治区", "新疆维吾尔自治区", "西藏自治区",
                        "香港特别行政区", "澳门特别行政区"]
        # 区域内的人员大多还是本地人员，不能完全随机化（7:3）
        if random.randint(0, 10) < 7:
            self.originLoc = "北京市"
        else:
            self.originLoc = provinceList[random.randint(0, 33)]


class callLogProducer:
    userList = []
    callLog = []
    startDate = time.mktime((2021, 1, 1, 0, 0, 0, 0, 0, 0))
    endDate = time.mktime((2022, 1, 1, 0, 0, 0, 0, 0, 0))

    def getUsersList(self):
        for i in range(1, 500):
            userTemp = user()
            self.userList.append(userTemp)

    def getCallDate(self, startDate, endDate):
        t = random.randint(startDate, endDate)  # 在时间范围内随机取样
        dateTup = time.localtime(t)  # 将时间戳生成元组
        date = time.strftime("%Y-%m-%d", dateTup)  # 将时间戳元组转化成格式化字符串
        return date

    def getCallLog(self):
        # 获取建立通话的日期
        callDate = self.getCallDate(self.startDate, self.endDate)

        # 获取主叫和被叫
        user1 = self.userList[random.randint(0, len(self.userList) - 1)]
        while True:
            user2 = self.userList[random.randint(0, len(self.userList) - 1)]
            if user1 != user2:
                break

        # 通话持续时间
        m, s = divmod(random.randint(0, 30 * 60), 60)
        h, m = divmod(m, 60)
        duration = "%02d:%02d:%02d" % (h, m, s)

        # 通话内容：随机生成一段文字
        size = random.randint(0, 50)
        text = Faker("zh_CN").paragraph(nb_sentences=size, variable_nb_sentences=True)

        log = [user1.phone, user2.phone, callDate, duration, text]
        self.callLog.append(log)

    def producer(self):
        self.getUsersList()  # 获取通话人群
        size = random.randint(10000, 50000)  # 通话总量
        for i in range(size):
            self.getCallLog()


aux = callLogProducer()
aux.producer()

sectionNames = ['主叫', '被叫', '日期', '通话时间', '通话内容']
result = pd.DataFrame(columns=sectionNames, data=aux.callLog)
result.to_csv('2021-01-01--2022-01-01用户通话记录.csv')

# print(aux.callLog)
# print(user1.firstName + user1.lastName + "\t" + user1.sex + "\t" + user1.phone + "\t" + user1.originLoc)


