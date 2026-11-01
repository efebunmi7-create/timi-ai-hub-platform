* {
  box-sizing: border-box;
}

:root {
  --bg: #090d1a;
  --panel: #101827;
  --panel-strong: #141f33;
  --panel-soft: #18253f;
  --line: rgba(148, 163, 184, 0.2);
  --text: #edf2ff;
  --muted: #8ca0bf;
  --primary: #7c3aed;
  --secondary: #3b82f6;
  --success: #34d399;
  --danger: #f87171;
  --warning: #fbbf24;
  --shadow: 0 20px 50px rgba(14, 20, 36, 0.45);
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  font-family: 'Inter', sans-serif;
  background: radial-gradient(circle at top left, rgba(124, 58, 237, 0.25), transparent 30%),
    radial-gradient(circle at top right, rgba(59, 130, 246, 0.2), transparent 30%),
    var(--bg);
  color: var(--text);
}

button,
input,
textarea {
  font: inherit;
}

button {
  cursor: pointer;
}

.app-shell {
  min-height: 100vh;
  display: flex;
}

.sidebar {
  width: 290px;
  background: rgba(10, 16, 28, 0.9);
  border-right: 1px solid var(--line);
  display: flex;
  flex-direction: column;
  padding: 20px 18px;
  position: sticky;
  top: 0;
  height: 100vh;
}

.brand-block {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 10px 8px 18px;
  border-bottom: 1px solid var(--line);
}

.brand-badge {
  width: 38px;
  height: 38px;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  border-radius: 12px;
  display: grid;
  place-items: center;
  font-weight: 800;
}

.brand-copy {
  display: flex;
  flex-direction: column;
}

.brand-copy strong {
  font-size: 1.05rem;
}

.brand-copy small {
  color: var(--muted);
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 22px 0;
}

.nav-btn,
.ghost-btn,
.primary-btn,
.auth-tab,
.tool-btn,
.close-btn {
  border: 1px solid transparent;
  border-radius: 12px;
  transition: all 0.2s ease;
}

.nav-btn {
  background: transparent;
  color: var(--text);
  text-align: left;
  padding: 12px 14px;
  border: 1px solid transparent;
}

.nav-btn.active {
  background: rgba(124, 58, 237, 0.14);
  border-color: rgba(124, 58, 237, 0.4);
}

.nav-btn:hover,
.ghost-btn:hover,
.primary-btn:hover,
.tool-btn:hover,
.auth-tab:hover {
  transform: translateY(-1px);
}

.sidebar-section {
  margin-top: 8px;
}

.section-label {
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 10px;
  text-transform: uppercase;
}

.category-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.category-item {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--line);
  color: var(--text);
  text-align: left;
  padding: 10px 12px;
  border-radius: 12px;
}

.category-item:hover {
  background: rgba(59, 130, 246, 0.08);
}

.sidebar-footer {
  margin-top: auto;
}

.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(52, 211, 153, 0.1);
  color: #b8f5da;
  padding: 8px 12px;
  border-radius: 999px;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--success);
  box-shadow: 0 0 14px rgba(52, 211, 153, 0.8);
}

.main-panel {
  flex: 1;
  padding: 24px 28px 36px;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding-bottom: 20px;
}

.search-wrap {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 10px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 0 14px;
  max-width: 680px;
}

.search-wrap input {
  width: 100%;
  background: transparent;
  border: none;
  outline: none;
  color: var(--text);
  padding: 14px 0;
}

.topbar-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.primary-btn,
.ghost-btn,
.tool-btn,
.auth-tab {
  padding: 11px 16px;
}

.primary-btn {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: #fff;
  box-shadow: var(--shadow);
}

.ghost-btn {
  background: rgba(255, 255, 255, 0.04);
  color: var(--text);
  border-color: var(--line);
}

#notificationCount {
  display: inline-grid;
  place-items: center;
  background: rgba(251, 191, 36, 0.2);
  color: #fef3c7;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  font-size: 0.72rem;
}

.hero-panel {
  background: linear-gradient(135deg, rgba(124, 58, 237, 0.14), rgba(59, 130, 246, 0.12));
  border: 1px solid rgba(124, 58, 237, 0.22);
  border-radius: 24px;
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 20px;
  padding: 26px;
  margin-bottom: 26px;
}

.hero-copy h1 {
  margin: 0 0 12px;
  line-height: 1.08;
  font-size: clamp(2.2rem, 2vw + 1rem, 3.2rem);
  max-width: 700px;
}

.eyebrow {
  color: #c4b5fd;
  letter-spacing: 0.1em;
  font-size: 0.78rem;
  text-transform: uppercase;
  margin-bottom: 10px;
}

.hero-copy p {
  color: var(--muted);
  line-height: 1.7;
  margin: 0 0 18px;
  max-width: 620px;
}

.hero-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.hero-metrics {
  display: grid;
  grid-template-columns: repeat(2, minmax(120px, 1fr));
  gap: 14px;
  align-content: center;
}

.metric-card {
  background: rgba(15, 23, 42, 0.72);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 18px 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.metric-label {
  color: var(--muted);
  font-size: 0.76rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.metric-card strong {
  font-size: 1.9rem;
}

.content-section {
  display: none;
  animation: fadeIn 0.2s ease;
}

.content-section.active-section {
  display: block;
}

.section-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.section-header-row h2 {
  margin: 0;
}

.section-header-row a,
.section-header-row span {
  color: #c7d2fe;
  text-decoration: none;
}

.bot-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
}

.bot-card {
  background: rgba(15, 23, 42, 0.72);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 18px 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-height: 200px;
}

.bot-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.bot-icon {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  font-size: 1.1rem;
  background: rgba(124, 58, 237, 0.12);
  border: 1px solid rgba(124, 58, 237, 0.25);
}

.bot-card h4 {
  margin: 0;
  font-size: 1.04rem;
}

.bot-card p {
  margin: 0;
  color: var(--muted);
  line-height: 1.6;
  flex: 1;
}

.bot-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  margin-top: auto;
}

.badge {
  display: inline-flex;
  align-items: center;
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 0.72rem;
  background: rgba(124, 58, 237, 0.08);
  color: #ddd6fe;
  border: 1px solid rgba(124, 58, 237, 0.24);
}

.badge.success {
  background: rgba(52, 211, 153, 0.1);
  color: #b7f8d6;
  border-color: rgba(52, 211, 153, 0.25);
}

.bot-card .primary-btn,
.bot-card .ghost-btn {
  width: 100%;
  justify-content: center;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}

.panel {
  background: rgba(15, 23, 42, 0.72);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 20px 18px;
}

.panel h3 {
  margin-top: 0;
}

.mini-stat-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(120px, 1fr));
  gap: 14px;
  margin-top: 16px;
}

.mini-stat {
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 14px;
  background: rgba(255, 255, 255, 0.02);
}

.mini-stat strong {
  display: block;
  font-size: 1.5rem;
  margin-top: 8px;
}

.feed-list {
  padding-left: 0;
  list-style-type: none;
  margin: 20px 0 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.feed-list li {
  padding: 10px 12px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--line);
  color: var(--muted);
}

.wide-panel {
  grid-column: 1 / -1;
}

.status-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 14px;
  margin-top: 16px;
}

.status-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 16px;
}

.status-card strong {
  display: block;
  margin-top: 8px;
}

.workspace-layout {
  display: grid;
  grid-template-columns: 1.4fr 0.8fr;
  gap: 18px;
}

.panel-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  margin-bottom: 16px;
}

.small-label {
  margin: 0 0 8px;
  color: var(--muted);
  font-size: 0.74rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.chat-window {
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-height: 260px;
  margin-bottom: 16px;
}

.message {
  padding: 14px 16px;
  border-radius: 14px;
  max-width: 90%;
  line-height: 1.6;
}

.message.assistant {
  background: rgba(124, 58, 237, 0.08);
  border: 1px solid rgba(124, 58, 237, 0.2);
}

.message.user {
  background: rgba(59, 130, 246, 0.08);
  border: 1px solid rgba(59, 130, 246, 0.2);
  align-self: flex-end;
}

.chat-form textarea {
  width: 100%;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--line);
  border-radius: 12px;
  color: var(--text);
  padding: 14px 16px;
  resize: vertical;
  min-height: 120px;
}

.chat-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 12px;
}

.bot-detail-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 14px;
  margin-top: 20px;
}

.bot-detail-card h4 {
  margin-top: 0;
}

.bot-detail-card p {
  color: var(--muted);
  line-height: 1.7;
}

.quick-tools {
  display: grid;
  grid-template-columns: repeat(2, minmax(120px, 1fr));
  gap: 10px;
  margin-top: 18px;
}

.tool-btn {
  background: rgba(255, 255, 255, 0.03);
  color: var(--text);
  border: 1px solid var(--line);
}

.modal {
  position: fixed;
  inset: 0;
  background: rgba(2, 6, 23, 0.72);
  display: grid;
  place-items: center;
  z-index: 1000;
}

.modal.hidden {
  display: none;
}

.modal-card {
  width: min(440px, calc(100% - 32px));
  background: rgba(15, 23, 42, 0.96);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 20px;
  box-shadow: var(--shadow);
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.close-btn {
  width: 32px;
  height: 32px;
  background: rgba(255, 255, 255, 0.04);
  color: var(--text);
  border-color: var(--line);
}

.auth-tabs {
  display: flex;
  gap: 10px;
  margin: 20px 0 16px;
}

.auth-tab {
  background: rgba(255, 255, 255, 0.02);
  color: var(--muted);
  border-color: var(--line);
  flex: 1;
}

.auth-tab.active {
  background: rgba(124, 58, 237, 0.15);
  color: var(--text);
  border-color: rgba(124, 58, 237, 0.3);
}

.form-group {
  margin-bottom: 12px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  color: var(--muted);
}

.form-group input {
  width: 100%;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--line);
  border-radius: 12px;
  color: var(--text);
  padding: 12px 14px;
}

.full-width {
  width: 100%;
  margin-top: 6px;
}

.hidden {
  display: none !important;
}

@media (max-width: 980px) {
  .app-shell {
    display: block;
  }

  .sidebar {
    width: 100%;
    height: auto;
    position: relative;
    border-right: none;
    border-bottom: 1px solid var(--line);
  }

  .main-panel {
    padding: 18px 18px 30px;
  }

  .hero-panel,
  .workspace-layout,
  .dashboard-grid {
    grid-template-columns: 1fr;
  }

  .topbar {
    flex-wrap: wrap;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(6px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
