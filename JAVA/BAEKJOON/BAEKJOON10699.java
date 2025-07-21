package BAEKJOON;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.text.SimpleDateFormat;
import java.util.*;
import java.time.LocalDate;

public class BAEKJOON10699 {
    public void solution() throws Exception{
        BufferedWriter br = new BufferedWriter(new OutputStreamWriter(System.out));
        Date today = new Date();
        SimpleDateFormat df = new SimpleDateFormat("YYYY-MM-dd");
        String result = df.format(today);
        br.write(LocalDate.now().toString() + "\n");
        br.write(result);
        br.close();
    }
}