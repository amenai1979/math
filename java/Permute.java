
import java.util.ArrayList;

public class Permute{
	String removeChar(int i, String mystring){
			int l = mystring.length();
			String s2="";
                        String s1="";
			if(l==1 || i>=l){
				return "";
			}
			if(i==0){
				s2=mystring.substring(1);
				return s2;
			}
			if(i==l-1){
				s1=mystring.substring(0,l-1);
				return s1;
			}
                        else {
                                s1=mystring.substring(0,i);
				s2=mystring.substring(i+1);
				return s1+s2;
                        }

	} 
	ArrayList<String> permute(String mylist){
		ArrayList<String> permutations = new ArrayList<>();
		for (int i=0; i< mylist.length(); i++){
			String l = mylist;

			if(l.length() == 1){
				ArrayList<String> permutation = new ArrayList<>();
				permutation.add(l);
				return permutation;
			}
			String e = String.valueOf(mylist.charAt(i));
			ArrayList<String> P = permute(this.removeChar(i,l));
			for (int j=0; j< P.size(); j++){
				permutations.add(e+P.get(j));
 			}
		}
		return permutations;
	}
	
	public static void main(String[] arg){
		Permute permutator = new Permute();
		ArrayList<String> permutations = permutator.permute(arg[0]);
		System.out.println(permutations);
	}
}
