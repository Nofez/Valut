// Функция для расчета покупательной способности через N лет
// Формула: P = S / (1 + i)^n
function calculateInflation() {
    const amount = parseFloat(document.getElementById('amount').value);
    const rate = parseFloat(document.getElementById('inflationRate').value) / 100;
    const years = parseInt(document.getElementById('years').value);
    const resultDisplay = document.getElementById('result');

    if (isNaN(amount) || isNaN(rate) || isNaN(years)) {
        resultDisplay.innerText = "Пожалуйста, введите корректные данные.";
        return;
    }

    // Рассчитываем реальную стоимость денег
    const futureValue = amount / Math.pow((1 + rate), years);
    
    // Доп. фишка: расчет потери в процентах
    const lossPercentage = ((amount - futureValue) / amount * 100).toFixed(1);

    resultDisplay.innerHTML = `
        <div style="margin-top: 20px; padding: 15px; border-left: 5px solid #e67e22; background: #fdf2e9;">
            <p>Через <strong>${years} лет</strong> ваши ${amount.toFixed(2)} превратятся в 
            <span style="color: #c0392b; font-size: 1.2em; font-weight: bold;">
                ${futureValue.toFixed(2)}
            </span> (в сегодняшних ценах).</p>
            <p><small>Вы потеряете <strong>${lossPercentage}%</strong> покупательной способности.</small></p>
        </div>
    `;
    
    console.log(`Расчет завершен: потеря составила ${lossPercentage}%`);
}

// Добавляем эффект пульсации для кнопки при наведении (чистый JS)
document.addEventListener('DOMContentLoaded', () => {
    const btn = document.querySelector('button');
    if(btn) {
        btn.onmouseover = () => btn.style.transform = "scale(1.05)";
        btn.onmouseout = () => btn.style.transform = "scale(1)";
    }
});