
class Solution {
public:
    vector<vector<int>> helper(TreeNode* root, vector<vector<int>>& ans) {
        if (root == nullptr)
            return {};

        queue<TreeNode*> q;
        q.push(root);

        bool left_to_right = true;

        while (!q.empty()) {
            vector<int> level;

            int size = q.size();

            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();

                level.push_back(node->val);

                if (node->left != nullptr) {
                    q.push(node->left);
                }

                if (node->right != nullptr) {
                    q.push(node->right);
                }
            }

            if (!left_to_right) {
                reverse(level.begin(), level.end());
            }

            ans.push_back(level);

            left_to_right = !left_to_right;
        }

        return ans;
    }

    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> ans;

        helper(root, ans);

        return ans;
    }
};

