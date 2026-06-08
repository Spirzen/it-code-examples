class Point {
    private int x;
    private int y;
    
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    @Override
    public String toString() {
        return "Point[x=" + x + ", y=" + y + "]";
    }
}

Point p = new Point(10, 20);
System.out.println(p);  // Point[x=10, y=20]
System.out.println(p.toString());  // Point[x=10, y=20]
