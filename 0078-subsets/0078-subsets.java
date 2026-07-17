class Solution {
    static List<List<Integer>> res;
    public List<List<Integer>> subsets(int[] nums) {
        res=new ArrayList<>();
        ArrayList<Integer>ans= new ArrayList<>();
        dfs(nums,0,ans);
        return res;
    }
    static void dfs(int []nums,int idx,ArrayList<Integer> ans){
        if(idx==nums.length){
            res.add(new ArrayList<>(ans));
            return ;
        }
        ans.add(nums[idx]);
        dfs(nums,idx+1,ans);
        ans.remove(ans.size()-1);
        dfs(nums,idx+1,ans);
    }
}