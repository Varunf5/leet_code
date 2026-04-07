struct TreeNode* createNode(int val) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}
int checkHeight(struct TreeNode* root, bool* isBalanced) {
    if (!root) return 0;
    int leftHeight = checkHeight(root->left, isBalanced);
    int rightHeight = checkHeight(root->right, isBalanced);

    if (abs(leftHeight - rightHeight) > 1) {
        *isBalanced = false;
    }
    return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
}
bool isBalanced(struct TreeNode* root) {
    bool isBalancedTree = true;
    checkHeight(root, &isBalancedTree);
    return isBalancedTree;
}
