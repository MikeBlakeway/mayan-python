// Page transitions attached to 
var button = document.getElementById("left");

button.addEventListener('click', () => {
    var url = link;
    var layerClass = ".layer";
    var layers = document.querySelectorAll(layerClass);

    for (const layer of layers) {
        layer.classList.toggle("active");
    };
    document.getElementById("page").classList.add("fade");
    setTimeout(function () {
        document.location.href = url
    }, 900);
});