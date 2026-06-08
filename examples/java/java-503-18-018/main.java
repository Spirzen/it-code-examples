class Rectangle {
    protected int width, height;

    public void setWidth(int w) { width = w; }
    public void setHeight(int h) { height = h; }
    public int getArea() { return width * height; }
}

class Square extends Rectangle {
    @Override
    public void setWidth(int w) {
        super.setWidth(w);
        super.setHeight(w); // ← нарушает контракт Rectangle: setWidth не должен менять height
    }

    @Override
    public void setHeight(int h) {
        super.setHeight(h);
        super.setWidth(h);  // ← аналогично
    }
}
