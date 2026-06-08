class UserProfile {
    constructor() {
        this.onResize = () => this.recalculateLayout();
        window.addEventListener('resize', this.onResize);
    }

    destroy() {
        // Забыли удалить обработчик!
        // window.removeEventListener('resize', this.onResize);
    }
}
