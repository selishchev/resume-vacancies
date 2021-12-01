from parse_hh_data import download, parse

#vacancy = download.vacancy("47908212")

#resume = download.resume("c01195e3000073214c0039ed1f736563726574")
#res_resume = parse.resume(resume)
vac_ids = download.vacancy_ids(4, 9.312, 7, 50)
res_ids = download.resume_ids(4, 22, 1, 1)
checker = 1
checker1 = 1
checker2 = 1
for i in vac_ids:
    print(download.vacancy(i))
    checker1 += 1
    #checker += 1
    #if checker == 10:
    #    checker = 1
    #    break

for i in res_ids:
    print(parse.resume(download.resume(i)))
    checker2 += 1
    #checker += 1
    #if checker == 10:
    #    checker = 1
    #    break
print(checker1)
print(checker2)
print(res_ids, len(res_ids))
print(vac_ids, len(vac_ids))
print()
#print(res_resume)
#print(vacancy)