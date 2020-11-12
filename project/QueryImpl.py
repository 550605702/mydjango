from project import  StrParagaphQueyr,Storage

def queryText(text):
    proxy = "";
    # 查询分段
    data = StrParagaphQueyr.ParagaphQuery(text,proxy)
    # 保存到数据库
    Storage.storage(data)
    return data

