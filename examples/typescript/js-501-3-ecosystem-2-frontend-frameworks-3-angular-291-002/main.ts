
import { Injectable } from '@angular/core';
import { CanActivateFn } from '@angular/router';
import { map } from 'rxjs';
import { AuthService } from './auth.service';

export const authGuard: CanActivateFn = () => {
  const authService = inject(AuthService);
  return authService.isAuthenticated$.pipe(map(isAuth => isAuth || redirectToLogin()));
};

function redirectToLogin(): boolean {
  // перенаправление через Router
  inject(Router).navigate(['/login']);
  return false;
}
