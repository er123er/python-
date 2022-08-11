function encryptApiKey() {
    var t = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
        , e = t.split("")
        , r = e.splice(0, 8);
    return e.concat(r).join("")
}



function getApiKey() {
    var t = (new Date).getTime()
        , e = encryptApiKey();
    return t = encryptTime(t),
        comb(e, t)
}
function encryptTime(t) {
    var e = (1 * t + 1111111111111).toString().split("")
        , r = 1
        , n = 1
        , o = 1;
    return e.concat([r, n, o]).join("")
}


function comb(t, e) {
    var r = "".concat(t, "|").concat(e);
    return btoa(r)
}


console.log(getApiKey())

