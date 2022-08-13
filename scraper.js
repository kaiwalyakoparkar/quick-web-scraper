//Package inclusions
const axios = require('axios');
const cheerio = require('cheerio');
const express = require('express');

//Declarations
const PORT = 8080;
const app = express();
const url = 'https://dev.to/';

//Scripts
axios(url)
    .then(res => {
        const html = res.data;
        //console.log(html)
        const $ = cheerio.load(html);
        const articles = [];

        $('.crayons-story__title', html).each(function() {
            const title = $(this).text();
            const url = $(this).find('a').attr('href');

            articles.push({
                title,
                url
            })
        })

        console.log(articles);
    }).catch(err => console.log(err))

//Server initialization
app.listen(PORT, () => {
    console.log(`server running on PORT ${PORT}`);
})