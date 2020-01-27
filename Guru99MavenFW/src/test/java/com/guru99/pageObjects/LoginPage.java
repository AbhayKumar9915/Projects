package com.guru99.pageObjects;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.PageFactory;

public class LoginPage {
	
	
	  WebDriver ldriver;
	  
	  public LoginPage(WebDriver rdriver) {
	  ldriver = rdriver;
	  PageFactory.initElements(rdriver, this); 
	  }
	 
	//Xpaths  
	public static String UserName_Xpath = "//input[@name='uid']";
	public static String Password_Xpath = "//input[@name='password']";
	public static String btnLogin_Xpath = "//input[@name='btnLogin']";
	
	
	public void setUserName(String uname) {
		ldriver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		ldriver.findElement(By.xpath(UserName_Xpath)).clear();
		ldriver.findElement(By.xpath(UserName_Xpath)).sendKeys(uname);
	}	
	
	public void setPassword(String pwd) {
		ldriver.findElement(By.xpath(Password_Xpath)).clear();
		ldriver.findElement(By.xpath(Password_Xpath)).sendKeys(pwd);
	}
	
	public void clickSubmit() {
		ldriver.findElement(By.xpath(btnLogin_Xpath)).click();
	}
}
