package com.MavenFW.testCases;

import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Parameters;

import com.MavenFW.utilities.ExcelUtil;
import com.MavenFW.utilities.ReadConfig;

public class BaseClass extends ExcelUtil {
	
	ReadConfig readconfig = new ReadConfig();
	
	public String baseURL = readconfig.getApplicationURL();
	public String UserName = readconfig.getUserName();
	public String Password = readconfig.getPassword();
	public WebDriver driver;
	public Logger logger;
	
	@Parameters("browser")
	@BeforeClass
	public void setup( String br){

		logger = Logger.getLogger("MavenFW");
		PropertyConfigurator.configure("log4j.properties");
		
		if(br.equals("chrome"))
		{
			System.setProperty("webdriver.chrome.driver",readconfig.getChromePath());
			driver = new ChromeDriver();
		}
		else if(br.equals("firefox")){
			System.setProperty("webdriver.gecko.driver",readconfig.getFirefoxPathL());
			driver = new FirefoxDriver();
		}
		driver.manage().window().maximize();
		driver.get(baseURL);
		logger.info("URL is Opened");
		
		}
	
	@DataProvider(name="LoginData")
	public Object[][] getData() {
		excelPath = (System.getProperty("user.dir")+"/testData/Data.xlsx");
		Object[][] arrayObject = getExcelData(excelPath,"Sheet1");
		return arrayObject;
	}

	public String[][] getExcelData(String excelPath, String sheetName) {
		String[][] arrayExcelData = null;

			int rc = getRowCount();
			int cc = getColCount();
			arrayExcelData = new String[rc-1][cc];
			
			for (int i= 1 ; i < rc; i++) {
				for (int j=0; j < cc; j++) {
					arrayExcelData[i-1][j] = getCellDataString(i, j);
				}

			}
		return arrayExcelData;
	}
	
	@AfterClass
	public void tearDown(){
		driver.close();
		
	}

}
