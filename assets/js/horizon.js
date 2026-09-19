(function () {
  'use strict';

  /** Replace ⭐️ N/10 with a colored badge in h2, h3, and li elements */
  function processScoreBadges() {
    var scoreRe = /⭐️\s*(\d+(?:\.\d+)?)\/10/;
    var targets = document.querySelectorAll('.main-content h2, .main-content h3, .main-content li');
    targets.forEach(function (el) {
      var m = el.innerHTML.match(scoreRe);
      if (!m) return;
      var score = parseFloat(m[1]);
      var tier;
      if (score >= 9) tier = 'high';
      else if (score >= 7) tier = 'good';
      else if (score >= 5) tier = 'mid';
      else tier = 'low';
      el.innerHTML = el.innerHTML.replace(
        scoreRe,
        '<span class="score-badge" data-tier="' + tier + '">' + m[1] + '</span>'
      );
    });
  }

  /** Add semantic classes to tag lines, source lines, and background paragraphs */
  function markSemanticElements() {
    var paragraphs = document.querySelectorAll('.main-content p');
    paragraphs.forEach(function (p) {
      var text = p.textContent.trim();

      // Tag line: starts with Tags or 标签 (bold prefix rendered by Markdown)
      if (/^(Tags|标签)\s*:/.test(text)) {
        p.classList.add('tag-line');
        return;
      }

      // Source line: pattern like "source · site · date"
      if (/^(rss|reddit|github|hackernews|hn|telegram|twitter|follow builders|aihot|openbb|ossinsight|gdelt|google news|google_news)\s*·/i.test(text)) {
        p.classList.add('source-line');
        return;
      }
    });
  }

  /** Fill dashboard metrics and normalize the recent-digest trend. */
  function setupDashboard() {
    var dashboard = document.querySelector('[data-dashboard]');
    if (!dashboard) return;

    var scoreBadges = Array.prototype.slice.call(
      dashboard.querySelectorAll('[data-dashboard-ranking] .score-badge')
    );
    var scores = scoreBadges
      .map(function (badge) {
        return parseFloat(badge.textContent);
      })
      .filter(function (score) {
        return Number.isFinite(score);
      });

    var highest = dashboard.querySelector('[data-dashboard-highest]');
    var average = dashboard.querySelector('[data-dashboard-average]');
    if (scores.length > 0) {
      var total = scores.reduce(function (sum, score) {
        return sum + score;
      }, 0);
      highest.textContent = Math.max.apply(Math, scores).toFixed(1);
      average.textContent = (total / scores.length).toFixed(1);
    } else {
      highest.textContent = '—';
      average.textContent = '—';
    }

    var trendItems = Array.prototype.slice.call(
      dashboard.querySelectorAll('[data-digest-trend] li')
    );
    var counts = trendItems.map(function (item) {
      return parseInt(item.getAttribute('data-count'), 10) || 0;
    });
    var maxCount = Math.max.apply(Math, counts.concat([1]));

    trendItems.forEach(function (item, index) {
      var bar = item.querySelector('.trend-bar');
      if (!bar) return;
      var width = counts[index] === 0 ? 0 : Math.max(8, (counts[index] / maxCount) * 100);
      bar.style.setProperty('--trend-width', width + '%');
    });
  }

  /** Enhance the Pages archive into accessible source tabs. */
  function setupArchiveTabs() {
    var archives = document.querySelectorAll('[data-archive-tabs]');
    archives.forEach(function (archive) {
      var tablist = archive.querySelector('[role="tablist"]');
      var tabs = Array.prototype.slice.call(archive.querySelectorAll('[role="tab"]'));
      var panels = Array.prototype.slice.call(archive.querySelectorAll('[role="tabpanel"]'));
      if (!tablist || tabs.length === 0 || panels.length === 0) return;

      var initialIndex = tabs.findIndex(function (tab) {
        return Number(tab.getAttribute('data-count') || 0) > 0;
      });
      if (initialIndex < 0) initialIndex = 0;

      function activateTab(index, moveFocus) {
        tabs.forEach(function (tab, tabIndex) {
          var active = tabIndex === index;
          tab.setAttribute('aria-selected', active ? 'true' : 'false');
          tab.setAttribute('tabindex', active ? '0' : '-1');
        });
        panels.forEach(function (panel, panelIndex) {
          panel.hidden = panelIndex !== index;
        });
        if (moveFocus) tabs[index].focus();
      }

      tabs.forEach(function (tab, index) {
        tab.addEventListener('click', function () {
          activateTab(index, false);
        });
        tab.addEventListener('keydown', function (event) {
          var nextIndex = index;
          if (event.key === 'ArrowRight') nextIndex = (index + 1) % tabs.length;
          else if (event.key === 'ArrowLeft') nextIndex = (index - 1 + tabs.length) % tabs.length;
          else if (event.key === 'Home') nextIndex = 0;
          else if (event.key === 'End') nextIndex = tabs.length - 1;
          else return;
          event.preventDefault();
          activateTab(nextIndex, true);
        });
      });

      archive.classList.add('is-enhanced');
      tablist.hidden = false;
      activateTab(initialIndex, false);
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    processScoreBadges();
    markSemanticElements();
    setupDashboard();
    setupArchiveTabs();
  });
})();
