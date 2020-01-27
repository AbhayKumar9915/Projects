package com.guru99.testCases;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;

public class BaseClass {
	
	public static String baseURL = "https://demo.guru99.com/V4/";
	public static String UserName = "mngr239663";
	public static String Password = "yjAmepu	";
	public static WebDriver driver;
	
	@BeforeClass
	public void setup(){
		System.setProperty("webdriver.chrome.driver",System.getProperty("user.dir")+"//Drivers//chromedriver.exe");
		driver = new ChromeDriver();
		driver.manage().window().maximize();
		
	}
	
	@AfterClass
	public void tearDown(){
		driver.close();
		
	}

}
