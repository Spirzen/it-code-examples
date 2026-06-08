
import 'dart:math';

class Circle {
  double radius;

  Circle(this.radius);

  double get area => pi * radius * radius;

  set area(double value) {
    radius = sqrt(value / pi);
  }
}
