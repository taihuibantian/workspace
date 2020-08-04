import sys
#線形探索法

# arr  :数値リスト
# n    :要素数
#  i    :探索する要素の位置
# target:探索値

arr = [30, 40, 20, 50, 90]
n = len(arr)

print(arr)

#探索する値の入力
target = input('探索値を入力する。:')
target = int(target) #str → int

#探索する
i = 0

while i < n:
    if arr[i] == target:
        print(f'探索値:{target}は0から数えて{i}番目にある。')
        sys.exit()
    i += 1

print(f'探索値:{target}はみつからんかった。')