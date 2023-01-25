test_list = ["Gfg","is","Best"]

subs_dict = {
    "Gfg":[5,6,7],
    "is":[7,4,2]
}

k=2

res = [ele if ele not in subs_dict else subs_dict[ele][k] for ele in test_list]

print(res)