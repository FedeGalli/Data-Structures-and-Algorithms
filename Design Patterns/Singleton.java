// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Singleton {
    
    private static Singleton _instance = null;
    private int x;
    
    private Singleton() {
        x = 9;
    }
    
    
    public static Singleton getInstance() {
        if (_instance == null) {
            _instance = new Singleton();
        }
        
        return _instance;
    }
    
    public int toStringa() {
        return x;
    }
    
    
    public static void main(String[] args) {
        
        Singleton data = Singleton.getInstance();
        
        System.out.println(data.toStringa());
    }
}