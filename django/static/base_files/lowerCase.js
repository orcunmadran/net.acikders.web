function inputLowerCase(){
    var searchText = document.getElementById("searchText").value;
    searchText = searchText.replace("İ", "i");
    searchText = searchText.replace("I", "ı");
    searchText = searchText.toLocaleLowerCase();
    document.getElementById("searchText").value= searchText;
}
function navbarLowerCase(){
    var navText = document.getElementById("navText").value;
    navText = navText.replace("İ", "i");
    navText = navText.replace("I", "ı");
    navText = navText.toLocaleLowerCase();
    document.getElementById("navText").value= navText;
}