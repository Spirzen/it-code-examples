// Определение CSS-правила для ограничения ширины изображений
string customStyles = @"
    img {
        max-width: 95% !important;
        display: block;
        margin: 0 auto;
    }
    
    /* Ограничение ширины таблиц */
    table {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
    }
";

// Внедрение стилей в WebView после завершения загрузки страницы
webView.EvaluateJavaScriptAsync(customStyles);
