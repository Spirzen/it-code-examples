class DataHolder implements Cloneable {
    private int value;
    private String[] items;
    
    public DataHolder(int value, String[] items) {
        this.value = value;
        this.items = items;
    }
    
    @Override
    protected Object clone() throws CloneNotSupportedException {
        DataHolder copy = (DataHolder) super.clone();
        copy.items = this.items.clone();  // глубокое копирование массива
        return copy;
    }
    
    public void setValue(int value) { this.value = value; }
    public void setItems(String[] items) { this.items = items; }
    public int getValue() { return value; }
    public String[] getItems() { return items; }
}

DataHolder original = new DataHolder(100, new String[]{"a", "b", "c"});
try {
    DataHolder copy = (DataHolder) original.clone();
    copy.setValue(200);
    copy.getItems()[0] = "x";
    
    System.out.println(original.getValue());      // 100 — значение не изменилось
    System.out.println(original.getItems()[0]);   // a — первый элемент массива не изменился благодаря глубокому копированию
} catch (CloneNotSupportedException e) {
    e.printStackTrace();
}
