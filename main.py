import pytest
from playwright.sync_api import Page, expect, sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_homepage_title(page: Page):
    page.goto("https://discover.moscow/")
    expect(page).to_have_title("Discover Moscow")  # Убраны слеши для регулярного выражения
    assert "Discover Moscow" in page.title()


def test_search_button(page: Page):
    page.goto("https://discover.moscow/")

    # Вариант 1: Ищем по иконке поиска (более надежно)
    search_button = page.locator("[aria-label='Search']").or_(page.locator("button.search-icon"))