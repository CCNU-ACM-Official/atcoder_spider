from bs4 import BeautifulSoup, Tag
import requests


class problem:
    index = ""
    id = ""
    url = ""
    text = ""


class contest:
    id = ""
    addr = []
    index = []
    name = []
    problems = []


def parse_problem(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    task_div = soup.find('div', id='task-statement')
    task = task_div.get_text(separator="\n")
    # TODO
    return task


def parse_contest(id):

    url = f"https://atcoder.jp/contests/{id}/tasks"
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

    ret = contest()
    ret.id = id
    ret.addr = ret_addr
    ret.index = ret_index
    ret.name = ret_name

    for i in ret_addr:
        ret.problems.append(parse_problem(i))

    return ret
