import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int width = 0;
        int height = 0;
        for(int[] size : sizes ){
            int a = Math.max(size[0],size[1]);
            int b = Math.min(size[0],size[1]);
            width= Math.max(a,width);
            height= Math.max(b,height);
        }
        answer = width*height;
        return answer;
    }
}