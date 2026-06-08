    private void sendRequest() {
        def url = urlField.text?.trim()
        if (!url) {
            JOptionPane.showMessageDialog(this, 'Введите URL', 'Ошибка', JOptionPane.WARNING_MESSAGE)
            return
        }

        setUiBusy(true)
        statusLabel.text = 'Статус: выполняется запрос...'
        metaLabel.text = 'Время: —   Размер: —'
        responseBodyArea.text = ''
        responseHeadersArea.text = ''

        def config = new HttpRequestConfig(
            url: url,
            method: methodCombo.selectedItem as String,
            headers: parseHeaders(headersArea.text),
            body: bodyArea.text ?: ''
        )

        SwingWorker<HttpResponseResult, Void> worker = new SwingWorker<HttpResponseResult, Void>() {
            @Override
            protected HttpResponseResult doInBackground() {
                executor.execute(config)
            }

            @Override
            protected void done() {
                try {
                    showResult(get())
                } catch (Exception e) {
                    showResult(HttpResponseResult.error(e.message ?: e.class.simpleName))
                } finally {
                    setUiBusy(false)
                }
            }
        }
        worker.execute()
    }
