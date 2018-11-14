'use strict';
//for translation
var pathname = window.location.pathname; // Returns path only
if(pathname.endsWith("en.html")){
    $('#cn').attr("href",pathname.replace("_en.html",".html"));
}else{
    $('#en').attr("href",pathname.replace(".html","_en.html"));
}



//for img click
