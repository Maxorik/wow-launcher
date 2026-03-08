import configparser
import asyncio
import os
from playwright.async_api import async_playwright, expect


script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, '../config.ini')
config = configparser.ConfigParser()
config.read(config_path)

warmane_url = "https://www.warmane.com/account"


async def vote_on_site():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            channel='chrome',
            headless=False,
            args=['--start-maximized', '--disable-blink-features=AutomationControlled']
        )

        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()

        await page.goto(warmane_url, wait_until="commit")

        await page.wait_for_timeout(3000)

        await page.type("#userID", config["SETTINGS"]["login"], delay=50)
        await page.type("#userPW", config["SETTINGS"]["password"], delay=50)
        await page.click("#frmLogin > div > button")

        try:
            await page.click("#page-content > div:nth-child(3) > div.content-inner.wm-ui-generic-frame.wm-ui-two-side-boxes.left.wm-ui-genericform.wm-ui-content-fontstyle.wm-ui-top-border.wm-ui-right-border.wm-ui-bottom-border > table > tbody > tr:nth-child(4) > td > span.myCollect > a")
        except:
            print('already voted')

        await page.wait_for_timeout(5000)
        await context.close()


if __name__ == "__main__":
    asyncio.run(vote_on_site())
    