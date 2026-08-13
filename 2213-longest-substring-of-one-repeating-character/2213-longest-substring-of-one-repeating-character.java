class Solution {

    static class Node {
        char leftChar, rightChar;
        int leftLen, rightLen, maxLen, len;

        Node(char c) {
            leftChar = rightChar = c;
            leftLen = rightLen = maxLen = len = 1;
        }
    }

    Node[] tree;
    char[] arr;

    public int[] longestRepeating(String s, String queryCharacters,
                                  int[] queryIndices) {

        int n = s.length();
        arr = s.toCharArray();

        tree = new Node[4 * n];
        build(1, 0, n - 1);

        int k = queryIndices.length;
        int[] ans = new int[k];

        for (int i = 0; i < k; i++) {
            int index = queryIndices[i];
            char c = queryCharacters.charAt(i);

            arr[index] = c;
            update(1, 0, n - 1, index, c);

            ans[i] = tree[1].maxLen;
        }

        return ans;
    }

    void build(int node, int l, int r) {
        if (l == r) {
            tree[node] = new Node(arr[l]);
            return;
        }

        int mid = l + (r - l) / 2;

        build(node * 2, l, mid);
        build(node * 2 + 1, mid + 1, r);

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    void update(int node, int l, int r, int index, char c) {
        if (l == r) {
            tree[node] = new Node(c);
            return;
        }

        int mid = l + (r - l) / 2;

        if (index <= mid) {
            update(node * 2, l, mid, index, c);
        } else {
            update(node * 2 + 1, mid + 1, r, index, c);
        }

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    Node merge(Node a, Node b) {

        Node res = new Node(a.leftChar);

        res.len = a.len + b.len;
        res.leftChar = a.leftChar;
        res.rightChar = b.rightChar;

        // Prefix
        res.leftLen = a.leftLen;

        if (a.leftLen == a.len && a.rightChar == b.leftChar) {
            res.leftLen = a.len + b.leftLen;
        }

        // Suffix
        res.rightLen = b.rightLen;

        if (b.rightLen == b.len && a.rightChar == b.leftChar) {
            res.rightLen = b.len + a.rightLen;
        }

        // Best answer inside either segment
        res.maxLen = Math.max(a.maxLen, b.maxLen);

        // Possible substring crossing the boundary
        if (a.rightChar == b.leftChar) {
            res.maxLen = Math.max(
                res.maxLen,
                a.rightLen + b.leftLen
            );
        }

        return res;
    }
}