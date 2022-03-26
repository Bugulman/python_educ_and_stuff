import pprint

# def lcs(x, y):
#     str_match={}
#     for first in x:
#         str_match[first] =0
#         for second in y:
#             if first==second:
#                 str_match[first]+=1
#             else:
#                 continue
#     print(str_match)
#     a=[x if y>0 else '' for x, y in str_match.items()]
#     return print(''.join(a))

def lcs(x, y):
    str_match=[[0 for x in range(0,len(y))]]
    result = []
    for first in x:
        row = []
        for second in y:
            if first==second:
                row.append(1)
            else:
                row.append(0)
        str_match.append(row)
    # str_match.append([0 for x in range(0,len(y))])
    for row in range(0,len(str_match)):
        if row==0:
            continue
        else:
            prev_row = str_match[row-1]
            current_row = str_match[row]
            r = [current_row[x]+prev_row[x-1] if x>0 and current_row[x]>0 else current_row[x] for x in range(0, len(current_row))]
            str_match[row]=r
    pprint.pprint(str_match)
    for row in range(len(str_match)-1, 0,-1):
        for coll in range(len(str_match[row])-1, -1, -1):
            # print(str_match[row], row, coll, str_match[row][coll])
            if str_match[row][coll]>1:
                while str_match[row][coll]>0:

                result.append(y[coll])
    print(result)
 

lcs("anothertest", "notatest")
# lcs( "defabc" , "abc" )
# lcs("132535365", "123456789")
