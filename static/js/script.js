let tempValueElement = document.getElementById('tempValue');
let tempValue = 0;

document.getElementById('increaseTemp').addEventListener('click', function() {
    tempValue++;
    tempValueElement.textContent = tempValue;
});

document.getElementById('decreaseTemp').addEventListener('click', function() {
    tempValue--;
    tempValueElement.textContent = tempValue;
});
