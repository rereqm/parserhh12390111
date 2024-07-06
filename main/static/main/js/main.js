const buttons = document.querySelectorAll('.button');
const texts = document.querySelectorAll('.text');

buttons.forEach((button, index) => {

        const text = texts[index];
        const isHidden = text.style.display === 'none';
        text.style.display = isHidden ? 'block' : 'none';

        button.addEventListener('click', () => {
        const isHidden = text.style.display === 'none';
        text.style.display = isHidden ? 'block' : 'none';
        button.textContent = isHidden ? 'Скрыть' : 'Показать';
                });
            });