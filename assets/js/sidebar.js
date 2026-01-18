// sidebar.js: controls expand/collapse and search init
document.addEventListener('DOMContentLoaded', function () {
  // Expand/collapse logic
  document.querySelectorAll('.year-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const ul = btn.nextElementSibling;
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', expanded ? 'false' : 'true');
      if (ul) ul.hidden = expanded ? true : false;
    });
  });

  document.querySelectorAll('.month-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const ul = btn.nextElementSibling;
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', expanded ? 'false' : 'true');
      if (ul) ul.hidden = expanded ? true : false;
    });
  });

  // Initialize Simple-Jekyll-Search
  if (window.SimpleJekyllSearch) {
    SimpleJekyllSearch({
      searchInput: document.getElementById('search-input'),
      resultsContainer: document.getElementById('search-results'),
      json: '{{ "/search.json" | relative_url }}',
      searchResultTemplate: '<div class="search-item"><a href="{url}">{title}</a><div class="search-meta">{date} • {tags}</div></div>',
      noResultsText: 'Nenhum resultado',
      limit: 10,
      templateMiddleware: function (result) {
        result.tags = (result.tags || []).join(', ');
        return result;
      }
    });
  }
});