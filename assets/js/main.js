// Dark mode toggle + persistência em localStorage
document.addEventListener('DOMContentLoaded', function () {
  const toggleId = 'theme-toggle';
  const stored = localStorage.getItem('theme'); // 'dark' | 'light' | null

  const apply = (theme) => {
    if (theme === 'dark') document.documentElement.classList.add('dark');
    else document.documentElement.classList.remove('dark');
  };

  // Aplica preferência salva ou preferência do sistema
  if (stored) {
    apply(stored);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    apply('dark');
  }

  // Atualiza o texto do botão (se existir)
  const updateButton = (btn) => {
    if (!btn) return;
    btn.textContent = document.documentElement.classList.contains('dark') ? '☀️' : '🌙';
  };

  // Cria botão se ele não existir no HTML (fallback)
  let btn = document.getElementById(toggleId);
  if (!btn) {
    btn = document.createElement('button');
    btn.id = toggleId;
    btn.className = 'theme-toggle';
    document.body.appendChild(btn);
  }

  updateButton(btn);

  btn.addEventListener('click', function () {
    const isDark = document.documentElement.classList.toggle('dark');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    updateButton(btn);
  });
});