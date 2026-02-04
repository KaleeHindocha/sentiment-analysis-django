window.addEventListener("load", function () {
    if (typeof polarityPercent !== "undefined") {
        const indicator = document.getElementById("indicator");
        const barWidth = document.querySelector(".sentiment-bar").offsetWidth;

        const position = (polarityPercent / 100) * barWidth;
        indicator.style.left = position + "px";
    }
});
