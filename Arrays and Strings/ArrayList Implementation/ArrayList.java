public class ArrayList {    
    String[] data;
    int len = 0;
    
    public ArrayList(String[] data) {
        this.data = data;
        len = 0;
    }

    public ArrayList(int startingLen){

        this.data = new String[startingLen];
        len = 0;
    }

    public ArrayList(){

        this.data = new String[10];
        len = 0;
    }

    public void append(String item) {
        if (outOfSpace()) {
            resize(true);
        }
        this.data[len] = item;
        len++;
        
    }

    public void removeLast() {
        if (len != 0) {
            this.data[len] = null;
            len--;
            if (tooMuchSpace())
                resize(false);
            
        } 
    }

    private boolean outOfSpace() {
        if (len == this.data.length) {
            return true;
        }
        return false;
    }

    private boolean tooMuchSpace() {
        
        if ((len < this.data.length / 2) && this.data.length > 10) {
            return true;
        }
        return false;
    }

    private void resize(boolean needToExpand) {

        String[] tmp  = needToExpand ? new String[this.data.length * 2] : new String[this.data.length / 2];

        for (int i = 0; i < len; i++) {
            tmp[i] = this.data[i];
        }

        this.data = tmp;
    }

    @Override
    public String toString() {
        String s = "";

        for (int i = 0; i < len; i++) {
            s += data[i];
        }

        return s;
    }

    public static void main(String[] args) {
        ArrayList list = new ArrayList();

        list.append("Ciao");
        list.append("come");
        list.append("va");
        list.append(" 4");
        list.append(" 5");
        list.append(" 6");
        list.append(" 7");
        list.append(" 8");
        list.append(" 9");
        list.append(" 10");
        list.append(" 11");

        System.out.println(list.data.length);
        System.out.println(list.toString());

        list.removeLast();

        System.out.println(list.data.length);
        System.out.println(list.toString());

        list.removeLast();

        System.out.println(list.data.length);
        System.out.println(list.toString());
    }
}