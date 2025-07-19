/**
 * 
 * @author ChiangWei
 * @date 2020/2/21
 *
 */

package Sample1;

import java.util.ArrayList;

public class PancakeHouseMenu {
	ArrayList menuItems;
	
	public PancakeHouseMenu() {
		menuItems = new ArrayList();
		
		addItem("K&B's Pancake Breakfast", "Pancakes with scrambled eggs, and toast", true, 2.99);
		addItem("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", false, 2.99);
		addItem("Blueberry Pancakes", "Pancakes made with fresh blueberries, and blueberry syrup", true, 3.49);
		addItem("Waffles", "Waffles, with your choice of blueberries or strawberries", true, 3.59);
	}
	
	public void addItem(String name, String description, boolean vegetarian, double price) {
		MenuItem menuItem = new MenuItem(name, description, vegetarian, price);
		menuItems.add(menuItem);
	}
	
	public Iterator createIterator() {
		return new PancakeHouseMenuIterator(menuItems);
	}
}
