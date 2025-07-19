/**
 * 
 * @author ChiangWei
 * @date 2020/4/9
 *
 */

public class FindKMP {
	public static void main(String[] args) {
		System.out.println(FindKMP.findKMP(new String("ABABABAB").toCharArray(), new String("ABABABAB").toCharArray()));
		System.out.println(FindKMP.findKMP(new String("ABABABCB").toCharArray(), new String("CB").toCharArray()));
		System.out.println(FindKMP.findKMP(new String("ABABABAB").toCharArray(), new String("AD").toCharArray()));
	}
	
	public static int findKMP(char[] text, char[] pattern) {
		int n = text.length;
		int m = pattern.length;
		if (m == 0) {
			return 0;
		}
		int[] fail = computeFailKMP(pattern);
		int j = 0;
		int k = 0;
		while (j < n) {
			if (text[j] == pattern[k]) {
				if (k == m - 1) {
					return j - m + 1;
				}
				j++;
				k++;
			} else if (k > 0) {
				k = fail[k - 1];
			} else {
				j++;
			}
		}
		return -1;
	}

	private static int[] computeFailKMP(char[] pattern) {
		int m = pattern.length;
		int[] fail = new int[m];
		int j = 1;
		int k = 0;
		while (j < m) {
			if (pattern[j] == pattern[k]) {
				fail[j] = k + 1;
				j++;
				k++;
			} else if (k > 0)
				k = fail[k - 1];
			else {
				j++;
			}
		}
		return fail;
	}
}
