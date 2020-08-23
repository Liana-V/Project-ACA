import json
import sys
from urllib.parse import urlparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup, NavigableString
from db.dbmgr import find
import hashlib


global dict_jobs,job_skills,h_count
dict_jobs=[]
job_skills = []
h_count=0
class Spider:
    def __init__(self, url: str):
        self.url = url
        self.base = '{u.scheme}://{u.netloc}'.format(u=urlparse(url))
        self.scanned = set()

    def run(self) -> dict:
        return self.__crawl(self.url)

    def __make_link(self, href: str) -> str:
        if not href or '#' in href or href.startswith('http'):
            return None

        return f'{self.base}{href}'

    def __open_url(self, url):
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urlopen(req) as response:
                soup = BeautifulSoup(response.read().decode(), 'html.parser')
                return soup
        except Exception:
            return None

    def __crawl_job(self, url: str) -> dict:
        s = self.__open_url(url)
        global h_count
        counter = 0
        record = {}
        if s:
            company = s.find('h1', {'class': 'job_company_title'}).text.replace('\n', ' ')
            img = s.find('img', {'class': 'radius_changes'}).get('src')
            job_info = s.find('div', {'id': 'job-post'})
            title = job_info.find('h2').text.replace('\n', ' ')
            ref = job_info.findAll('p')
            deadline = ref[0].text.replace('\n', ' ')
            category = ref[2].text.replace('\n', ' ')
            job_type = ref[3].text.replace('\n', ' ')

            job = s.find('div', {'class': 'job-list-content-desc hs_line_break'})
            a = job.find('h3', text='Job description:')
            k = a.next_siblings
            h = []
            arr = []
            m = 0
            for i in k:
                if isinstance(i, NavigableString):
                    continue
                if i.has_attr('class') and i['class'][0]=='hidden':
                    continue

                if i.name == 'h3':
                    if h:
                        g = '\n'.join(h)
                        arr.append(g)
                    if not h or m == 2:
                        arr.append(i.text)
                    h = []
                    m += 1
                    #print()
                    continue
                u = i.text
                h.append(u)

            if len(arr) < 5:
                for i in range(5 - len(arr)):
                    arr.append('')

            job_desc = arr[0]
            job_resp = arr[1]
            req_qual = arr[2]
            req_cond_level = arr[3]
            salary = arr[4]
            try:
                add_info = job.find('div', {'class': 'additional-information information_application_block'}).findAll(
                    'p').text
            except Exception:
                add_info = ''
            try:
                skill_tag = s.find('div', {'class': 'soft-skills-list clearfix'}).findAll('p')
            except Exception:
                skill_tag = []
            skills = []
            for i in skill_tag:
                skills.append(i.text.replace('\n', ''))
            id="{}{}{}".format(str(company).replace(" ", "").replace('\n', '').rstrip(), str(title).replace(" ", "").replace('\n',''),str(deadline).replace(" ", "").replace('\n', '') )
            id = hashlib.sha1(str.encode(id)).hexdigest()[:12]
            id=int(id, 16)

            for s in skills:
                s = find('id', 'SKILLS', str(s))
                if s:
                    job_skills.append({'id':h_count,'job_id': id, 'skill_id': s})
                    h_count+=1



            record = {
                'id': id, 'company': company, 'img': img, 'title': title, 'deadline': deadline,
                'category': category, 'job_type': job_type, 'job_desc': job_desc,
                'job_resp': job_resp, 'req_qual': req_qual, 'req_cond_level': req_cond_level, 'salary': salary,
                'add_info': add_info
            }
            for value in record:
                try:

                    spliter=record[value].split(':') # for Armenian language ՛։՛ is considered the end of a sentence
                    if len(spliter)==0 :
                        continue
                    if '\n' in spliter[1]:
                        record[value] = spliter[0]
                    else:
                        record[value]=spliter[1]
                except Exception as ex:
                    pass

        return record


    def __crawl(self, url: str) -> dict:
        soup = self.__open_url(url)
        counter = 0
        if soup:
            div_tag = soup.find("div", {"id": "search_list_block"})
            k = div_tag.find_all('a',{"class":"history_block_style history_block_padding"})
            if not k:
                pass
            for j in range(0, len(k)):
                if counter == 50:
                    break
                link = self.__make_link(k[j]['href'])
                if not link or link in self.scanned:
                    continue
                self.scanned.add(link)
                dict_jobs.append(self.__crawl_job(link))
                counter += 1
            return dict_jobs


def job_scrap():
    for page in range(1):
        spider = Spider("https://staff.am/en/jobs?page={}{}".format(str(page), "&per-page=50"))
        a=spider.run()
        if not a:
            break
    with open('scrap/data.json', 'w') as fp:
        json.dump(dict_jobs, fp, indent=4)
    fp.close()
    with open('scrap/job_skills.json', 'w') as fp2:
        json.dump(job_skills, fp2, indent=4)
    fp2.close()
    return 'a'


if __name__ == '__main__':
    job_scrap()
