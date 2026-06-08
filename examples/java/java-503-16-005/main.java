class InitOrder {
    static { System.out.print("S1 "); }
    { System.out.print("I1 "); }
    static { System.out.print("S2 "); }
    { System.out.print("I2 "); }

    InitOrder() { System.out.print("C "); }

    static { System.out.print("S3 "); }
    { System.out.print("I3 "); }
}

// При первом обращении к классу:
// S1 S2 S3

// При new InitOrder():
// I1 I2 I3 C
