class ImageLoader {
    constructor() {
        this.cache = new Map();
        this.registry = new FinalizationRegistry(key => {
            console.log(`Изображение ${key} удалено из кэша`);
            this.cache.delete(key);
        });
    }
    
    load(url) {
        if (this.cache.has(url)) {
            return this.cache.get(url);
        }
        
        const image = new Image();
        image.src = url;
        
        this.cache.set(url, image);
        this.registry.register(image, url);
        
        return image;
    }
    
    clear() {
        this.cache.clear();
        console.log("Кэш изображений очищен");
    }
}

const loader = new ImageLoader();
const img1 = loader.load("image1.jpg");
const img2 = loader.load("image2.jpg");

// После удаления ссылок изображения будут удалены из кэша
