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
    top.location.href='mark_user.html'
}

function profil(i)
{
    top.location.href='Dmitry_Shop.html'
}

function statistica(i)
{
    top.location.href='Dmitry_Table.html'
}