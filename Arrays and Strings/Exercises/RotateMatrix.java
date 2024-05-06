//given an image rapresented by n x n matrix, where each pixel is represented by an integer, write an algo to rotate 
//by 90 degrees
public class RotateMatrix {
    public static int[][] rotateMatrix(int[][] matrix) {
        //not in place

        if(matrix.length == 0 || matrix.length != matrix[0].length)
            return new int[0][0];
        
        
        int[][] newMatrix = new int[matrix.length][matrix[0].length];

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                newMatrix[j][matrix.length - i - 1] = matrix[i][j];
            }
        }

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(newMatrix[i][j]);
            }
            System.out.println("");
        }

        return newMatrix;
    }


    public static void main(String[] args) {

        int[][] matrix ={{1, 1, 0, 1} , 
                         {0, 1, 0, 0}, 
                         {1, 1, 1, 0},
                         {0, 0, 0, 1}};
        RotateMatrix.rotateMatrix(matrix);
    }
}
