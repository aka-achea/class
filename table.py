from prettytable import PrettyTable

x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
x.align["City name"] = "l" # Left align city names
x.padding_width = 1 # One space between column edges and contents (default)
x.add_row(["Adelaide",1295, 1158259, 600.5])
x.add_row(["Brisbane",5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])
# print(x)

c = ['Date','Title','Tag','Author','Source','link','mail']
l = [('2018-12-07 11:39:48', '我是如何走进黑客世界的？', '计', 'FreeBuf', '微信公众号', 'https://mp.weixin.qq.com/s/vwF0QOkz4if47FZ9x0t3NA', 'CJYRB@hotmail.com'), ('2018-12-05 09:57:23', '去虾头、开虾背、撕虾壳，剥虾仁的流水线长这样', '食', '果壳', '微信公众号', 'https://mp.weixin.qq.com/s/A1YL4oVkdXvsdGAx0-2mIw', 'CJYRB@hotmail.com'), ('2018-12-11 11:40:07', '远离冻疮香肠手，涂凡士林真的有效吗？', '健', '果壳', '微信公众号', 'https://mp.weixin.qq.com/s/XRxp7vzj0X5_hPixDLXQgQ', 'CJYRB@hotmail.com')]
def list_table(c,l):
    lt = PrettyTable(c)
    lt.padding_width = 1
    for i in l:
        print(i)
        lt.add_row(i)

    print(lt)
         


if __name__ == "__main__":
    list_table(c,l)