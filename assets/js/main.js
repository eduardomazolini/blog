// Dark/light toggle + persistência em localStorage
(function () {
  const toggleId = 'theme-toggle';
  const storageKey = 'theme'; // 'dark' | 'light' | null

  const applyClass = (theme) => {
    document.documentElement.classList.remove('dark', 'light');
    if (theme === 'dark') document.documentElement.classList.add('dark');
    else if (theme === 'light') document.documentElement.classList.add('light');
    // if theme is null/undefined, do not add either class (let @media do the job)
  };

  const currentEffectiveTheme = () => {
    // Priority: explicit class > stored (already applied) > system preference
    if (document.documentElement.classList.contains('dark')) return 'dark';
    if (document.documentElement.classList.contains('light')) return 'light';
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) return 'dark';
    return 'light';
  };

  const updateButton = (btn) => {
    if (!btn) return;
    const theme = currentEffectiveTheme();
    btn.textContent = theme === 'dark' ? '☀️' : '🌙';
  };

  const onClick = function () {
    // Toggle explicitly between dark and light (so user choice overrides system)
    const isCurrentlyDark = document.documentElement.classList.contains('dark') ||
      (!document.documentElement.classList.contains('light') && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);

    const newTheme = isCurrentlyDark ? 'light' : 'dark';
    applyClass(newTheme);
    localStorage.setItem(storageKey, newTheme);
    updateButton(this);
  };

  const init = () => {
    const stored = localStorage.getItem(storageKey); // 'dark' | 'light' | null

    if (stored === 'dark' || stored === 'light') {
      // Aplica escolha explícita do usuário
      applyClass(stored);
    } else {
      // Sem escolha do usuário: nenhuma classe explícita => deixa o @media cuidar disso
      // (ou, se quiser, poderia aplicar a preferencia do sistema como classe)
    }

    // Procura o botão (pode vir do include) e cria fallback se necessário
    let btn = document.getElementById(toggleId);
    if (!btn) {
      btn = document.createElement('button');
      btn.id = toggleId;
      btn.className = 'theme-toggle';
      document.body.appendChild(btn);
    }

    updateButton(btn);

    // Garante que não adicionamos múltiplos listeners
    btn.removeEventListener('click', onClick);
    btn.addEventListener('click', onClick);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();