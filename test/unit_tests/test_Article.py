import pytest
from module.web_scraper import WebScrapper
from module.Article import Article
from bs4 import BeautifulSoup


@pytest.fixture()
def localFirstArticleSoup():
    with open("H:/Python/PyTest/Demo/test/unit_tests/test_files/firstArticleHTML.html", encoding="utf-8") as fp:
        contents = fp.read()
        soup = BeautifulSoup(contents, "lxml")
        for div in soup.find_all("div", class_="swp_social_panel"):
            div.decompose()
        return soup


@pytest.fixture()
def article_obj(localFirstArticleSoup):
    content = "\nАргументът „защо пак нови избори, нищо няма да се промени“ се среща често. Срещаше се и 2013г, когато протестирахме срещу кабинета на БСП и ДПС. И в двата случая, това е аргумент на тези, които се притесняват от избори. И е неверен по няколко причини.\nВече е ясно, че ГЕРБ няма да управлява – на предишните избори не беше ясно – много хора мислеха, че ще има пак някой трик, някое тайно съглашение по нощите и че щяхме да осъмнем с кабинет Борисов 4 или в най-добрия случай ГЕРБ 4 с Борисов, раздаващ задачи от „зайчарника“. Партиите в парламента удържаха обещанието си и без да формират управленска коалиция помежду си, не дадоха власт на ГЕРБ. Това е много значително, защото хората, които гласуват по принцип за победителя и/или за това да има управление, вече нямат причина да гласуват за ГЕРБ, защото те са в изолация и е ясно, че няма да управляват. Това води със себе си освен директно загубените гласове, и косвено загубените от корпоративните мрежи, които са чакали държавни пари по линия на управлението и затова са насочвали ресурс към ГЕРБ – ако те нямат такива гаранции, няма причина да наливат контролираните от тях гласове в празната каца на ГЕРБ. Не казвам, че ще мигрират към други партии, но може да се снишат.\nОпозиционните партии показаха принципност и конструктивност – Демократична България, Има такъв народ и Изправи се! показаха, че макар да имат фундаментални различия по много теми, могат да бъдат конструктивни по общи цели (т.нар. „тематични мнозинства“) и че не ги влече управлението на всяка цена. При ДБ и ИТН (слагам ДБ на първо място, защото съм част от тази коалиция) това според мен ще донесе допълнителни гласове. ИСМВ имат проблеми с кохерентността на групата си, които могат да нулират позитивите от тези няколко седмици."
    article = Article(None, None, content, None)
    return article


def test_set_content_to_first_three_paragraphs(article_obj, localFirstArticleSoup):
    content = localFirstArticleSoup.find("div", class_="entry-content clearfix").get_text()
    article = Article(None, None, content, None)
    article.set_content_to_first_three_paragraphs()
    article_obj.set_content_to_first_three_paragraphs()
    assert article.content == article_obj.content
