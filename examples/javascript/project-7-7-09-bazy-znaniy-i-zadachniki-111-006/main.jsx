// src/components/HomepageHeader.js

import React from 'react';

export default function HomepageHeader() {
  return (
    <header className="hero">
      <h1>Заголовок Секции</h1>
      <p>Описание функционала</p>
      <a href="/docs" className="button button--primary">
        Начать изучение
      </a>
    </header>
  );
}
