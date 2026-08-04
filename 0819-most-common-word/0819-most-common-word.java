import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {

        Set<String> ban = new HashSet<>();
        for (String word : banned) {
            ban.add(word);
        }

        paragraph = paragraph.toLowerCase().replaceAll("[^a-z]", " ");

        Map<String, Integer> freq = new HashMap<>();
        String ans = "";
        int max = 0;

        for (String word : paragraph.split("\\s+")) {
            if (word.length() == 0 || ban.contains(word)) {
                continue;
            }

            int count = freq.getOrDefault(word, 0) + 1;
            freq.put(word, count);

            if (count > max) {
                max = count;
                ans = word;
            }
        }

        return ans;
    }
}