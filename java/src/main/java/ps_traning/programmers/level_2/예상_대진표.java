package ps_traning.programmers.level_2;

public class 예상_대진표 {
    public int solution(int n, int a, int b) {
        int answer = 0;

        while (a != b) {
            if (a % 2 == 0) a = a / 2;
            else a = a / 2 + 1;
            if (b % 2 == 0) b = b / 2;
            else b = b / 2 + 1;
            answer++;
        }

        return answer;
    }
}
