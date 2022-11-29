require('dotenv').config()
// API_TOKEN = .API_TOKEN;

const base = "https://api.brightdata.com/dca/trigger?collector=c_lb1zn0xu28f5g9cjy8&queue_next=1"
// const base = "https://api.brightdata.com/dca/trigger_immediate?collector=c_lb1zn0xu28f5g9cjy8"
const fetchUrl="https://api.brightdata.com/dca/dataset?id=j_lb2e0ath88e9oiuj2"

function setLocation() {
    fetch(base, {
        method: "POST",
        body: JSON.stringify([{keyword: "chicago"}]),
        headers: {
            Authorization: `Bearer ${process.env.API_TOKEN}`,
            ContentType: "application/json"
        }
    })
    .then((response) => response.json())
    .then((data) => console.log(data));
}

function getData () {
    fetch(fetchUrl, {
        headers: {
            Authorization: `Bearer ${process.env.API_TOKEN}`,
            ContentType: "application/json"
        }
    })
    .then((response) => response.json())
    .then((data) => console.log(data));
}

// setLocation();
getData();