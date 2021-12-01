from parse_hh_data import download, parse
import json
import codecs
# ['dace3ab7000898addd0039ed1f444632306f6f', '60cd40d90000eeb5a80039ed1f33516865516e', 'c7eed9b700057089b80039ed1f526c424c544c', '1a57178f00008632b10039ed1f736563726574', '3af80f900002b9435b0039ed1f6d6f444b4669', 'da8687250007d8568d0039ed1f724845364243', '6cf95be500028324560039ed1f785765336174', '5143ae960003b48d740039ed1f59526e6d4539', '7d34298700079316860039ed1f494832717866', '22d42f3a000014d5be0039ed1f736563726574', '55a832690005261f740039ed1f4c7a49786d79', '3d2188140008fdf8a40039ed1f6472316a764b', 'f409059a000792cc7e0039ed1f677152667976', '9ee92cea0001f678a50039ed1f4c4479313133', 'b476123f00059486fc0039ed1f6b46704f5638', 'cb86147700035896000039ed1f4f5748464347', '84ce8e3a0007f5affd0039ed1f4c5146587959', 'e3734ef800061550760039ed1f45674946454e'] 18
vacancy = download.vacancy("49084668")

resume = download.resume("dace3ab7000898addd0039ed1f444632306f6f")
res_resume = parse.resume(resume)
print(vacancy)
for i in vacancy.values():
    print(i)

res_profarea_lst = []
specs_ids_lst = []
for i in res_resume.values():
    if type(i) == list:
        for k in i:
            if type(k) == dict:
                if k.get('profarea_name') != None:
                    print(k.get('profarea_name'))
                    res_profarea_lst.append(k.get('profarea_name'))

with codecs.open("specializations.json", "r", "utf_8_sig") as f:
    text = f.read()
specs_json = json.loads(text)
for i in res_profarea_lst:
    for j in specs_json:
        if j.get('name') == i:
            specs_ids_lst.append(int(j.get('id')))
        for k in j.get('specializations'):
            if k.get('name').lower() == i.lower():
                specs_ids_lst.append(float(k.get('id')))
print(specs_ids_lst)

for i in specs_ids_lst:
    vacancies_ids = download.vacancy_ids(4, i, 7, 50)
    for j in vacancies_ids:
        print(download.vacancy(j))


