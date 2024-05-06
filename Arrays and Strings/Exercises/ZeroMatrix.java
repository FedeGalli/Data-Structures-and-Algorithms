//M x N matrix if a element is 0, its entire row and column are set to 0

public class ZeroMatrix {
    public static void zeroMatrix(int[][] matrix) {

        int[][] newMatrix = new int[matrix.length][matrix[0].length];

        for(int i = 0; i < matrix.length; i++) {
            for(int j = 0; j < matrix[i].length; j++) {
                newMatrix[i][j] = 1;
            
            }
        }
        for(int i = 0; i < matrix.length; i++) {
            for(int j = 0; j < matrix[i].length; j++) {

                if (matrix[i][j] == 0) {
                    for (int k = 0; k < matrix.length; k++) {
                        newMatrix[k][j] = 0;
                    }
                    for (int k = 0; k < matrix[i].length; k++) {
                        newMatrix[i][k] = 0;
                    } 
                    break;
                }
            }
        }

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(newMatrix[i][j]);
            }
            System.out.println("");
        }
    }

    public static void main(String[] args) {

        int[][] matrix ={{1, 1, 0, 1} , 
                         {1, 0, 1, 1}, 
                         {1, 1, 1, 1}};
        ZeroMatrix.zeroMatrix(matrix);
    }
}
