package com.MavenFW.utilities;

import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class ExcelUtil {
	
	public static String excelPath;
	public static XSSFWorkbook wb;
	public static XSSFSheet sheet;
	
	public ExcelUtil() {
		try {
			excelPath = (System.getProperty("user.dir")+"/testData/Data.xlsx");
			wb = new XSSFWorkbook(excelPath);
			sheet = wb.getSheet("Sheet1");
		}catch(Exception e) {
			System.out.println(e.getMessage());
		}
	}
	
	public static int getRowCount() {
		 
		int rowCount = sheet.getPhysicalNumberOfRows();
		return rowCount;
	}
	
	public static int getColCount() {
		 
		int colCount = sheet.getRow(0).getPhysicalNumberOfCells();
		return colCount;
	}
	
	public static String getCellDataString(int rowNum,int colNum) {
		 
		 String s = sheet.getRow(rowNum).getCell(colNum).getStringCellValue();
		return s;
	 }

}
