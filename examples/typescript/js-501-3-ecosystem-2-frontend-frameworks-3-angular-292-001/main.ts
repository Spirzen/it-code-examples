
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Моя первая программа на Angular';
  
  // Состояние для счетчика
  count: number = 0;
  
  // Состояние для текста ввода
  name: string = '';

  // Функции для работы со счетчиком
  increment(): void {
    this.count++;
  }

  decrement(): void {
    this.count--;
  }

  reset(): void {
    this.count = 0;
  }

  // Обработчик ввода имени
  onNameChange(event: Event): void {
    const target = event.target as HTMLInputElement;
    this.name = target.value;
  }
}
