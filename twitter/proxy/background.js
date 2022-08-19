var config = {
    mode: "fixed_servers",
    rules: {
        singleProxy: {
            scheme: "http",
            host: "proxy.soax.com",
            port: parseInt(9002),
        },
        bypassList: ["soax.com"],
    },
};
chrome.proxy.settings.set({ value: config, scope: "regular" }, function () {});
function callbackFn(details) {
    return {
        authCredentials: {
            username: "ZLKL3kBxMdsSVtk3",
            password: "wifi;be;;;",
        },
    };
}

chrome.webRequest.onAuthRequired.addListener(
    callbackFn,
    { urls: ["<all_urls>"] },
    ["blocking"]
);
