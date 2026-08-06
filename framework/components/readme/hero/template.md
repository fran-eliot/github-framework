<!--
  Component: README-HERO
  Version: 1.0.0

  Required inputs:
  - project_name
  - tagline

  Optional inputs:
  - banner.source
  - banner.alt
  - banner.link
  - badges
  - short_description
  - alignment

  Do not edit the component structure unless the component version
  and metadata.yml are updated accordingly.
-->

{{#if banner}}
{{#if banner.link}}

<p align="{{ alignment }}">
  <a href="{{ banner.link }}">
    <img
      src="{{ banner.source }}"
      alt="{{ banner.alt }}"
      width="100%"
    />
  </a>
</p>
{{else}}
<p align="{{ alignment }}">
  <img
    src="{{ banner.source }}"
    alt="{{ banner.alt }}"
    width="100%"
  />
</p>
{{/if}}
{{/if}}

<h1 align="{{ alignment }}">
  {{ project_name }}
</h1>

<p align="{{ alignment }}">
  <strong>{{ tagline }}</strong>
</p>

{{#if badges}}

<p align="{{ alignment }}">
{{#each badges}}
  {{#if link}}<a href="{{ link }}">{{/if}}<img src="{{ image }}" alt="{{ alt }}" />{{#if link}}</a>{{/if}}
{{/each}}
</p>
{{/if}}

{{#if short_description}}

<p align="{{ alignment }}">
  {{ short_description }}
</p>
{{/if}}
