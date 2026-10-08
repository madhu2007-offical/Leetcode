class Solution {
public:
    unordered_map<long long, int> prefix;

    int dfs(TreeNode* root, long long currSum, int targetSum) {
        if (root == nullptr) {
            return 0;
        }

        currSum += root->val;

        int count = prefix[currSum - targetSum];

        prefix[currSum]++;

        count += dfs(root->left, currSum, targetSum);
        count += dfs(root->right, currSum, targetSum);

        prefix[currSum]--;

        return count;
    }

    int pathSum(TreeNode* root, int targetSum) {
        prefix.clear();
        prefix[0] = 1;

        return dfs(root, 0, targetSum);
    }
};