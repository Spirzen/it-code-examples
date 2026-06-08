// src/components/HomepageHeader.js

import React from 'react';

export default function HomepageHeader() {
  return (
    <header className="hero">
      <h1>Название Проекта</h1>
      <p>Краткое описание предназначения</p>
      <a href="/docs/intro" className="button button--primary">
        Начать чтение
      </a>
    </header>
  );
}
