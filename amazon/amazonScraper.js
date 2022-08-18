//Packages
const axios = require("axios");
const cheerio = require("cheerio");
const puppeteer = require("puppeteer");
require("dotenv").config();

// const url =
//     "https://www.amazon.co.uk/Apple-24-inch-8%E2%80%91core-7%E2%80%91core-ports/dp/B0932Y7SLQ?ref_=ast_slp_dp&th=1";

const url = "https://www.amazon.co.uk/dp/B08F9CXYX1/ref=uk_a_imac_1"

const product = { name: "", price: "", link: "" };

//Set interval
const handle = setInterval(scrape, 5000);

//connect with the proxy directly through code
async function proxy () {
    const browser = await puppeteer.launch({ 
        headless: true, 
        args: ['--proxy-server=23.109.113.44:10002'] 
    }); 
    const page = await browser.newPage(); 
    await page.authenticate();
    await browser.close();
}

async function scrape() {

    //Fetch the data
    const { data } = await axios.get(url);
    //Load up the html
    const $ = cheerio.load(data);
    const item = $("div#dp-container");
    //Extract the data that we need
    product.name = $(item).find("h1 span#productTitle").text();
    product.link = url;
    const price = $(item)
        .find("span .a-price-whole")
        .first()
        .text()
        .replace(/[,.]/g, "");
    const priceNum = parseInt(price);
    product.price = priceNum;
    console.log(product);
    //Log when price is low
    if (priceNum < 500) {
        console.log("It's cheaper now")
    }
}

proxy();
scrape();
