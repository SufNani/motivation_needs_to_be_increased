document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.querySelector('.toggle-footer-btn');
    const footer = document.querySelector('.footer');

    toggleButton.addEventListener('click', function() {
        footer.classList.toggle('hidden');
        toggleButton.textContent = footer.classList.contains('hidden') ? 'Показать футер' : 'Скрыть футер';
    });
});

function klikaj(i)
{
    top.location.href='/user'
}

function profil(i)
{
    top.location.href='/shop'
}

function statistica(i)
{
    top.location.href='/table'
}