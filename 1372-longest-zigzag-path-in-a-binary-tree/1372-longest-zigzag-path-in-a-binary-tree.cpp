class Solution {
public:
    int ans = 0;

    void dfs(TreeNode* root, int left, int right) {
        if (root == nullptr) {
            return;
        }

        ans = max(ans, max(left, right));

        dfs(root->left, right + 1, 0);
        dfs(root->right, 0, left + 1);
    }

    int longestZigZag(TreeNode* root) {
        dfs(root, 0, 0);
        return ans;
    }
};