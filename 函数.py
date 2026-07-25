#计算三角形的面积
def triangle_aera(l,b):
    """
    :triangle_aera:三角面积
    :param l: 高
    :param b: 底
    :return: 面积
    """
    aera = l * b / 2
    return aera
print(triangle_aera(3,4))






#是否存在元音字母
def hhh(s):
    j = 0
    for h in s:
        if h in 'aeiouAOEIU':
            j += 1
    return j
print(hhh("askldjalskdjalououiouiouiouiouioskdjals"))


#关于列表最值计算
def score(score_list):
    max_score = max(score_list)
    min_score = min(score_list)
    Average_score = round(sum(score_list) / len(score_list),1)
    return max_score, min_score, Average_score
print(score([3,4,5,9191991919191991]))

