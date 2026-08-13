class Solution {

    private void backTrack(List<String> ans,StringBuilder sb,int n){
        if(sb.length()==n){
            ans.add(sb.toString());
            return;
        }

        sb.append('1');
        backTrack(ans,sb,n);
        sb.deleteCharAt(sb.length()-1); 


        // 0
        if(sb.length()==0 || sb.charAt(sb.length()-1) != '0'){
            sb.append('0');
            backTrack(ans,sb,n);
            sb.deleteCharAt(sb.length()-1); //backTrack
        }

    }

    public List<String> validStrings(int n) {
        List<String> ans = new ArrayList<>();
        backTrack(ans,new StringBuilder(),n);
        return ans;
    }
}