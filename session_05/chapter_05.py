# 开发人员：DYL
# 开发时间：2022/4/18 20:43

# 字典元素的遍历

scores = {'张三': 100, '李四': 98, '王五': 97}
for item in scores:
    print(item, scores[item], scores.get(item))
