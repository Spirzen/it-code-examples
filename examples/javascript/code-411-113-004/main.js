// Сторона JavaScript
class NativeBridge {
    constructor() {
        this.callbacks = new Map();
        this.callId = 0;
    }

    call(method, params = {}) {
        return new Promise((resolve, reject) => {
            const id = ++this.callId;
            this.callbacks.set(id, { resolve, reject });

            const message = {
                id: id,
                method: method,
                params: params,
                timestamp: Date.now()
            };

            this.sendToNative(JSON.stringify(message));
        });
    }

    sendToNative(message) {
        // Платформенно-зависимая реализация
        if (window.AndroidBridge) {
            window.AndroidBridge.postMessage(message);
        } else if (window.webkit?.messageHandlers?.nativeBridge) {
            window.webkit.messageHandlers.nativeBridge.postMessage(message);
        }
    }

    handleResponse(response) {
        const { id, result, error } = JSON.parse(response);
        const callback = this.callbacks.get(id);
        if (callback) {
            if (error) {
                callback.reject(new Error(error));
            } else {
                callback.resolve(result);
            }
            this.callbacks.delete(id);
        }
    }
}

window.bridge = new NativeBridge();
