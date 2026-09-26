class Solution {
    public String evaluate(String s, List<List<String>> knowledge) {


        HashMap<String,String> mp = new HashMap<>();
        for(List<String> pair : knowledge){
            
            String key = pair.get(0);
            String val = pair.get(1);
            mp.put(key,val);
        }

        StringBuilder sb = new StringBuilder();
        int left = 0;
        for(int i = 0;i<s.length();i++){

            char ch = s.charAt(i);

            if(ch == '('){
                
                left = i+1;
                while(left<s.length() && s.charAt(left)!= ')'){
                    left++;
                }
                String s1 = s.substring(i+1,left);

                if(mp.containsKey(s1)){
                    sb.append(mp.get(s1));
                }else{
                    sb.append("?");
                }

                i = left;
            }
            else{
                sb.append(ch);
            }

        }
        return sb.toString();

    }
}