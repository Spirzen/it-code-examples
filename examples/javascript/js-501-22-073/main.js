class DateFormatter {
    constructor(locale = "ru-RU", options = {}) {
        this.locale = locale;
        this.options = options;
        this.formatter = new Intl.DateTimeFormat(locale, options);
    }
    
    format(date) {
        return this.formatter.format(date);
    }
    
    formatRange(startDate, endDate) {
        return `${this.format(startDate)} - ${this.format(endDate)}`;
    }
    
    formatRelative(date) {
        const diff = date - Date.now();
        const seconds = Math.floor(diff / 1000);
        const minutes = Math.floor(seconds / 60);
        const hours = Math.floor(minutes / 60);
        const days = Math.floor(hours / 24);
        
        const formatter = new Intl.RelativeTimeFormat(this.locale, { 
            numeric: "auto" 
        });
        
        if (Math.abs(days) >= 1) {
            return formatter.format(days, "day");
        } else if (Math.abs(hours) >= 1) {
            return formatter.format(hours, "hour");
        } else if (Math.abs(minutes) >= 1) {
            return formatter.format(minutes, "minute");
        } else {
            return formatter.format(seconds, "second");
        }
    }
}

const formatter = new DateFormatter("ru-RU", {
    dateStyle: "long",
    timeStyle: "short"
});

const now = new Date();
const tomorrow = new Date(now);
tomorrow.setDate(tomorrow.getDate() + 1);

console.log(formatter.format(now));           // "15 января 2024 г., 14:30"
console.log(formatter.formatRange(now, tomorrow)); // "15 января 2024 г., 14:30 - 16 января 2024 г., 14:30"
console.log(formatter.formatRelative(tomorrow)); // "завтра"
