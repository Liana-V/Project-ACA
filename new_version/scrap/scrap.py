import json
import sys
from urllib.parse import urlparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup, NavigableString

global dict_jobs
dict_jobs=[]


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
        counter = 0
        record = {}
        if s:
            company = s.find('h1', {'class': 'job_company_title'}).text.replace('\n', '').strip()
            img = s.find('img', {'class': 'radius_changes'}).get('src')
            job_info = s.find('div', {'id': 'job-post'})
            title = job_info.find('h2').text.replace('\n', '').strip()
            ref = job_info.findAll('p')
            deadline = ref[0].text.replace('\n', '').strip()
            category = ref[2].text.replace('\n', '').strip()
            job_type = ref[3].text.replace('\n', '').strip()
            job = s.find('div', {'class': 'job-list-content-desc hs_line_break'})
            a = job.find('h3', text='Job description:')
            k = a.next_siblings
            h = []
            arr = []
            m = 0
            for i in k:
                if isinstance(i, NavigableString):
                    continue
                if i.name == 'h3':
                    if h:
                        g = '\n'.join(h)
                        arr.append(g)
                    if not h or m == 2:
                        arr.append(i.text)
                    h = []
                    m += 1
                    continue

                u = i.text
                h.append(u)

            if len(arr) < 5:
                for i in range(5 - len(arr)):
                    arr.append('')

            job_desc = arr[0].replace('\n', '')
            job_resp = arr[1].replace('\n', '')
            req_qual = arr[2].replace('\n', '')
            req_cond_level = arr[3].replace('\n', '')
            salary = arr[4].replace('\n', '')
            try:
                add_info = job.find('div', {'class': 'additional-information information_application_block'}).find(
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

            id = [str(company).replace(" ", "").replace('\n', '').rstrip() + str(title).replace(" ", "").replace('\n',
                                                                                                                 '') + str(
                deadline).replace(" ", "").replace('\n', '')]
            id = hash(''.join(id).lower())
            id += sys.maxsize + 1
            record = {
                'id': id, 'company': company, 'img': img, 'title': title, 'deadline': deadline,
                'category': category, 'job_type': job_type, 'job_desc': job_desc,
                'job_resp': job_resp, 'req_qual': req_qual, 'req_cond_level': req_cond_level, 'salary': salary,
                'add_info': add_info
            }
        return record


    def __crawl(self, url: str) -> dict:
        soup = self.__open_url(url)
        counter = 0
        if soup:
            d = list()
            div_tag = soup.find("div", {"id": "search_list_block"})
            k = div_tag.find_all('a', href=True)
            print(url)
            for j in range(0, 29, 4):
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
        spider = Spider("https://staff.am/en/jobs?page=" + str(page) + "&per-page=50")
        spider.run()
    print(dict_jobs)
    with open('scrap/data.json', 'w') as fp:
        print(dict_jobs)
        json.dump(dict_jobs, fp, indent=4)
    fp.close()
    return 'a'


if __name__ == '__main__':
    job_scrap()
