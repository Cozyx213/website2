document.addEventListener('DOMContentLoaded', function () {
    var ghost = document.getElementById("ghost");
    var numberContainer = document.getElementById("counter_container");
    var clickCount = 0;
    var retry = document.getElementById("retry");
    var isMouseOverGhost = false;
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    function updateNumber(count) {
        numberContainer.innerText = count;
    }
    function teleportGhost() {


        var newX = Math.random() * (window.innerWidth - ghost.width);
        var newY = Math.random() * (window.innerHeight - ghost.height);


        ghost.style.left = newX + 'px';
        ghost.style.top = newY + 'px';



    }

    
    retry.addEventListener("click", function () {
        clickCount = 0;
        updateNumber(clickCount);
    });
    ghost.addEventListener("mousedown", function () {
        clickCount++;
        updateNumber(clickCount);
        teleportGhost();
    });
    async function teleportLoop() {
        while (clickCount < 9) {
            var level = clickCount * 100
            await sleep(1000 - level);
            teleportGhost();
        }

    }
    teleportLoop()

});
