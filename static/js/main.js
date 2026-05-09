const btn = document.getElementById('themeBtn');

function applyTheme(theme) {
    if (theme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        if (btn) btn.textContent = '☀️';
    } else {
        document.documentElement.removeAttribute('data-theme');
        if (btn) btn.textContent = '🌙';
    }
}

function toggleTheme() {
    let current = localStorage.getItem('theme') || 'light';
    let next = current === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', next);
    applyTheme(next);
}

applyTheme(localStorage.getItem('theme') || 'light');

function likePost(postId) {
    fetch(`/likes/${postId}/like/`, {
        method: "POST",
        headers: { "X-CSRFToken": getCSRFToken() }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("like-count").innerText = data.likes;
        let likeBtn = document.querySelector(".like-btn");
        if (likeBtn) likeBtn.style.color = data.liked ? "red" : "";
    });
}

function getCSRFToken() {
    for (let c of document.cookie.split(';')) {
        c = c.trim();
        if (c.startsWith('csrftoken=')) return c.substring(10);
    }
}