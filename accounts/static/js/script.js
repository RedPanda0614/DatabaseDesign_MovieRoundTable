window.addEventListener('scroll', function() {
    var scroll = window.pageYOffset || document.documentElement.scrollTop;
    document.querySelector('.fullscreen-bg').style.opacity = Math.min(1, scroll / 500);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('heroText').style.opacity = 1;
});

function showUserInfo() {
    document.getElementById('userInfo').style.display = 'block';
}

function hideUserInfo() {
    document.getElementById('userInfo').style.display = 'none';
}
