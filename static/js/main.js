const btn = document.getElementById('themeBtn');

function applyTheme(theme) {
    if (theme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
        btn.textContent = '☀️';
    } else {
        document.documentElement.removeAttribute('data-theme');
        btn.textContent = '🌙';
    }
}

function toggleTheme() {
    let current = localStorage.getItem('theme') || 'dark';
    let next = current === 'dark' ? 'light' : 'dark';

    localStorage.setItem('theme', next);
    applyTheme(next);
}

applyTheme(localStorage.getItem('theme') || 'dark');


function likePost(postId) {
    fetch(`/blog/${postId}/like/`)
    .then(res => res.json())
    .then(data => {
        document.getElementById("like-count").innerText = data.likes;
    });
}

