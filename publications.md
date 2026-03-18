---
layout: page
title: Publications
permalink: /publications/
---
<style>.post-header { display: none; }</style>
<script>
(function () {
  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      try {
        var ta = document.createElement('textarea');
        ta.value = text;
        ta.setAttribute('readonly', '');
        ta.style.position = 'fixed';
        ta.style.top = '-1000px';
        document.body.appendChild(ta);
        ta.select();
        var ok = document.execCommand('copy');
        document.body.removeChild(ta);
        ok ? resolve() : reject(new Error('copy failed'));
      } catch (e) {
        reject(e);
      }
    });
  }

  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a.publication-cite') : null;
    if (!a) return;
    e.preventDefault();
    var bibtex = a.getAttribute('data-bibtex') || '';
    copyText(bibtex).then(function () {
      var old = a.textContent;
      a.textContent = 'Copied';
      window.setTimeout(function () { a.textContent = old; }, 1200);
    });
  });
})();
</script>

<h1 style="font-size: 2.5em; margin-bottom: 20px;">Publications</h1>
<p style="font-size: 1.1em; margin-bottom: 30px;">For a complete list, see my <a href="https://scholar.google.com/citations?user=DuqZJvsAAAAJ&hl=de&authuser=1">Google Scholar profile</a>.</p>

<div style="margin-bottom: 40px;">
  <h2 style="margin-bottom: 28px; font-size: 1.8em;">2026</h2>
  <div class="card publication-card">
  <div class="publication-grid">
    <div class="publication-image">
      <img src="/assets/images/Multi-Agent-Framework.webp" alt="Publication">
    </div>
    <div class="publication-content">
      <h3 class="publication-title">Beyond Static Instruction: A Multi-agent AI Framework for Adaptive Augmented Reality Robot Training</h3>
      <div class="publication-authors">Nicolas Leins, Jana Gonnermann-Müller, Malte Teichmann, Sebastian Pokutta</div>
      <div class="publication-venue">Companion Proceedings of the 21st ACM/IEEE International Conference on Human-Robot Interaction, Mar 2026</div>
      <div class="publication-links"><a class="publication-cite" href="#" data-bibtex="@inproceedings&#123;leins_beyond_2026,&#10;	title = &#123;Beyond &#123;Static&#125; &#123;Instruction&#125;: &#123;A&#125; &#123;Multi&#125;-agent &#123;AI&#125; &#123;Framework&#125; for &#123;Adaptive&#125; &#123;Augmented&#125; &#123;Reality&#125; &#123;Robot&#125; &#123;Training&#125;&#125;,&#10;	author = &#123;Leins, Nicolas and Gonnermann-Müller, Jana and Teichmann, Malte and Pokutta, Sebastian&#125;,&#10;	booktitle = &#123;Companion &#123;Proceedings&#125; of the 21st &#123;ACM&#125;/&#123;IEEE&#125; &#123;International&#125; &#123;Conference&#125; on &#123;Human&#125;-&#123;Robot&#125; &#123;Interaction&#125;&#125;,&#10;	publisher = &#123;Association for Computing Machinery&#125;,&#10;	year = &#123;2026&#125;,&#10;	pages = &#123;989--993&#125;,&#10;	doi = &#123;10.1145/3776734.3794542&#125;,&#10;	url = &#123;https://doi.org/10.1145/3776734.3794542&#125;,&#10;	shorttitle = &#123;Beyond &#123;Static&#125; &#123;Instruction&#125;&#125;,&#10;&#125;">Cite</a> | <a href="https://doi.org/10.1145/3776734.3794542">DOI</a></div>
    </div>
  </div>
  </div>
  <div class="card publication-card">
  <div class="publication-grid">
    <div class="publication-image">
      <img src="/assets/images/SA-in-robotics.webp" alt="Publication">
    </div>
    <div class="publication-content">
      <h3 class="publication-title">Investigating the Influence of Spatial Ability in Augmented Reality-assisted Robot Programming</h3>
      <div class="publication-authors">Nicolas Leins, Jana Gonnermann-Müller, Malte Teichmann, Sebastian Pokutta</div>
      <div class="publication-venue">Feb 2026</div>
      <div class="publication-links"><a class="publication-cite" href="#" data-bibtex="@misc&#123;leins_investigating_2026,&#10;	title = &#123;Investigating the &#123;Influence&#125; of &#123;Spatial&#125; &#123;Ability&#125; in &#123;Augmented&#125; &#123;Reality&#125;-assisted &#123;Robot&#125; &#123;Programming&#125;&#125;,&#10;	author = &#123;Leins, Nicolas and Gonnermann-Müller, Jana and Teichmann, Malte and Pokutta, Sebastian&#125;,&#10;	publisher = &#123;arXiv&#125;,&#10;	year = &#123;2026&#125;,&#10;	month = &#123;feb&#125;,&#10;	doi = &#123;10.48550/arXiv.2602.03544&#125;,&#10;	url = &#123;http://arxiv.org/abs/2602.03544&#125;,&#10;	note = &#123;arXiv:2602.03544 [cs]&#125;,&#10;&#125;">Cite</a> | <a href="http://arxiv.org/abs/2602.03544">Preprint</a></div>
    </div>
  </div>
  </div>
  <div class="card publication-card">
  <div class="publication-grid">
    <div class="publication-image">
      <img src="/assets/images/Within_Between.webp" alt="Publication">
    </div>
    <div class="publication-content">
      <h3 class="publication-title">Within-Model vs Between-Prompt Variability in Large Language Models for Creative Tasks</h3>
      <div class="publication-authors">Jennifer Haase, Jana Gonnermann-Müller, Paul H. P. Hanel, Nicolas Leins, Thomas Kosch, Jan Mendling, Sebastian Pokutta</div>
      <div class="publication-venue">Jan 2026</div>
      <div class="publication-links"><a class="publication-cite" href="#" data-bibtex="@misc&#123;haase_within-model_2026,&#10;	title = &#123;Within-&#123;Model&#125; vs &#123;Between&#125;-&#123;Prompt&#125; &#123;Variability&#125; in &#123;Large&#125; &#123;Language&#125; &#123;Models&#125; for &#123;Creative&#125; &#123;Tasks&#125;&#125;,&#10;	author = &#123;Haase, Jennifer and Gonnermann-Müller, Jana and Hanel, Paul H. P. and Leins, Nicolas and Kosch, Thomas and Mendling, Jan and Pokutta, Sebastian&#125;,&#10;	publisher = &#123;arXiv&#125;,&#10;	year = &#123;2026&#125;,&#10;	month = &#123;jan&#125;,&#10;	doi = &#123;10.48550/arXiv.2601.21339&#125;,&#10;	url = &#123;http://arxiv.org/abs/2601.21339&#125;,&#10;	note = &#123;arXiv:2601.21339 [cs]&#125;,&#10;&#125;">Cite</a> | <a href="http://arxiv.org/abs/2601.21339">Preprint</a></div>
    </div>
  </div>
  </div>
  <div class="card publication-card">
  <div class="publication-grid">
    <div class="publication-image">
      <img src="/assets/images/adhd.webp" alt="Publication">
    </div>
    <div class="publication-content">
      <h3 class="publication-title">Stable Personas: Dual-Assessment of Temporal Stability in LLM-Based Human Simulation</h3>
      <div class="publication-authors">Jana Gonnermann-Müller, Jennifer Haase, Nicolas Leins, Thomas Kosch, Sebastian Pokutta</div>
      <div class="publication-venue">Jan 2026</div>
      <div class="publication-links"><a class="publication-cite" href="#" data-bibtex="@misc&#123;gonnermann-muller_stable_2026,&#10;	title = &#123;Stable &#123;Personas&#125;: &#123;Dual&#125;-&#123;Assessment&#125; of &#123;Temporal&#125; &#123;Stability&#125; in &#123;LLM&#125;-&#123;Based&#125; &#123;Human&#125; &#123;Simulation&#125;&#125;,&#10;	author = &#123;Gonnermann-Müller, Jana and Haase, Jennifer and Leins, Nicolas and Kosch, Thomas and Pokutta, Sebastian&#125;,&#10;	publisher = &#123;arXiv&#125;,&#10;	year = &#123;2026&#125;,&#10;	month = &#123;jan&#125;,&#10;	doi = &#123;10.48550/arXiv.2601.22812&#125;,&#10;	url = &#123;http://arxiv.org/abs/2601.22812&#125;,&#10;	note = &#123;arXiv:2601.22812 [cs]&#125;,&#10;	shorttitle = &#123;Stable &#123;Personas&#125;&#125;,&#10;&#125;">Cite</a> | <a href="http://arxiv.org/abs/2601.22812">Preprint</a></div>
    </div>
  </div>
  </div>
  <div class="card publication-card">
  <div class="publication-grid">
    <div class="publication-image">
      <img src="/assets/images/facet.webp" alt="Publication">
    </div>
    <div class="publication-content">
      <h3 class="publication-title">FACET: Multi-Agent AI Supporting Teachers in Scaling Differentiated Learning for Diverse Students</h3>
      <div class="publication-authors">Jana Gonnermann-Müller, Jennifer Haase, Nicolas Leins, Moritz Igel, Konstantin Fackeldey, Sebastian Pokutta</div>
      <div class="publication-venue">Jan 2026</div>
      <div class="publication-links"><a class="publication-cite" href="#" data-bibtex="@misc&#123;gonnermann-muller_facet_2026,&#10;	title = &#123;&#123;FACET&#125;: &#123;Multi&#125;-&#123;Agent&#125; &#123;AI&#125; &#123;Supporting&#125; &#123;Teachers&#125; in &#123;Scaling&#125; &#123;Differentiated&#125; &#123;Learning&#125; for &#123;Diverse&#125; &#123;Students&#125;&#125;,&#10;	author = &#123;Gonnermann-Müller, Jana and Haase, Jennifer and Leins, Nicolas and Igel, Moritz and Fackeldey, Konstantin and Pokutta, Sebastian&#125;,&#10;	publisher = &#123;arXiv&#125;,&#10;	year = &#123;2026&#125;,&#10;	month = &#123;jan&#125;,&#10;	doi = &#123;10.48550/arXiv.2601.22788&#125;,&#10;	url = &#123;http://arxiv.org/abs/2601.22788&#125;,&#10;	note = &#123;arXiv:2601.22788 [cs]&#125;,&#10;	shorttitle = &#123;&#123;FACET&#125;&#125;,&#10;&#125;">Cite</a> | <a href="http://arxiv.org/abs/2601.22788">Preprint</a></div>
    </div>
  </div>
  </div>
</div>

<div style="margin-bottom: 40px;">
  <h2 style="margin-bottom: 28px; font-size: 1.8em;">2025</h2>
  <div class="card publication-card">
  <div class="publication-grid">
    <div class="publication-image">
      <img src="/assets/images/fig_RobotAR.webp" alt="Publication">
    </div>
    <div class="publication-content">
      <h3 class="publication-title">UR5e Augmented Reality Interface on Meta Quest 3</h3>
      <div class="publication-authors">Nicolas Leins</div>
      <div class="publication-venue">Aug 2025</div>
      <div class="publication-links"><a class="publication-cite" href="#" data-bibtex="@misc&#123;leins_ur5e_2025,&#10;	title = &#123;&#123;UR5e&#125; &#123;Augmented&#125; &#123;Reality&#125; &#123;Interface&#125; on &#123;Meta&#125; &#123;Quest&#125; 3&#125;,&#10;	author = &#123;Leins, Nicolas&#125;,&#10;	year = &#123;2025&#125;,&#10;	url = &#123;https://github.com/NLeins/UR5e-Augmented-Reality-Quest3-Interface&#125;,&#10;&#125;">Cite</a> | <a href="https://github.com/NLeins/UR5e-Augmented-Reality-Quest3-Interface">Link</a></div>
    </div>
  </div>
  </div>
</div>

<div style="margin-bottom: 40px;">
  <h2 style="margin-bottom: 28px; font-size: 1.8em;">2024</h2>
  <div class="card publication-card">
  <div class="publication-grid">
    <div class="publication-image">
      <img src="/assets/images/fig_ICIS.webp" alt="Publication">
    </div>
    <div class="publication-content">
      <h3 class="publication-title">Value by Design: Reducing Cognitive Load by Using Visual Guidance in Augmented Reality - An Eye-Tracking Study</h3>
      <div class="publication-authors">Jana Gonnermann-Müller, Nicolas Leins, Norbert Gronau, Thomas Kosch</div>
      <div class="publication-venue">ICIS 2024 Proceedings, Dec 2024</div>
      <div class="publication-links"><a class="publication-cite" href="#" data-bibtex="@article&#123;gonnermann-muller_value_2024,&#10;	title = &#123;Value by &#123;Design&#125;: &#123;Reducing&#125; &#123;Cognitive&#125; &#123;Load&#125; by &#123;Using&#125; &#123;Visual&#125; &#123;Guidance&#125; in &#123;Augmented&#125; &#123;Reality&#125; - &#123;An&#125; &#123;Eye&#125;-&#123;Tracking&#125; &#123;Study&#125;&#125;,&#10;	author = &#123;Gonnermann-Müller, Jana and Leins, Nicolas and Gronau, Norbert and Kosch, Thomas&#125;,&#10;	journal = &#123;ICIS 2024 Proceedings&#125;,&#10;	year = &#123;2024&#125;,&#10;	month = &#123;dec&#125;,&#10;	url = &#123;https://aisel.aisnet.org/icis2024/humtechinter/humtechinter/18&#125;,&#10;	shorttitle = &#123;Value by &#123;Design&#125;&#125;,&#10;&#125;">Cite</a> | <a href="https://aisel.aisnet.org/icis2024/humtechinter/humtechinter/18">Link</a></div>
    </div>
  </div>
  </div>
  <div class="card publication-card">
  <div class="publication-grid">
    <div class="publication-image">
      <img src="/assets/images/fig_springerVR.webp" alt="Publication">
    </div>
    <div class="publication-content">
      <h3 class="publication-title">Comparing head-mounted and handheld augmented reality for guided assembly</h3>
      <div class="publication-authors">Nicolas Leins, Jana Gonnermann-Müller, Malte Teichmann</div>
      <div class="publication-venue">Journal on Multimodal User Interfaces, Sep 2024</div>
      <div class="publication-links"><a class="publication-cite" href="#" data-bibtex="@article&#123;leins_comparing_2024,&#10;	title = &#123;Comparing head-mounted and handheld augmented reality for guided assembly&#125;,&#10;	author = &#123;Leins, Nicolas and Gonnermann-Müller, Jana and Teichmann, Malte&#125;,&#10;	journal = &#123;Journal on Multimodal User Interfaces&#125;,&#10;	year = &#123;2024&#125;,&#10;	month = &#123;sep&#125;,&#10;	doi = &#123;10.1007/s12193-024-00440-1&#125;,&#10;	url = &#123;https://doi.org/10.1007/s12193-024-00440-1&#125;,&#10;&#125;">Cite</a> | <a href="https://doi.org/10.1007/s12193-024-00440-1">DOI</a></div>
    </div>
  </div>
  </div>
</div>

<hr style="border-top: 1px solid #f3f4f6; margin: 40px 0;">

<h2 style="font-size: 1.8em; margin-bottom: 20px;">Citation Profiles</h2>
<ul style="font-size: 1.1em; line-height: 1.8;">
<li><a href="https://scholar.google.com/citations?user=DuqZJvsAAAAJ&hl=de&authuser=1">Google Scholar</a></li>
<li><a href="https://www.researchgate.net/profile/Nicolas-Leins?ev=hdr_xprf">ResearchGate</a></li>
</ul>
