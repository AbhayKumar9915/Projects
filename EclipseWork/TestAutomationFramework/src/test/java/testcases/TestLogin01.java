package testcases;

import org.openqa.selenium.By;
//import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;
//import org.openqa.selenium.WebElement;
//import org.openqa.selenium.support.ui.ExpectedConditions;
//import org.openqa.selenium.support.ui.WebDriverWait;

public class TestLogin01 {

	public static void main(String[] args) {
		String expected_title = "Secure Page page for Automation Testing Practice";
		FirefoxDriver driver = new FirefoxDriver();
		driver.manage().window().maximize();
//		JavascriptExecutor jse = (JavascriptExecutor)driver;
//		jse.executeScript("window.scrollBy(0,800)");
		driver.get("https://practice.expandtesting.com/login");
		driver.findElement(By.id("username")).sendKeys("practice");
		driver.findElement(By.id("password")).sendKeys("SuperSecretPassword!");
		driver.findElement(By.xpath("//button[@type='submit']")).click();
		
		String actual_title = driver.getTitle();
		Assert.assertEquals(actual_title, expected_title);
//		WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
//		WebElement element = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//button[@type='submit']")));
//		element.click();

		driver.close();

	}

}
