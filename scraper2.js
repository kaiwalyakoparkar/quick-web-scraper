const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage();
    await page.goto("https://dev.to/")

    const grabParagraph = await page.evaluate(() => {
        const pgTag = document.querySelector(".crayons-story.crayons-story--featured a");
        return pgTag.innerText;
    });

    console.log(grabParagraph);
    await browser.close();
})