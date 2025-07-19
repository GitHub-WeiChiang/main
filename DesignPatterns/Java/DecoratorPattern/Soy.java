/**
 * 
 * @author ChiangWei
 * @date 2020/02/10
 *
 */

public class Soy extends CondimentDecorator {
	Beverage beverage;
	
	public Soy(Beverage beverage) {
		this.beverage = beverage;
	}

	public String getDescription() {
		return beverage.getDescription() + ", Soy";
	}
	
	public double cost() {
		return .15 + beverage.cost();
	}
}
