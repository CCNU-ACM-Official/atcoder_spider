from bs4 import BeautifulSoup, Tag
import requests
from src.AtSpider.structures import *

def parse_problem(url):

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    task_div = soup.find('div', id='task-statement')
    task = task_div.get_text(separator="\n", strip=True)
    task = list(task.split(sep="\n"))
    i = task.index('Sample Input 1')
    samples = " ".join(task[i:])
    statement = " ".join(task[task.index('Problem Statement') + 1:i])
    ret = problem()
    ret.statement = statement
    ret.samples = samples
    return ret


def parse_contest(id):
    ret = contest()
    url = f"https://atcoder.jp/contests/{id}/tasks"
    ret.id = id

    ret.contest_url = url
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    context = soup.find("tbody").find_all("tr")
    ret_addr = []
    ret_index = []
    ret_name = []

    for href in context:
        ret_addr.append("https://atcoder.jp" + href.a.get("href"))
        ret_index.append(href.a.get_text())
        ret_name.append(href.find_all("a")[1].get_text())

    
    
    ret.problems_addrs = ret_addr
    ret.index = ret_index
    ret.name = ret_name

    for i in ret_addr:
        ret.problems.append(parse_problem(i))

    return ret

