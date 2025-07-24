from collections import Counter

lst = ['피자','치킨','바나나','피자','햄버거','치킨','바나나','치킨','바나나','치킨','햄버거']
result = Counter(lst)
top_k, top_v = result.most_common(1)[0]

for k,v in result.items():
    print(f'- {k}:{v}표')

print(f'오늘의 점심메뉴는 {top_k}입니다. ({top_v}표) ')