public class Knight : Warrior
{
    public string HorseName { get; set; }
    
    // base — аналог super в Java
    public Knight(string name, string horseName, int level = 1) 
        : base(name, level)
    {
        HorseName = horseName;
    }
    
    public override string ToString() 
        => $"{base.ToString()} на коне {HorseName}";
}
