/**
 * 
 * @author ChiangWei
 * @date 2020�~2��19��
 *
 */

package Sample2;

public class BeverageTestDrive {
	public static void main(String[] args) {
		TeaWithHook teaHook = new TeaWithHook();
		CoffeeWithHook coffeeHook = new CoffeeWithHook();
		
		System.out.println("\nMaking tea...");
		teaHook.prepareRecipe();
		
		System.out.println("\nMaking coffee...");
		coffeeHook.prepareRecipe();
	}
}
