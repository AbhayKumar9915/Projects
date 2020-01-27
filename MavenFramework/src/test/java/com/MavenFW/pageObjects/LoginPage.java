package com.MavenFW.pageObjects;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.PageFactory;

public class LoginPage extends Locators{
	
	  WebDriver driver;
	  
	  public LoginPage(WebDriver rdriver) {
	  driver = rdriver;
	  PageFactory.initElements(rdriver, this); 
	  }
	  
	  public void setUserName(String uname) {
		  driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
	      driver.findElement(By.xpath(UserName_Xpath)).clear();
		  driver.findElement(By.xpath(UserName_Xpath)).sendKeys(uname);
	  }	
	
	  public void setPassword(String pwd) {
		  driver.findElement(By.xpath(Password_Xpath)).clear();
		  driver.findElement(By.xpath(Password_Xpath)).sendKeys(pwd);
	  }
	
	  public void clickLogin() {
		  driver.findElement(By.xpath(btnLogin_Xpath)).click();
	  }

	  public void clickWelcomeAdmin() {
		  driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		  driver.findElement(By.xpath(WelcomeAdmin_Xpath)).click();
	  }

	  public void clickLogout() {
		  driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		  driver.findElement(By.xpath(LogoutBtn_Xpath)).click();
	  }
}
