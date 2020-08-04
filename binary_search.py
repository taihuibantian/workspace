import sys
#二分探索法

#  arr   : 数値リスト
#   n    : 要素数
# left   : 左端要素のindex
# right  : 右端要素のindex
# center : 中央要素のindex
# target : 探索値

arr = [11,13,24,26,35,37,46,49,54,68]
print(arr)

target=input("探索値を入力する:")
target=int(target)

n = len(arr)
left = 0
right = n -1

while left <= right:
    center = (left + right) // 2 #要素の真ん中をチェック
    if arr[center] == target:
        print(f"探索値:{target}は0から数えて{center}番目にあります")
        sys.exit()
    elif arr[center] < target:
        left = center + 1
    else:
        right = center - 1
print(f'探索値:{target}は見つかりませんでした')