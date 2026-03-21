const API_BASE = 'http://127.0.0.1:8000';
let currentUser = null;

// DOM Elements
const authScreen = document.getElementById('auth-screen');
const dashboardScreen = document.getElementById('dashboard-screen');
const currentUserDisplay = document.getElementById('current-user-display');
const authMsg = document.getElementById('auth-message');

// Authentication Forms
document.getElementById('login-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const id = document.getElementById('login-id').value.trim();
    if(id) {
        // Simulating login since we have no complex auth endpoint
        currentUser = id;
        showDashboard();
    }
});

document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const id = document.getElementById('reg-id').value.trim();
    const name = document.getElementById('reg-name').value.trim();
    const email = document.getElementById('reg-email').value.trim();
    const password = document.getElementById('reg-password').value;

    try {
        const res = await fetch(`${API_BASE}/users/`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({id, name, email, password})
        });
        const data = await res.json();
        if(res.ok) {
            authMsg.innerHTML = `<span class="success-text">Registered! Please login.</span>`;
            document.querySelector('.tab-btn[data-target="login"]').click();
            document.getElementById('login-id').value = id;
        } else {
            authMsg.innerHTML = `<span class="error-text">${data.detail || 'Error'}</span>`;
        }
    } catch(err) {
        authMsg.innerHTML = `<span class="error-text">Network error. Ensure backend is running.</span>`;
    }
});

document.getElementById('logout-btn').addEventListener('click', () => {
    currentUser = null;
    dashboardScreen.classList.remove('active');
    dashboardScreen.classList.add('hidden');
    authScreen.classList.remove('hidden');
    authScreen.classList.add('active');
});

// UI View Toggling
function showDashboard() {
    authScreen.classList.remove('active');
    authScreen.classList.add('hidden');
    dashboardScreen.classList.remove('hidden');
    dashboardScreen.classList.add('active');
    currentUserDisplay.textContent = currentUser;
}

// Tabs Logic
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        btn.classList.add('active');
        document.getElementById(btn.dataset.target).classList.add('active');
    });
});

// Main Nav Toggling
document.querySelectorAll('.nav-item').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.view-section').forEach(c => {
            c.classList.remove('active');
            c.classList.add('hidden');
        });
        btn.classList.add('active');
        const targetView = document.getElementById(`view-${btn.dataset.view}`);
        targetView.classList.remove('hidden');
        targetView.classList.add('active');
    });
});

// Manage Movies Forms
document.getElementById('add-movie-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const msgBox = document.getElementById('movie-msg');
    const id = document.getElementById('movie-id').value.trim();
    const title = document.getElementById('movie-title').value.trim();
    const summary = document.getElementById('movie-summary').value.trim();
    const genres = document.getElementById('movie-genres').value.split(',').map(g => g.trim());
    
    try {
        const res = await fetch(`${API_BASE}/movies/`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({id, title, summary, genres, poster_url:""})
        });
        const data = await res.json();
        if(res.ok) {
            msgBox.innerHTML = `<span class="success-text">Movie added successfully!</span>`;
            e.target.reset();
        } else {
            msgBox.innerHTML = `<span class="error-text">${data.detail || 'Error adding movie'}</span>`;
        }
    } catch(err) {
        msgBox.innerHTML = `<span class="error-text">Network error.</span>`;
    }
});

document.getElementById('like-movie-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const msgBox = document.getElementById('like-msg');
    const movie_id = document.getElementById('like-movie-id').value.trim();
    const rating = parseFloat(document.getElementById('like-rating').value);
    
    try {
        const res = await fetch(`${API_BASE}/movies/like`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({user_id: currentUser, movie_id, rating})
        });
        const data = await res.json();
        if(res.ok) {
            msgBox.innerHTML = `<span class="success-text">Liked! ${data.rating} stars.</span>`;
            e.target.reset();
        } else {
            msgBox.innerHTML = `<span class="error-text">${data.detail || 'Error liking movie'}</span>`;
        }
    } catch(err) {
        msgBox.innerHTML = `<span class="error-text">Network error.</span>`;
    }
});

// Manage Network Forms
document.getElementById('add-friend-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const msgBox = document.getElementById('friend-msg');
    const friend_id = document.getElementById('friend-id').value.trim();
    
    try {
        const res = await fetch(`${API_BASE}/users/friend`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({user_id: currentUser, friend_id})
        });
        const data = await res.json();
        if(res.ok) {
            msgBox.innerHTML = `<span class="success-text">Added friend successfully!</span>`;
            e.target.reset();
        } else {
            msgBox.innerHTML = `<span class="error-text">${data.detail || 'Error adding friend'}</span>`;
        }
    } catch(err) {
        msgBox.innerHTML = `<span class="error-text">Network error.</span>`;
    }
});

document.getElementById('find-path-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const resultBox = document.getElementById('path-result');
    const target_id = document.getElementById('path-target-id').value.trim();
    
    try {
        const res = await fetch(`${API_BASE}/users/path?user_id=${currentUser}&target_id=${target_id}`);
        const data = await res.json();
        if(res.ok) {
            const chainHtml = data.chain.join(' &rarr; ');
            resultBox.innerHTML = `<div><strong>Hops:</strong> ${data.hops}</div><div style="margin-top:0.5rem"><strong>Path:</strong> ${chainHtml}</div>`;
        } else {
            resultBox.innerHTML = `<span class="error-text">${data.detail || 'No path found'}</span>`;
        }
    } catch(err) {
        resultBox.innerHTML = `<span class="error-text">Network error.</span>`;
    }
});

// Recommendations Logic
document.querySelectorAll('.rec-btn').forEach(btn => {
    btn.addEventListener('click', async () => {
        document.querySelectorAll('.rec-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        const type = btn.dataset.type;
        const container = document.getElementById('recommendations-container');
        container.innerHTML = `<div class="empty-state">Loading recommendations...</div>`;
        
        try {
            const res = await fetch(`${API_BASE}/recommend/${type}/${currentUser}`);
            const data = await res.json();
            
            if(data.recommendations && data.recommendations.length > 0) {
                container.innerHTML = '';
                data.recommendations.forEach(rec => {
                    const r = rec.movie || rec; // Handle different cypher return shapes gracefully
                    const card = document.createElement('div');
                    card.className = 'movie-card';
                    card.innerHTML = `
                        <h4>${r.title || 'Unknown Title'}</h4>
                        <div class="score">Score: ${r.score ? r.score.toFixed(2) : (rec.score ? rec.score.toFixed(2) : 'N/A')}</div>
                        <p style="font-size:0.85rem; color:#cbd5e1">${(r.summary || '').substring(0, 80)}...</p>
                    `;
                    container.appendChild(card);
                });
            } else {
                container.innerHTML = `<div class="empty-state">No recommendations found. Try liking more movies or adding friends!</div>`;
            }
        } catch(err) {
            container.innerHTML = `<div class="empty-state error-text">Failed to load recommendations. Is backend running?</div>`;
        }
    });
});
