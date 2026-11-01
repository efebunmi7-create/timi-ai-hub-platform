const state = {
  bots: [],
  filteredBots: [],
  selectedBotId: 'general-ai',
  user: null,
  authMode: 'login'
};

const categoryLabelMap = {
  'AI Chat Bots': 'AI Bots',
  'Telegram Bots': 'Telegram',
  'Website Automation': 'Web Automation',
  'Developer Tools': 'Dev Tools',
  'Business Bots': 'Business',
  'Social Media Bots': 'Social',
  'Security & Testing': 'Security',
  'File & Documents': 'Files',
  'Entertainment': 'Entertainment'
};

const elements = {
  categoryList: document.getElementById('categoryList'),
  featuredBots: document.getElementById('featuredBots'),
  botGrid: document.getElementById('botGrid'),
  botCountLabel: document.getElementById('botCountLabel'),
  searchInput: document.getElementById('searchInput'),
  navButtons: [...document.querySelectorAll('.nav-btn')],
  sections: [...document.querySelectorAll('.content-section')],
  authModal: document.getElementById('authModal'),
  authForm: document.getElementById('authForm'),
  authSubmitBtn: document.getElementById('authSubmitBtn'),
  nameGroup: document.getElementById('nameGroup'),
  authTrigger: document.getElementById('authTrigger'),
  chatForm: document.getElementById('chatForm'),
  promptInput: document.getElementById('promptInput'),
  workspaceBotName: document.getElementById('workspaceBotName'),
  workspaceBotStatus: document.getElementById('workspaceBotStatus'),
  workspaceMessages: document.getElementById('workspaceMessages'),
  botDetailCard: document.getElementById('botDetailCard'),
  metricUsers: document.getElementById('metricUsers'),
  metricActive: document.getElementById('metricActive'),
  metricUsage: document.getElementById('metricUsage'),
  metricApi: document.getElementById('metricApi'),
  analyticsCards: document.getElementById('analyticsCards'),
  activityFeed: document.getElementById('activityFeed'),
  statusPanel: document.getElementById('statusPanel'),
  viewAllBots: document.getElementById('viewAllBots'),
  launchBotsBtn: document.getElementById('launchBotsBtn'),
  dashboardBtn: document.getElementById('dashboardBtn'),
  systemStatusBtn: document.getElementById('systemStatusBtn')
};

function $(selector) {
  return document.querySelector(selector);
}

async function apiFetch(url, options = {}) {
  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {})
    },
    ...options
  });

  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.message || 'Request failed');
  }
  return data;
}

function setActiveView(view) {
  elements.navButtons.forEach((btn) => {
    btn.classList.toggle('active', btn.dataset.view === view);
  });

  elements.sections.forEach((section) => {
    const match = section.id === `${view}Section`;
    section.classList.toggle('active-section', match);
  });
}

function renderCategories() {
  const categories = ['AI Chat Bots', 'Telegram Bots', 'Website Automation', 'Developer Tools', 'Business Bots', 'Social Media Bots', 'Security & Testing', 'File & Documents', 'Entertainment'];

  elements.categoryList.innerHTML = categories.map((category) => `
    <button class="category-item" data-category="${category}">${categoryLabelMap[category] || category}</button>
  `).join('');

  elements.categoryList.querySelectorAll('.category-item').forEach((btn) => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.category;
      applyFilter(filter);
      setActiveView('bots');
    });
  });
}

function applyFilter(category) {
  const search = elements.searchInput.value.trim().toLowerCase();
  state.filteredBots = state.bots.filter((bot) => {
    const matchesCategory = category === 'all' || bot.category === category;
    const matchesSearch = !search || `${bot.name} ${bot.description}`.toLowerCase().includes(search);
    return matchesCategory && matchesSearch;
  });
  renderBotList();
}

function renderBotList() {
  const bots = state.filteredBots.length ? state.filteredBots : state.bots;
  elements.botCountLabel.textContent = `${bots.length} tools`;

  elements.botGrid.innerHTML = bots.map((bot) => `
    <article class="bot-card" data-bot-id="${bot.id}">
      <div class="bot-card-header">
        <div class="bot-icon" style="background:${bot.color === 'purple' ? 'rgba(124,58,237,0.12)' : 'rgba(59,130,246,0.12)'}; border-color:${bot.color === 'purple' ? 'rgba(124,58,237,0.25)' : 'rgba(59,130,246,0.25)'};">${iconFor(bot.icon)}</div>
        <span class="badge success">${bot.tier}</span>
      </div>
      <div>
        <h4>${bot.name}</h4>
      </div>
      <p>${bot.description}</p>
      <div class="bot-meta">
        <span class="badge">${bot.category}</span>
        <button class="primary-btn open-bot" data-bot-id="${bot.id}">Launch</button>
      </div>
    </article>
  `).join('');

  const cards = [...document.querySelectorAll('.open-bot')];
  cards.forEach((button) => {
    button.addEventListener('click', () => {
      const botId = button.dataset.botId;
      selectBot(botId);
      setActiveView('workspace');
    });
  });

  const featured = bots.slice(0, 6);
  elements.featuredBots.innerHTML = featured.map((bot) => `
    <article class="bot-card">
      <div class="bot-card-header">
        <div class="bot-icon">${iconFor(bot.icon)}</div>
        <span class="badge success">${bot.tier}</span>
      </div>
      <div>
        <h4>${bot.name}</h4>
      </div>
      <p>${bot.description}</p>
      <div class="bot-meta">
        <span class="badge">${bot.category}</span>
        <button class="primary-btn open-bot" data-bot-id="${bot.id}">Open</button>
      </div>
    </article>
  `).join('');

  elements.featuredBots.querySelectorAll('.open-bot').forEach((button) => {
    button.addEventListener('click', () => {
      selectBot(button.dataset.botId);
      setActiveView('workspace');
    });
  });
}

function selectBot(botId) {
  const bot = state.bots.find((item) => item.id === botId) || state.bots[0];
  state.selectedBotId = bot.id;

  elements.workspaceBotName.textContent = bot.name;
  elements.workspaceBotStatus.textContent = bot.status;
  elements.workspaceBotStatus.className = `badge ${bot.status === 'Available' ? 'success' : ''}`;

  elements.botDetailCard.innerHTML = `
    <h4>${bot.name}</h4>
    <p>${bot.description}</p>
    <div class="badge">${bot.category}</div>
    <p><strong>Tier:</strong> ${bot.tier}</p>
    <p><strong>status:</strong> ${bot.status}</p>
  `;
}

function iconFor(name) {
  const icons = {
    sparkles: '✦',
    code: '</>',
    calculator: '∑',
    'pen-square': '✎',
    languages: 'A',
    spellcheck: '✓',
    'book-open': '📘',
    'file-pdf': 'PDF',
    image: '◌',
    mic: '🎙',
    'graduation-cap': '🎓',
    briefcase: '▣',
    'check-square': '☑',
    messages: '✉',
    'help-circle': '?',
    bot: '🤖',
    bell: '🔔',
    users: '👥',
    'door-open': '🚪',
    'alarm-clock': '⏰',
    'message-square-text': '💬',
    package: '▤',
    globe: '🌐',
    'list-checks': '✓',
    mail: '✉',
    'calendar-check': '📅',
    'search-check': '⌕',
    'file-code': '</>',
    paintbrush: '🖌',
    terminal: '⌨',
    python: 'PY',
    server: '▣',
    bug: '🐞',
    plug: '⚡',
    braces: '{}',
    regex: '.*',
    'layout-template': '▦',
    building: '🏢',
    sales: '↗',
    receipt: '🧾',
    megaphone: '📣',
    caption: '✍',
    hash: '#',
    lightbulb: '💡',
    'shield-check': '🛡',
    shield: '🛡',
    key: '🔑',
    certificate: '✓',
    'scan-search': '⌕',
    activity: '⚡',
    'file-text': 'T',
    arrows: '⇄',
    ocr: 'OCR',
    'user-circle': '◉',
    'sticky-note': '✎',
    book: '📚',
    laugh: '😄',
    'question-mark': '?',
    film: '🎬',
    gamepad: '🎮'
  };

  return icons[name] || '✦';
}

function renderDashboard(data) {
  const stats = data.stats || {};
  elements.metricUsers.textContent = stats.registered_users ?? 0;
  elements.metricActive.textContent = stats.active_users ?? 0;
  elements.metricUsage.textContent = stats.bot_usage ?? 0;
  elements.metricApi.textContent = stats.api_usage ?? 0;

  elements.analyticsCards.innerHTML = `
    <div class="mini-stat"><span>Subscriptions</span><strong>${stats.subscriptions ?? 0}</strong></div>
    <div class="mini-stat"><span>System uptime</span><strong>${stats.system_uptime ?? '99.94%'}</strong></div>
    <div class="mini-stat"><span>AI models</span><strong>4</strong></div>
    <div class="mini-stat"><span>Bot coverage</span><strong>45+</strong></div>
  `;

  const logs = data.logs || [];
  elements.activityFeed.innerHTML = logs.slice(0, 8).map((entry) => `
    <li>${entry.description} • ${new Date(entry.created_at).toLocaleString()}</li>
  `).join('');

  elements.statusPanel.innerHTML = `
    <div class="status-card"><span>Platform</span><strong>Healthy</strong></div>
    <div class="status-card"><span>Database</span><strong>Connected</strong></div>
    <div class="status-card"><span>Analytics</span><strong>Operational</strong></div>
    <div class="status-card"><span>API layer</span><strong>Secure</strong></div>
  `;
}

function renderAuthState() {
  const isLogin = state.authMode === 'login';
  elements.nameGroup.classList.toggle('hidden', isLogin);
  elements.authSubmitBtn.textContent = isLogin ? 'Login' : 'Create account';
  document.querySelectorAll('.auth-tab').forEach((tab) => {
    tab.classList.toggle('active', tab.dataset.auth === state.authMode);
  });
}

function openAuthModal() {
  elements.authModal.classList.remove('hidden');
}

function closeAuthModal() {
  elements.authModal.classList.add('hidden');
}

async function loadData() {
  try {
    const [botData, dashboardData, meData, statusData] = await Promise.all([
      apiFetch('/api/bots'),
      apiFetch('/api/dashboard'),
      apiFetch('/api/auth/me'),
      apiFetch('/api/system-status')
    ]);

    state.bots = botData.bots || [];
    state.filteredBots = [...state.bots];
    state.user = meData.user;
    renderBotList();
    renderDashboard(dashboardData);
    renderSystemStatus(statusData);
    updateUserState();
  } catch (error) {
    console.error('Failed to load app data:', error);
  }
}

function updateUserState() {
  const user = state.user;
  if (user) {
    elements.authTrigger.textContent = `${user.name}`;
  } else {
    elements.authTrigger.textContent = 'Login / Register';
  }
}

function renderSystemStatus(data) {
  const status = data.status || 'online';
  const statusPill = document.querySelector('.status-pill');
  statusPill.innerHTML = `<span class="dot"></span> ${status === 'online' ? 'System online' : 'System monitoring'}`;
}

async function handleAuthSubmit(event) {
  event.preventDefault();
  const name = $('#nameInput')?.value.trim() || '';
  const email = $('#emailInput').value.trim();
  const password = $('#passwordInput').value;

  try {
    const endpoint = state.authMode === 'login' ? '/api/auth/login' : '/api/auth/register';
    const payload = {
      name,
      email,
      password
    };

    const result = await apiFetch(endpoint, {
      method: 'POST',
      body: JSON.stringify(payload)
    });

    state.user = result.user;
    updateUserState();
    closeAuthModal();
    showToast(result.message || 'Success');
    await loadData();
  } catch (error) {
    showToast(error.message, true);
  }
}

function showToast(message, isError = false) {
  const existing = document.querySelector('.toast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.className = `toast ${isError ? 'error' : ''}`;
  toast.textContent = message;
  toast.style.position = 'fixed';
  toast.style.right = '20px';
  toast.style.bottom = '20px';
  toast.style.zIndex = '2000';
  toast.style.background = isError ? 'rgba(248,113,113,0.15)' : 'rgba(52,211,153,0.15)';
  toast.style.border = '1px solid ' + (isError ? 'rgba(248,113,113,0.3)' : 'rgba(52,211,153,0.3)');
  toast.style.color = '#fff';
  toast.style.borderRadius = '12px';
  toast.style.padding = '12px 16px';
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 2600);
}

async function handleChatSubmit(event) {
  event.preventDefault();
  const prompt = elements.promptInput.value.trim();
  if (!prompt) {
    showToast('Please enter a prompt first.', true);
    return;
  }

  const bot = state.bots.find((item) => item.id === state.selectedBotId) || state.bots[0];

  const userMessage = document.createElement('div');
  userMessage.className = 'message user';
  userMessage.innerHTML = `<strong>You</strong><p>${prompt}</p>`;
  elements.workspaceMessages.appendChild(userMessage);
  elements.promptInput.value = '';

  try {
    const result = await apiFetch('/api/chat', {
      method: 'POST',
      body: JSON.stringify({ bot_id: bot.id, prompt })
    });

    const assistantMessage = document.createElement('div');
    assistantMessage.className = 'message assistant';
    assistantMessage.innerHTML = `<strong>${bot.name}</strong><p>${result.response.output}</p>`;
    elements.workspaceMessages.appendChild(assistantMessage);
    elements.workspaceMessages.scrollTop = elements.workspaceMessages.scrollHeight;
  } catch (error) {
    showToast(error.message, true);
  }
}

function bindEvents() {
  elements.searchInput.addEventListener('input', () => applyFilter('all'));

  elements.navButtons.forEach((button) => {
    button.addEventListener('click', () => setActiveView(button.dataset.view));
  });

  document.getElementById('viewAllBots').addEventListener('click', (event) => {
    event.preventDefault();
    setActiveView('bots');
  });

  document.getElementById('launchBotsBtn').addEventListener('click', () => setActiveView('bots'));
  document.getElementById('dashboardBtn').addEventListener('click', () => setActiveView('dashboard'));
  document.getElementById('systemStatusBtn').addEventListener('click', async () => {
    const data = await apiFetch('/api/system-status');
    showToast(data.message || 'System healthy');
  });

  document.getElementById('closeAuthModal').addEventListener('click', closeAuthModal);
  elements.authTrigger.addEventListener('click', openAuthModal);

  document.querySelectorAll('.auth-tab').forEach((tab) => {
    tab.addEventListener('click', () => {
      state.authMode = tab.dataset.auth;
      renderAuthState();
    });
  });

  elements.authForm.addEventListener('submit', handleAuthSubmit);
  elements.chatForm.addEventListener('submit', handleChatSubmit);

  document.getElementById('clearChatBtn').addEventListener('click', () => {
    elements.workspaceMessages.innerHTML = `
      <div class="message assistant">
        <strong>Assistant</strong>
        <p>Ready to help. Tell me what you want to create, automate, or improve.</p>
      </div>
    `;
  });

  document.querySelectorAll('.tool-btn').forEach((button) => {
    button.addEventListener('click', () => {
      const tool = button.dataset.tool;
      const prompt = {
        summarize: 'Summarize this opportunity and list the most important actions.',
        brainstorm: 'Brainstorm a practical set of ideas for growth and engagement.',
        plan: 'Create a clear 7-day action plan with milestones.',
        export: 'Provide a ready-to-share summary you can export to stakeholders.'
      }[tool] || 'Create a detailed plan.';
      elements.promptInput.value = prompt;
      setActiveView('workspace');
    });
  });

  document.addEventListener('click', (event) => {
    const clickTarget = event.target;
    if (clickTarget === elements.authModal) {
      closeAuthModal();
    }
  });
}

renderCategories();
renderAuthState();
bindEvents();
selectBot(state.selectedBotId);
loadData();
