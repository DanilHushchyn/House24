$('.number').attr('value',generateNumber())
function generateNumber() {
    var chars = "0123456789";
    var string_length = 5;
    var randomstring1 = '';
    var randomstring2 = '';
    for (var i=0; i<string_length; i++) {
        var rnum = Math.floor(Math.random() * chars.length);
        randomstring1 += chars.substring(rnum,rnum+1);
    }
    for (var i=0; i<string_length; i++) {
        var rnum = Math.floor(Math.random() * chars.length);
        randomstring2 += chars.substring(rnum,rnum+1);
    }
    let result = randomstring1+'-'+randomstring2
    return result;
}
